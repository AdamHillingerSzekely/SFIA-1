from application import db
from application.models import Test, Question, UserTest, AnsweredQuestion
import random
from application.forms import AnswerVerification

test = Test.query.filter_by(id=1).first()



# create a new user test (/test/create)
def test_create():
	user_questions = []
	for question in test.questions:
		user_questions.append(AnsweredQuestion(question=question.question, answer=question.answer))

	user_test = UserTest(answered_questions=user_questions)

	db.session.add(user_test)
	db.session.commit()
	print(f"redirect('/user/test/{user_test.id})'")
    # redirect user to the test
def question_set():
	form = TakeTest()

	return render_template('questionbankupload.html', title='Question Set', form=form)
# /user/test/<id>
def test_user(id):
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
	if unanswered_questions:
		question = random.choice(unanswered_questions)
		print(f"{question.question}\n{question.answer}")
		# render_template('user-test.html', question=question) 
	print('all questions answered, going to the results')
	# redirect to results

test_create()
test_user(1)
