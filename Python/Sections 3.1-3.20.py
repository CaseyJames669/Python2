#Section 3.1
"""
import math
l = eval(input("Enter the length from the center to a vertex:"))
s = 2 * l * math.sin(math.pi/5)
area = ((3*math.sqrt(3))/2) * s ** 2
print("The area of the pentagon is", format(area, ".2f"))
"""

#Section 3.2
"""
import math
x1,y1 = eval(input("Enter point 1 in degrees:"))
x2,y2 = eval(input("Enter point 2 in degrees:"))
x1 = math.radians(x1)
x2 = math.radians(x2)
y1 = math.radians(y1)
y2 = math.radians(y2)
radius = 6371.01
d = radius * math.acos(math.sin(x1)*math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1-y2))
print("The distance between the two points is ",d,"km")
"""

#Section 3.4
"""
import math
s = eval(input("Enter the side:"))
area = (5 * s ** 2)/ (4* math.tan (math.pi/5))
print("The area of the pentagon is ", area)
"""

#Section 3.5
"""
import math
numSides = eval(input("Enter the number of sides:"))
side = eval(input("Enter the side:"))
area = (numSides * side ** 2) / (4 * math.tan(math.pi/numSides))
print("The area of the polygon is", area)
"""

#Section 3.6
"""
i = eval(input("Enter an ASCII code:"))
i = chr(i)
print("The character is",i)
"""

#Section 3.7
"""
import math
import time
i = math.ceil(time.time())//100000
i = chr(i)
i = i.upper()
print(i)
"""

#Section 3.8
"""
amount = eval(input("Enter the amount:"))
remainingAmount = int(amount)
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

print("Your amount", amount, "consists of \n",
      "\t", numberOfOneDollars, "dollars\n",
      "\t", remainingAmount, "cents")
"""

#Section 3.9
"""
name = input("Enter a employee's name:")
hoursWorked = eval(input("Enter number of hours worked in a week:"))
payRate = eval(input("Enter hourly pay rate:"))
fedTax = eval(input("Enter federal tax rate:"))
stateTax = eval(input("Enter state tax rate:"))

print("Employee Name: ", name)
print("Hours Worked: ", hoursWorked)
print("Pay Rate: $", payRate)
grossPay = hoursWorked * payRate
print("Gross Pay: $", grossPay)
fedTaxW = fedTax * grossPay
stateTaxW = stateTax *grossPay
totalD = fedTaxW + stateTaxW
netPay = grossPay - totalD
print("Deductions: \n",
      "\t Federal Withholding (",fedTax*100,"%)",format(fedTaxW,".2f"),"\n",
      "\t State Withholding (",stateTax*100,"%)",format(stateTaxW,".2f"),"\n",
      "\t Total Deductions: $", format(totalD,".2f"))
print("Net Pay: $", format(netPay,".2f"))
"""

#Section 3.10
"""
import turtle
i = '\u03b1\u03b2\u03b3\u03b4\u03b5\u03b6\u03b7\u03b8'
turtle.write(i, font=("Arial",32, "normal"))
turtle.hideturtle()
"""

#Section 3.11
"""
number = str(input("Enter an integer: "))
print("The reversed number is ", number[::-1])
"""


