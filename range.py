## In this script, there is an error.
## Clone this project in your machine and correct it.
## adding a new line to show changes in repo
## aaaaa
## The program finds the highest value in the randomly generated array of integer.
## Hint: Check whether the program will function with negative numbers range.
#Arjun is best employee
import random

highest = 0

arraydata = []

for i in range(1, 100):
    arraydata.append(random.randint(0, 100))

print(arraydata)


for num in arraydata:
    if (num > highest):
        highest = num

print(highest)
