#4.2
"""
import random
a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
ans = eval(input("What is " + str(a) + "+" + str(b) + "+" + str(c) + "? "))
d = a+b+c
if ans == d:
    print("Correct!")
else:
    print("Incorrect.")
    
"""

#4.3
"""
a,b,c,d,e,f = eval(input("Enter a, b, c, d, e, f: "))
errorCheck = ((a*d)-(b*c))
if errorCheck == 0:
    print("No Solution.")
else:
    x = ((e*d)-(b*f))/((a*d)-(b*c))
    y = ((a*f)-(e*c))/((a*d)-(b*c))
    print("x is ", x, "and y is ", y)
"""

#4.4
"""
import random
a = random.randint(0,99)
b = random.randint(0,99)
ans = eval(input("What is " + str(a) + "+" + str(b) + "? "))
c = a + b
if ans != c:
    print("False.")
else:
    print("Correct.")
"""

#4.5
"""
today = eval(input("Enter today's day: "))
daysElapsed = eval(input("Enter the number of days elapsed since today: "))

if (today == 0):
    nameForToday = "Sunday"
else:
    if (today == 1):
        nameForToday = "Monday"
    else:
        if (today == 2):
            nameForToday = "Tuesday"
        else:
            if (today == 3):
                nameForToday = "Wednesday"
            else:
                if (today == 4):
                    nameForToday = "Thursday"
                else:
                    if (today == 5):
                        nameForToday = "Friday"
                    else:
                        if (today == 6):
                            nameForToday = "Saturday"
newDay = (today + daysElapsed) % 7 
if (newDay == 0):
    newDay = "Sunday"
else:
    if (newDay == 1):
        newDay = "Monday"
    else:
        if (newDay == 2):
            newDay = "Tuesday"
        else:
            if (newDay == 3):
                newDay = "Wednesday"
            else:
                if (newDay == 4):
                    newDay = "Thursday"
                else:
                    if (newDay == 5):
                        newDay = "Friday"
                    else:
                        if (newDay == 6):
                            newDay = "Saturday"

print("Today is", nameForToday, "and the future day is", newDay)
"""

#4.6
"""
weight = eval(input("Enter your weight: "))
feet = eval(input("Enter feet: "))
inches = eval(input("Enter inches: "))
ftInches = feet * 12
height = ftInches + inches
KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254
weightInK = weight * KILOGRAMS_PER_POUND
heightInM = height * METERS_PER_INCH
bmi = weightInK / (heightInM * heightInM)
print("BMI is", format(bmi, ".2f"))
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are normal.")
elif bmi < 30:
    print("You are overwieght.")
else:
    print("you are Obese.")
"""

#4.7
"""
amount = eval(input("Enter the amount:"))
remainingAmount = int(amount * 100)
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

numberOfQuaters = remainingAmount // 25
remainingAmount = remainingAmount % 25

numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

numberOfPennies = remainingAmount

print("Your amount", amount, "consists of ")
if numberOfOneDollars > 1:
    print("\t", numberOfOneDollars, "dollars")
elif numberOfOneDollars == 1:
    print("\t", numberOfOneDollars, "dollar")
    
if numberOfQuaters > 1:
    print("\t", numberOfQuaters, "quaters")
elif numberOfQuaters == 1:
    print("\t", numberOfQuaters, "quater")

if numberOfDimes > 1:
    print("\t", numberOfDimes, "dimes")
elif numberOfDimes == 1:
    print("\t", numberOfDimes, "dime")

if numberOfNickels > 1:
    print("\t", numberOfNickels, "nickels")
elif numberOfNickels == 1:
    print("\t", numberOfNickels, "nickel")

if numberOfPennies > 1:
    print("\t", numberOfPennies, "pennies")
elif numberOfPennies == 1:
    print("\t", numberOfPennies, "penny")
"""

#4.8
"""
a,b,c = eval(input("Enter 3 integars: "))
numbers = [a,b,c]
numbers.sort()
print(numbers)
"""

#4.9
"""
weight1, price1 = eval(input("Enter weight and price for package 1: "))
weight2, price2 = eval(input("Enter weight and price for package 2: "))
total1 = weight1/price1
total2 = weight2/price2
if total1 < total2:
    print("Package 1 has the better price.")
else:
    print("Package 2 has the better price.")
"""

#4.10
"""
import random
a = random.randint(0,99)
b = random.randint(0,99)
ans = eval(input("What is " + str(a) + "*" + str(b) + "? "))
d = a*b
if ans == d:
    print("Correct!")
else:
    print("Incorrect.")
"""

#4.11
"""
month, year = eval(input("Enter month, year: "))

if (month == 1):
    nameForMonth = "January"
    daysInMonth = 31
elif (month == 2):
    nameForMonth = "Febuary"
    isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year %400 == 0)
    if isLeapYear == True:
        daysInMonth = 29
    elif isLeapYear != True:
        daysInMonth = 28
elif (month == 3):
    nameForMonth = "March"
    daysInMonth = 31
elif (month == 4):
    nameForMonth = "April"
    daysInMonth = 30
elif (month == 5):
    nameForMonth = "May"
    daysInMonth = 31
elif (month == 6):
    nameForMonth = "June"
    daysInMonth = 30
elif (month == 7):
    nameForMonth = "July"
    daysInMonth = 31
elif (month == 8):
    nameForMonth = "August"
    daysInMonth = 31
elif (month == 9):
    nameForMonth = "September"
    daysInMonth = 30
elif (month == 10):
    nameForMonth = "October"
    daysInMonth = 31
elif (month == 11):
    nameForMonth = "November"
    daysInMonth = 30
elif (month == 12):
    nameForMonth = "December"
    daysInMonth = 31

print(nameForMonth, year,"has", daysInMonth,"days.")
"""

#4.12
"""
x = eval(input("Enter an integer: "))
if (x % 5 ==0 and x % 6 == 0):
    print(x,"is divisible by both 5 and 6.")
elif (x % 5 == 0):
    print(x,"is divisible by 5.")
elif (x % 6 ==0):
    print(x,"is divisible by 6.")
else:
    print(x,"is not divisible by 5 or 6.")
"""

#4.14
"""
import random
guess = input("Heads or Tails?")
answer = random.randint(0,1)
if answer == 1:
    answer = "Heads"
else:
    answer = "Tails"
if guess == answer:
    print("You Win!!")
else:
    print("Wrong!!")
"""
#4.15


