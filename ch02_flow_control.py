# Flow Control Statements
#Boolean Expressions: True or False
#Comparison Operators: ==, !=, >, <, >=, <=
spam = True
print(spam)
print(42 == 42)
print("Dog" == "Cat")
print("Dog" != "Cat")
print(42 > 41)
print(42 < 41)
print(42 >= 42)
print(42 <= 42) 

#Example of Boolean Expressions AND Operator *Both need to be True*
#True and True = True
#True and False = False
#False and True = False
#False and False = False

print(True and True)
print(True and False)
print(False and True)
print(False and False)

#Example of Boolean Expressions OR Operator *Only one needs to be True*
#True or True = True
#True or False = True
#False or True = True
#False or False = False

print(True or True)
print(True or False)
print(False or True)
print(False or False)

#Example of Boolean Expressions NOT Operator *Reverses the value*
#not True = False
#not False = True   

print(not True)
print(not False)

#Example of Boolean Expressions with Variables
spam = 10
print(spam > 5 and spam < 15)  
print(spam > 5 and spam > 15)
print(spam > 5 or spam < 15) 
print(spam < 5 or spam > 15)
print(not spam > 5)
print(not spam < 5)
print(2 + 2 == 4 and 2 + 2 == 5)
print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2) 
# *** Not first then and then or***

#Example of Boolean Expressions with Variables and Comparison Operators
name = "Alex"
password = "password123"
if name == "Alex":
    print("Hello, Alex!")
    if password == "password123":
        print("Access granted.")
    else:
        print("Access denied. Incorrect password.")

#Example 2:
name = "Carlos"
age = 3000
if name == "Alice":
    print("Hi, Alice!")
elif age < 12:
    print("You are not Alice, kiddo.")
else:
    print("You are neither Alice nor a little kid.")

#Example of While Loop
spam = 0
while spam < 5:
    print("Hello, world.")
    spam = spam + 1

#Example of While Loop with Statement
name = ""
while name != "your name":
    print("Please type your name.")
    name = input()
print("Thank you!")

#Example of While Loop with Break Statement 
while True:
    print("Please type your name.")
    name = input()
    if name == "your name":
        break
print("Thank you!")

#Example of While Loop with Continue Statement
while True:
    print("Who are you?")
    name = input()
    if name != "Joe":
        continue
    print("Hello, Joe. What is the password? (It is a fish.)")
    password = input()
    if password == "swordfish":
        break  
    
print("Access granted")

#Example of while Loop with condition of other data type with True or False
name = ""
while not name:
    print("Enter your name:")
    name = input()
print("How many guests will you have?")
numOfGuests = int(input())
if numOfGuests:
    print("Be sure to have enough room for all your guests.")
    print("Done")

#Example of For Loop
print("My name is")
for i in range(5):
    print("Jimmy Five Times (" + str(i) + ")")

#Example of For Loop 2:
total = 0
for num in range(101):
    total = total + num
    print(total)

#Example of For Loop using while Loop:
print("My name is")
i = 0
while i < 5:
    print("Jimmy Five Times (" + str(i) + ")")
    i = i + 1

#range() function can take 1, 2, or 3 arguments. If it takes 1 argument, 
# it will generate numbers from 0 to that number - 1. If it takes 2 arguments, 
# it will generate numbers from the first argument to the second argument - 1. 
# If it takes 3 arguments, it will generate numbers from the first argument to the second argument - 1,
# incrementing by the third argument.
#Example of For Loop using range() function with 1 argument:
for i in range(5):
    print(i)

#Example of For Loop using range() function with 2 arguments:
for i in range(5, 10):
    print(i)

#Example of For Loop using range() function with 3 arguments:
for i in range(0, 10, 2):
    print(i)

#Example of For Loop using range() function with 3 arguments and negative step:
for i in range(10, 0, -1):
    print(i)

#Importing modules
import random
for i in range(5):
    print(random.randint(1, 10))  # Prints a random integer between 1 and 10 (inclusive)

#Importing modules using from keyword
from random import randint
for i in range(5):
    print(randint(1, 10))  # Prints a random integer between 1 and 10 (inclusive)

#Import system module and use sys.exit() to exit the program
import sys
while True:
    print("Type 'exit' to exit.")
    response = input()
    if response == "exit":
        sys.exit()
    print("You typed " + response + ".")


#Example with import random Guessing Game
import random
secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break  # This condition is the correct guess!

if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))

#example with import random and sys on Rock, Paper, Scissors Game
import random, sys

print("ROCK, PAPER, SCISSORS")

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True:  # The player input loop.
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break  # Break out of the player input loop.
        print("Type one of r, p, s, or q.")

    # Display what the player chose:
    if playerMove == 'r':
        print("ROCK versus...")
    elif playerMove == 'p':
        print("PAPER versus...")
    elif playerMove == 's':
        print("SCISSORS versus...") 

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print("ROCK")
    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        computerMove = 's'
        print("SCISSORS")

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print("You win!")
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print("You win!")
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print("You win!")
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print("You lose!")
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print("You lose!")
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print("You lose!")
        losses = losses + 1 
#Practice:
#1 What are the two Boolean values? True and False
#2 What are the three Boolean operators? and, or, not
#3 Write out the truth tables for the Boolean operators.

# Truth table for AND operator: *Both must be True*
# A     B     A and B
# True  True  True
# True  False False
# False True  False
# False False False

# Truth table for OR operator: *At least one must be True*
# A     B     A or B
# True  True  True
# True  False True
# False True  True
# False False False

# Truth table for NOT operator: *Inverts the Boolean value*
# A     not A
# True  False
# False True

#4 What do the following expressions evaluate to?
# 5 > 3 and 2 < 4 evaluates to True
# not (5 > 4) evaluates to False
# (5 > 4) or (3 < 2) evaluates to True
# not ((5 > 4) or (3 < 2)) evaluates to False
# (True and True) and (True == False) evaluates to False
# (not False) or (not True) evaluates to True

#5 What are the six comparison operators?
#  ==, !=, >, <, >=, <=

#6 What is the difference between the = and == operators?
# The = operator is used for assignment, while the == operator is used for comparison.

#7 Explain what a condition is and where you would use one.
# A condition is a statement that evaluates to either True or False. 
# Conditions are used in control flow statements, 
# such as if statements and loops, to determine the flow of execution based on certain criteria.

#8 Identify the three blocks in this code:
spam = 0
if spam == 10:
    print("eggs")
    if spam > 5:
        print("bacon")
    else:
        print("ham")
    print("spam")
print("spam")

# The three blocks in the code are:
# 1. The first block is the if statement that checks if spam == 10.
# 2. The second block is the nested if statement that checks if spam > 5.
# 3. The third block is the else statement that executes if spam <= 5.

#9 Write code that prints Hello if 1 is stored in spam, 
# prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam = int(input("Enter a number: "))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")

#10 What keys can you press to force a program to quit if it has an infinite loop?
# You can press Ctrl + C to force a program to quit if it has an infinite loop

#11 What is the difference between break and continue?
# The *break* statement is used to exit a loop prematurely,
# while the *continue* statement is used to skip the rest of 
# the code inside a loop for the current iteration and move on to the next iteration.

#12 Write the difference between range(10), range(0, 10), and range(0, 10, 1).
# range(10) generates numbers from 0 to 9 (10 is exclusive).
# range(0, 10) generates numbers from 0 to 9 (10 is exclusive).
# range(0, 10, 1) generates numbers from 0 to 9 (10 is exclusive) with a step of 1. 
# All three are equivalent in this case.

#13 Write a short program that prints the numbers 1 to 10 using a for loop.
#then write an equivalent program that prints the numbers 1 to 10 using a while loop.
for i in range(1, 11):
    print(i)

while i <= 10:
    print(i)
    i += 1

#14 If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# You would call it using the syntax: spam.bacon()

#Extra Credit:
#Look up the round() and abs() functions on the internet, and find out what they do.
#Experiment with them.

#round() function rounds a number to the nearest integer or to a specified number of decimal places.
print(round(3.14159))  # Output: 3

#abs() function returns the absolute value of a number, which is the non-negative value of that number.
print(abs(-5))  # Output: 5

