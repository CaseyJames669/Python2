import csv
from FileUtilities import openFileReadRobust as openRead, \
                          openFileWriteRobust as openWrite

outfile = open('grades.grd', 'w')
with open("grades.csv") as csv_file:

   finalList = []
   gradestr = '{:^16}' + 4 * '  {:>13} '
   finalList.insert(0, gradestr.format('Name', 'HWavg', 'QZavg', 'EXavg', 'Final'))

   for row in csv.reader(csv_file, delimiter=','): # Looping through each row
       name = [] #List of Names
       hw = [] # List of homework scores
       qu = [] # List of quiz scores
       ts = [] # List of test scores

       count = 0
       while count < 2:
           name.append("" if row[count] == '-' else row[count])           
           count += 1
       name == row[0:2]
       
       count = 2

       # Homework
       while count < 14:
           hw.append(0 if row[count] == '-' else row[count])           
           count += 1
       hw = [int(i) for i in hw]
       hwTotal = sum (hw)
       hwPercent = format(hwTotal/ float(395)*100, "10.2f")

       # Quizzes
       while count < 26:
           qu.append(0 if row[count] == '-' else row[count])
           count += 1
       qu = [float(y) for y in qu]
       qu.sort()
       qu.pop(0)
       qu.pop(0)
       quTotal = sum (qu)
       quPercent = format(quTotal/ float(100)*100, "10.2f")

       # Test
       while count < 30:
           ts.append(0 if row[count] == '-' else row[count])
           count += 1
       ts = [float(x) for x in ts]
       ts.sort()
       ts.pop(0)
       tsTotal = sum (ts)
       tsPercent = format(tsTotal/ float(300)*100, "10.2f")

       #Calculating the Final Score
       finalScore = format((float(hwPercent) * .40) + (float(quPercent) * .10)
                           + (float(tsPercent) * .50), "10.2f")
      
       final = (name, hwPercent, quPercent, tsPercent, finalScore)
       finalList.append(final)

finalList.remove(finalList[1])
outfile.write(str(finalList))
outfile.close()
