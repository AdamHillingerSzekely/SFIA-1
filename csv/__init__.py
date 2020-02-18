class Test():
	def __init__(self, Question='', Answer=''):
		self.Question = Question
		self.Answer = Answer

	def __repr__(self):
		return "Question: %s\nAnswer: %s"





# open the csv file in read mode (r)
with open(sfia-1/csv/RandDtest.csv, 'r') as csv_file:
    # get a list of the rows
    rows = csv.reader(csv_file)
    # for every row in the rows list, print it 
    for row in rows:
        print(row)
