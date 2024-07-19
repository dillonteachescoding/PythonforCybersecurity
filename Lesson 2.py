import greet
print(greet.greet("Updog"))

#Lesson 2


#Print a loop of Yeah it works 10 times
for _ in range(10):
    print("Yeah it works 10 times")


#Printing an Elif statement and if or kinda statement

#Prompt the user a number
number = int(input("Please Enter a Number: "))

#Check is that number even or odd
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is not Even")

#Take a input of user for grade
grade = int(input("Enter your grade percentage: "))

#Check the grade
if grade > 90:
    print("You have a A")
elif grade > 80:
    print("You have a B")
elif grade > 70:
    print("You have a C")
else:
    print("Failed")

#Create a script that prompts user for a number, and then
#tells the user if number is even

#Prompt user for number
number = int(input("Give a number: "))

#Check if the value is even or odd
if number % 2 == 0:
    print(f"{number} is even!")
else:
    print(f"{number} is false!")


#Prompt a user with a question
answer = input("Is today a good day? (y/n): ")

#Check that response if user did yes, or no
if answer.lower() == 'y':
    for _ in range (10):
        print("Yea it is")
