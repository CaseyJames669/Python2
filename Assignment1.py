"""
Assignment 9:
Grade Calculations and Redirection of Input
This program takes a students name, their 3 test values, 5 quiz values,
drops the lowest of each, and then tells you what the ending grade is.

Preconditions:
    User must enter one name
    Assignments are values between 0-10
    Quizes are values between 0-60
    Tests are values between 0-100
"""
__author__ = 'Casey Bladow'
__date__ = '1/22/13'

def calcTestAvg(testScores):
    """Take the 4 test scores,a nd then find the average

    Purpose: sum up the remaining test scores and find the average
    Preconditions: 4 test have been entered but the lowest has been removed
    Postconditions: the average of the remaining 4 scores is testAvg
    """
    total = sum(testScores) 
    testAvg = total/300
    return testAvg

def calcQuizAvg(quizScores):
    """Find the average of the quiz scores

    Purpose: sum up the remaining quiz scores and find the average
    Preconditions: 12 quiz have been entered but the lowest has been removed
    Postconditions: the average of the remaining 12 scores is quizAvg
    """
    total = sum(quizScores) 
    quizAvg = total/120
    return quizAvg

def calcAssignAvg(assignScores):
    """Find the average of the assignment scores

    Purpose: sum up the remaining assignment scores and find the average
    Preconditions: 12 assignment have been entered but the lowest has been removed
    Postconditions: the average of the remaining 12 scores is assignAvg
    """
    total = sum(assignScores) 
    assignAvg = total/345
    return assignAvg
    
def main():
    numStudents = eval(input("How many students will you be entering data for? "))
    for x in range(0,numStudents):
        data = input("Please enter the students name and scores seperated by "\
                     "comma's: ").title()
        grades = data.split(",")
        grades = [s.strip() for s in grades]
        if '-' in grades:
            '-' == 0
        name = grades[0],grades[1]
        #testScores list initialized
        assignScores = grades[2:13]
        assignScores = [float(s) for s in assignScores]
        #quizScores list initialized
        quizScores = grades[14:25]
        quizScores = [float(s) for s in quizScores]
        #testScores list initialized
        testScores = grades[26:29]
        testScores = [float(s) for s in testScores]
        #lowest test score dropped
        dropTest = testScores.remove(min(testScores))
        testAvg = (sum(testScores))/300
        #score is figured out here. 45% for tests, 10% for quizes, 45% for
        #homework. The quizes are then multiplied by ten to add the
        #additional zero and send out the appropriate value.
        score = (testAvg*.45)+((quizAvg*.10)*10)+((assignAvg*.45)*10)
        print("Name \t HWavg \t QZavg \t EXavg \t Final")
        # ERROR - I cant figure out how to break this line to make the
        #Col:80!!! 
        print(grades[1],",",grades[0] + '\t' + str(calcAssignAvg(assignScores))+
        	'\t' + str(calcQuizAvg(quizScores)) + '\t' + 
		str(calcTestAvg(testScores)) + '\t' + str(score))

if __name__ == '__main__':
    main()
