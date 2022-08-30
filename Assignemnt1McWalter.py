#Question 1
#Write a program that asks the user to input marks obtained in three tests. Your program should display the
#average test score.


from decimal import ROUND_UP
from socket import INADDR_ALLHOSTS_GROUP


FirstGrade=float(input('\n'"Enter 1st grade: "))
SecondGrade=float(input("Enter 2nd grade: "))
ThirdGrade=float(input("Enter 3rd grade: "))

#calculate the total
total1 = FirstGrade + SecondGrade + ThirdGrade
#calculate the average
average = total1/3
print("The total grade is: ", total1)
print("The average is: ",average )
print('\n')

#Question 2
#Write a program that asks the user to input base and height of a triangle as integer. Your program should
#calculate and display the area of triangle using formula area = 1/2 * base * height.

Base=float(input("Enter the base of the triangle: "))
Height=float(input("Enter the \b height of the triangle: "))
'\n'
#calculate the total
area = .5 * Base * Height
#calculate the average

print("The total \b area is: ", area)
print('\n')

#Question 3
#Write a program that asks the user to input his height in centimeters. Your program should convert and display the
#height in Feet and inches. (Hint: 1 inch equals 2.54 centimeters and 1 foot equals 12 inches)
import math
height=float(input('\n'"Enter person's height in Centimeters: "))
inches=height*0.3937
feet=height*0.0328084



print('\n'"The height of the person in Feet is: ",math.trunc(feet))
print('\n'"The height of the person in inches is:",math.trunc(inches))

