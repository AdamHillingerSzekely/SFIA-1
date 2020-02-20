from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt
from application.models import Posts, Users, Test, Question, UserTest, AnsweredQuestion
from application.forms import PostForm, RegistrationForm, LoginForm, UpdateAccountForm, TakeTest, AnswerVerification, QuestionGenerator
import random


blogData = [{ "name": {"first":"John", "last":"Doe"},
"title":"First Post",
"content":"This is some big data for Flask lectures"},
{
        "name": {"first":"Jane", "last":"Doe"},
        "title":"Second Post",
        "content":"This is even more blog data for Flask lectures"}]


@app.route('/')
@app.route('/home')
def home():
	postData = Posts.query.all()
	return render_template('home.html', title='Home', posts=postData)

@app.route('/about')
def about():
	return render_template('about.html', title='About')


@app.route('/question_set', methods=['GET', 'POST'])
def question_set():
    form = TakeTest()
    return render_template('questionbankupload.html', title='Question Set', form=form)

@app.route('/user/test/create')
def user_test_create():
    test = Test.query.filter_by(id=1).first()
    user_questions = []
    print('creating user questions')
    for question in test.questions:
        user_questions.append(AnsweredQuestion(question=question.question, answer=question.answer, attempts = 0))
    print('creating user test')
    user_test = UserTest(answered_questions=user_questions)
    db.session.add(user_test)
    db.session.commit()
    db.session.refresh(user_test)
    return redirect(url_for('testpage', id=user_test.id))


@app.route('/user/testpage/<id>')
def testpage(id):
    form = QuestionGenerator()
    user_test = UserTest.query.filter_by(id=id).first()
    #for question in user_test:
    #if answer == question.answer:

    # check the answer
    # - make sure you get the question id from the form
    # - get the data from the form
    # - compare the answer to the questions given

    # get a random question
    unanswered_questions = []
    for question in user_test.answered_questions:
        if not question.completed:
            unanswered_questions.append(question)
    print(unanswered_questions)
    if unanswered_questions:
        question = random.choice(unanswered_questions)
        print(f"{question.question}\n{question.answer}")
        return render_template('testpage.html', title='The Test', question=question, form=form, test_id=id)
    # render_template('user-test.html', question=question)
    print('all questions answered, going to the results')
    return redirect(url_for('analysis', test_id=id))

@app.route('/test/<test_id>/question/<question_id>', methods=['POST'])
def user_question(test_id, question_id):
    answered_question = AnsweredQuestion.query.filter_by(id=question_id).first()
    form = QuestionGenerator()
    user_answer = form.question.data
    print("Actual answer: " + answered_question.answer + "\nUser answer: " + user_answer)
    if answered_question.answer == user_answer:
        answered_question.completed = True
        print('answer is correct !')
    else:
        print('answer is incorrect !')
        answered_question.attempts = answered_question.attempts + 1
    db.session.add(answered_question)
    db.session.commit()
    return redirect(url_for('testpage', id=test_id))

@app.route('/test/<test_id>/analysis', methods=['GET', 'POST'])
def analysis(test_id):
	results=AnsweredQuestion.query.filter_by(user_test_id=test_id)

	return render_template('analysis.html', results=results)



@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user=Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=[ 'GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

		user = Users(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			email = form.email.data,
			password = hash_pw
		)

		db.session.add(user)
		db.session.commit()

		return redirect(url_for('post'))
	return render_template('register.html', title='Register', form=form)

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
	form = PostForm()
	if form.validate_on_submit():
		postData = Posts(
			title = form.title.data,
			content = form.content.data,
			author=current_user
		)

		db.session.add(postData)
		db.session.commit()

		return redirect(url_for('home'))
	else:
		print(form.errors)

	return render_template('post.html', title='Post', form=form)


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
	user = current_user.id

	account = Users.query.filter_by(id=user).first()
	posts= Posts.query.filter_by(user_id=user).all()
	logout_user()
	for post in posts:
			db.session.delete(post)
	db.session.delete(account)
	db.session.commit()
	return redirect(url_for('register'))
