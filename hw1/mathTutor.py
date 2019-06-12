"""
file: mathTutor.py
author: Michelle Vered
Prompts user to answer solve various math problems and checks their work
"""

from random import randint
import csv

# global variables
GRADES = [1,2,3]
NUM_QUESTIONS = 5

def main():
	"""Program which asks users to solve math problems and checks their work"""
	name, grade = welcome()
	allResults = []
	for i in range(1,NUM_QUESTIONS+1):
		print('Problem #%d:' % i, end='')
		num1,num2 = generateQuestion(grade)
		result = askQuestion(num1,num2,name)
		allResults.append(result)
	score = calculateScore(allResults,name)
	logResults(name,grade,score)

def welcome():
	"""Displays welcome message; prompts user for name and grade
	valid inputs for grade are GRADES, else it will prompt user to re-enter"""
	print('')
	print('Welcome to the Math Tutor') # prints welcome message
	print('')

	name = input('Enter your name: ') # prompts for name

	gradesText = ', '.join(str(i) for i in GRADES) # converts GRADES to string 
	grade = input('Enter your grade (%s): ' % gradesText) # prompts for grade
	try:
		grade = int(grade) # converts grade to int
		if grade not in GRADES: # if grade is int but not in list of grades, re-prompts user
			grade = input('Sorry, invalid grade. Please re-enter your grade using only (%s): ' % gradesText)
			grade = int(grade)
	except:  # if user inputted grade cannot be converted to integer then re-prompts
		grade = input('Sorry, invalid grade. Please re-enter your grade using only (%s): ' % gradesText)
		grade = int(grade)
	
	print('')
	print('Directions: Please answer the following %s problems %s.' % (str(NUM_QUESTIONS),name))
	print('')
	
	return name, grade


def generateQuestion(grade):
	"""Generates math problem for user based on grade level, prompts user to solve problem"""

	# sets range for numbers in problem, depending on grade level
	if grade == 1:
		numRange = [0,9]
	elif grade == 2:
		numRange = [10,99]
	elif grade == 3:
		numRange = [100,999]

	# generates the two numbers for use in the problem
	num1 = randint(numRange[0],numRange[1])
	num2 = randint(numRange[0],numRange[1])

	# returns the two numbers for the problem
	return num1, num2



def askQuestion(num1,num2,name):
	"""Checks users answer to math problem, provides feedback message"""
	correctAnswer = num1 + num2

	# gets correct number of spaces for each number so the ones places will all line up
	spacesNum1 = 6 - len(str(num1))
	spacesNum2 = 5 - len(str(num2))
	spacesAnswer = 10 - (len(str(correctAnswer)))

	# prints question and prompts user for answer
	print(' '*spacesNum1,str(num1),sep='')
	print(' '*11,'+',' '*spacesNum2,str(num2),sep='')
	print(' '*13,'----',sep='')
	answerPrompt = 'Answer:' + ' '*spacesAnswer
	userAnswer = int(input(answerPrompt))
	print('')

	# prints feedback message to user to let them know if answer was correct or not
	if correctAnswer == userAnswer:
		message = 'Great ' + name + ', your answer is correct!!!'
		result = True
	else:
		message = 'Sorry ' + name + ', but your answer is incorrect. The correct answer is ' + str(correctAnswer) + '.'
		result = False
	print(message)
	print('')

	# returns True or False depending on if the user got the correct answer
	return result

def calculateScore(allResults, name):
	"""Calculates a total score after all problems have been answered; outputs final results to user"""
	
	# calculates number correct and overall score
	numCorrect = sum(allResults) 
	score = numCorrect / NUM_QUESTIONS

	# prints final results to user
	print('================== Summary ==================')
	print('Bye %s! You answered %s out of %s problems correctly.' % (name,str(numCorrect),str(NUM_QUESTIONS)))
	print('')

	# returns score (pct value)
	return score

def logResults(name,grade,score):
	"""Logs name, grade-level, and score to file"""

	# append data to log file
	with open('Log.txt','a') as file:
			writer = csv.writer(file,delimiter='\t')
			writer.writerow([name,str(grade),str(score)])
	file.close()

main()