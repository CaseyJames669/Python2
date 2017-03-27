#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# file grades.py
# author: Casey Bladow
# 

'''
This script reads an input .cvs file with:
    first name
    surname
    12 homework grades
    12 quiz scores (10 pts each)
     4 exam scores (100 pts each)
line at a time and reports
    first and surname
    averages for each category of score
    averall average and letter grade, per the schedule:
        homework - 40%; quizes - 10%; exams - 50%
        [100, 90] - A; (90, 80] - B; (80, 70] - C; (70, 60] - D; (60, 0] - F
'''
inline = ""
from FileUtilities import openFileReadRobust as openRead, \
                          openFileWriteRobust as openWrite

# Stub function for processing student data                          
def processStudent(data, possible):

    return ["blow, joe", 53, 26, 12, 34]

# Stub function for setting up files for I/O
def setUpIO():
    return infile, outfile 

# Opens the input and output files
infile = open('grades.csv','r')
outfile = open('grades.grd','w')

# Get the homework, quiz, and exam possible totals
line = infile.readline().rstrip('\n').split(',')
hwtot = sum([0 if k == '-' else int(k) for k in line[2:14]])
qztot = 100
extot = 300
totals = [hwtot, qztot, extot]

gradelist = []
grades = []

stuData = infile.readline().rstrip('\n').split(',')
stuData[0] = grades[0:1]
#testScores list initialized
stuData[1] = stuData[2:13]
#stuData[1] = [float(s) for s in stuData]
#quizScores list initialized
stuData[2] = stuData[14:25]
#stuData[2] = [float(s) for s in stuData]
#testScores list initialized
stuData[3] = stuData[26:29]
#stuData[3] = [float(s) for s in stuData]

# For every line in the file, compute the averages and final grade
for line in infile:
    # process line and add it to the list of grades

    #stuData = processStudent(line, totals)
    
    # Add student to grade list
    # Note: this next step could have been done much more elegantly, but
    #       I wanted you to see the formatting
    gradelist.append('{:<16}  {:8.2f}  {:8.2f}  {:8.2f}  {:8.2f}'.format\
                        (stuData[0], stuData[1], stuData[2], stuData[3],
                         stuData[4]))

# Sort list and provide a heading
gradelist.sort()
gradestr = '{:^16}' + 4 * '  {:>8}'
gradelist.insert(0, gradestr.format('Name', 'HWavg', 'QZavg', 'EXavg', 'Final'))

# Write the list to the output file
outfile.write('\n'.join(gradelist) + '\n')

# Close files ... because it's a good thing to do
infile.close()
outfile.close()
