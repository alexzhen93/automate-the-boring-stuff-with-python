#functions are defined using the def keyword, 
#followed by the function name and parentheses. 
# The code block within every function starts with a colon (:) and is indented.

def hello():
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there!")

hello()

#functions can take parameters, which are specified within the parentheses.
def hello(name): #name is a parameter that will be passed to the function
    print("Howdy " + name + "!")
    print("Howdy " + name + "!!!")
    print("Hello there " + name + "!")

hello("Alice") #Alice is passed as an argument to the function
hello("Bob")

#functions can return values using the return statement.
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"

r = random.randint(1, 9) #randomly generates a number between 1 and 9
fortune = getAnswer(r) #calls the getAnswer function with the random number as an argument
print(fortune) #prints the returned value from the getAnswer function

#Example of a function that does not return a value, but instead prints a message to the console.
spam = print("Hello!") #prints "Hello!" to the console

print(None == spam) #returns True, because the print function does not return a value, it returns None

#Keyword argument in functions allows you to specify the value of a parameter by name, 
#rather than by position. This can make your code more readable and easier to understand.
import random

random.randint(1, 10) #returns a random integer between 1 and 10

print("Hello", end=" ") #prints "Hello" without a newline at the end
print("World")

print("cats", "dogs", "mice", sep=", ") #prints "cats, dogs, mice" with a comma and space between each word

#The call stack is a data structure that keeps track of the function calls in a program.
#Example of call stack in action:
def a():
    print("a() starts")
    b()
    d()
    print("a() returns")

def b():
    print("b() starts")
    c()
    print("b() returns")

def c():
    print("c() starts")
    print("c() returns")

def d():
    print("d() starts")
    print("d() returns")

a() #calls the function a(), which in turn calls b() and d()

#local and global variables: 
# Local variables are defined within a function and can only be accessed within that function. 
# Global variables are defined outside of any function and can be accessed from anywhere in the program.


#global variables can be accessed from anywhere in the program, including within functions.
#local variables can be accessed only within the function in which they are defined.

def spam():
    eggs = 31337

spam()
#print(eggs) #this will raise an error because eggs is a local variable and cannot be accessed outside of the spam() function

#can't use variable defined in another function 

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam() #this will raise an error because eggs is a local variable in the spam() function and cannot be accessed in the bacon() function

#read global variable from local scope
#Example:
def spam():
    print(eggs)

eggs = 42
spam()
print(eggs)

#Example 2:
def spam():
    eggs = "spam local"
    print(eggs)         #prints "spam local"

def bacon():
    eggs = "bacon local"
    print(eggs)         #print "bacon local"    
    spam()
    print(eggs)         #print "bacon local"

eggs = "global" 
bacon()
print(eggs)             #print "global"

#Modify global variable inside of a function
def spam():
    global eggs
    eggs = "spam"

eggs = "global"
spam()
print(eggs)

#Example: local and global variable with same name 
def spam():
    print(eggs) #error if uncomment eggs = "spam local"
   # eggs = "spam local" 

eggs = "global"
spam()

#Exception handling: prevent from program to crash using try and

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument.")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def spam(divideBy):
    return 42 / divideBy
    
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
        print("Error: Invalid argument.")

#short program: ZigZag
# import time, sys
# indent = 0 # How many spaces to indent.
# indentIncreasing = True # Where the indentation is increasing or not.

# try:
#     while True: # The main program loop.
#         print(" " * indent, end="")
#         print("********")
#         time.sleep(0.1) # Pause for 1/10 of a second.

#         if indentIncreasing:
#             # Increase the number of spaces:
#             indent = indent + 1
#             if indent == 20:
#                 # Change direction:
#                 indentIncreasing = False

#         else:
#             # Decrease the number of spaces:
#             indent = indent - 1
#             if indent == 0:
#                 # Change direction:
#                 indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit()

#Practice questions:

# 1. Why are functions advantageous to have in your programs?
# Useful to execute code multiple time and advoide duplicated code and we can re use.

# 2. When does the code in a function execute: when the function is defined or when the function is called?
# the code on the function exceute when the function is call

# 3. What statement creates a function?
# def statement define the function and we need to make sure to call it to run the code

# 4. What is the difference between a function and a function call?
# function define what the function is about
# function call is exceute the fuction

# 5. How many global scopes are there in a Python program? How many local scopes?
# 1 global scope and we can access it anywhare in the program
# local scopes infinite whenever definding a new function there will be a local scope

# 6. What happens to variables in a local scope when the function call returns?
# after the function is call and local scope is used, they will be destroy and no longer accessibel 

# 7. What is a return value? Can a return value be part of an expression?
# A return value is whatever return from a function. Return value can be part of an expression

# 8. If a function does not have a return statement, what is the return value of a call to that function?
# it will return None (nothing)

# 9. How can you force a variable in a function to refer to the global variable?
# When we accessing we can directly use it. if we want to change it we have to use global infront of the variable

# 10. What is the data type of None?
# None is it own data type nothing nill or NULL

# 11. What does the import areallyourpetsnamederic statement do?
# import a module call areallyourpetsnamederic a python field that is being import and we can access any function that is in the module

# 12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?
#import spam
#spam.bacon()

#from spam import *
#bacon()

# 13. How can you prevent a program from crashing when it gets an error?
# we can use a try except block with error handling inside the except block

# 14. What goes in the try clause? What goes in the except clause?
#Try: put code we want to exceute inside the try block
#Except: error handling 

#Practice Project:

# The Collatz Sequence
# Write a function named collatz() that has one parameter named number. 
# If number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.

# Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. 
# (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, 
# you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)

# Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.

# Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.

# The output of this program could look something like this:

# Enter number:
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1

# Input Validation
# Add try and except statements to the previous project to detect whether the user types in a noninteger string. Normally, the int() function will raise a ValueError error if it is passed a noninteger string, as in int('puppy'). In the except clause, print a message to the user saying they must enter an integer.

def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result

print("Enter number:")

try:
    number = int(input())

    while number != 1:
        number = collatz(number)
except ValueError:
    print('Invalid input. You must enter an integet.')
    