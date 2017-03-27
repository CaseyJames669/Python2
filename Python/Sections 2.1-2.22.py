#Section 2.1
"""
c = eval(input("Enter a degree in Celsius: "))
f = (9/5)*c+32
print(c, "Celsius is ", f, "Fahrenheit")
"""

#Section 2.2
"""
import math
radius, length = eval(input("Enter the radius and length of a cylinder:"))
area = radius * radius * math.pi
volume = area * length
print("The area is ",area)
print("The volume is ",volume)
"""

#Section 2.3
"""
feet = eval(input("Enter a value for feet: "))
meters = (feet * .305)
print(feet,"feet is ",meters,"meters")
"""

#Section 2.4
"""
pounds = eval(input("Enter a value in pounds: "))
kilograms = (pounds * .454)
print(pounds,"pounds is", kilograms,"kilograms")
"""

#Section 2.5
"""
subtotal, gr = eval(input("Enter the subtotal and a gratuity rate: "))
ga = (gr * subtotal)/100
total = ga + subtotal
print("The gratuity is ",round(ga,2)," and that totla is ", round(total,2))
"""

#Section 2.6
"""
N = eval(input("Enter a number between 0 and 1000: "))

#Extract values
A=N%10   #Pulls A
N=N//10  #Removes digit

B=N%10 
N=N//10

C=N%10   #Removing C is not needed

total = A + B + C
print("The sum of the digits is ", total)
"""

#Section 2.7
"""
m = eval(input("Enter the number of minutes: "))
years = m//525600
days = (m%525600)//1440
print(m, "minutes is approximately", years," years and", days,"days")
"""

#Section 2.8
"""
m = eval(input("Enter the amount of water in kilograms:"))
intTemp = eval(input("Enter the initial temperature:"))
finalTemp = eval(input("Enter the final temperature:"))
q = m * (finalTemp - intTemp) * 4184
print("The evergy needed is", q)
"""

#Section 2.9
"""
temp = eval(input("Enter the temperature in Fahrenheit between -58 and 41:"))
windSpeed = eval(input("Enter the wind speed in miles per hour:"))
windChillIndex = 35.74 + 0.6215 * temp - 35.75 * windSpeed**.16 + .4275 * temp * windSpeed **.16
print("The wind chill index is", windChillIndex)
"""

#Section 2.10
"""
s,a = eval(input("Enter speed and acceleration:"))
length = (s**2)/(2*a)
print("The minimum runway length for this airplane is", length,"meters")
"""

#Section 2.11
"""
finalAcctValue = eval(input("Enter final account value:"))
APR = eval(input("Enter annual interest rate in percent:"))
MPR = APR/1200
years = eval(input("Enter the number of years:"))
intDepositAmount = finalAcctValue/((1+MPR)**(years*12))
print("Initial deposit value is",intDepositAmount)
"""

#Section 2.12
"""
i=1
print("a b a**b")
while i < 6:
    b=i+1
    print(i, b, i**b)
    i += 1
"""

#Section 2.13
"""
x = eval(input("Enter an integer:"))
A=x%10
x=x//10
B=x%10
x=x//10
C=x%10
x=x//10
D=x

print(D)
print(C)
print(B)
print(A)
"""

#Section 2.14
"""
x1,y1,x2,y2,x3,y3 = eval(input("Enter three points for a triangle:"))
a = int((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)) ** .5
b = int((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3)) ** .5
c = int((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1)) ** .5
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** .5
print("The area of the triangle is", area)
"""

#Section 2.15
"""
s = eval(input("Enter the side:"))
area = ((3*(3 ** .5)/2))* (s ** 2)
print("The area of a the hexagon is", area)
"""

#Section 2.16
"""
v0,v1,t = eval(input("Enter v0, v1, and t:"))
a = (v1-v0)/t
print("The average acceleration is",a)
"""

#Section 2.17
"""
weight = eval(input("Enter weight in pounds:"))
height = eval(input("Enter height in inches:"))
kg = weight * .45259237
meter = height * .0254
bmi = kg / (meter ** 2)
print("BMI is", bmi)
"""

#Section 2.18
"""
import time

currentTime = time.time()
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes //60
currentHour = totalHours % 24
offset = eval(input("Enter the time zone offset to GMT: "))
currentHour = currentHour + offset
print("Current time is", currentHour, ":", currentMinute, ":", currentSecond, "GMT")
"""

#Section 2.19
"""
investAmount = eval(input("Enter investment amount: "))
APR = eval(input("Enter annual interest rate: "))
years = eval(input("Enter number of years: "))
acc = investAmount * ( 1 + (APR/1200)) ** (years*12)
print("Accumulated value is ", acc)
"""

#Section 2.20
"""
bal, apr = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))
interest = bal * (apr / 1200)
print("the interest is ",interest)
"""

#Section 2.21
"""
msa = eval(input("Enter the monthly saving amount:"))
nsa = msa * (1 + .00417)
nsa = (100 + nsa) * (1 + .00417)
nsa = (100 + nsa) * (1 + .00417)
nsa = (100 + nsa) * (1 + .00417)
nsa = (100 + nsa) * (1 + .00417)
nsa = (100 + nsa) * (1 + .00417)
print("After the 6th month, the account value is ", nsa)
"""

#Section 2.22
"""
years = eval(input("Enter the number of years:"))
birth = int(31536000*years)//7
death = int(31536000*years)//16
imm = int(31536000*years)//45

newPop = 312032486 + birth - death + imm
print("The population at", years,"is",newPop)
"""
