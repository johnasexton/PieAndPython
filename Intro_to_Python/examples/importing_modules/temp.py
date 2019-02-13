# -*- coding: utf-8 -*-

# this prints "hello class" to the screen
print('hello class')

# VARIABLES

# atomic types of variables are string, integers and booleans

# String
name = "John"

# Int
age = "51"

# boolean "True" and "False" are case sensitive and important for conditional logic
bool_true = True
bool_false = False 

# concatenate your variables into a larger string using String and Int types
print("My name is", name, "and I am", age, "years old")
print(bool_true, "or", bool_false)

# COLLECTIONS
# list positions start with "position-zero" so '1' = position-zero
# list is defined by the [] square brackets, not the name or the contents which can be anything
a_list = ['1', '2', '3'] 

# use your collection and print position-zero
print(a_list[0])

# now change the 1 to a 4
# lists can be modified
a_list[1] = '4'

# tuple is another kind of collection
# a tuple is defined by the () parenthesees not the name, or contents which can be anything
a_tuple = (1, 2, 3)
print(a_tuple[1])

# modifying a tuple will throw an error since tuples are immutable
# a_tuple[1] = 5 # commented out since it is immutable it errors

# DICTIONARY is another type of collection
# these are 'key: value' pairs so you query the key and get the value
# dictionary is defined by the {} curly braces not the variable name or the contents which can be anything
a_dict = {
        "one": 1,
        "two": '2',
        "three": 3
        }
print(a_dict["three"])

# LOOPS 
# perform an action on every item in a collection 
# 2 main types are: while & for...in
numbers = [1, 2, 3, 4, 5]
i = 0 # set your index value to position-zero
sum = 0 # set another variable called "sum" to 0
while i < len(numbers): # define while loop condition and terminate with a ":" colon     
    # it will result in a boolean True or False
    sum += numbers[i] # equivalent to sum = sum + <value from collection>
    i += 1
    # once the conditional while loop evaluates to a boolean True, it will loop
    # once the condition evaluates as a boolean False, it will EXIT the while loop
    # this will trigger the NEXT line of code that is OUTSIDE the while loop 
    # inside or outside of the loop is all controlled by indentation or not
    # indented is inside, and flush left is outside the structure
    print(sum)

# for...in loop is a different type of loop
for number in numbers:  # automatically starts at position-zero and puts it into the variable "number" 
    sum += number
    print(sum)

# LOGICAL BRANCHING

# IF Statements
age = 18
if age < 21:
    print('no booze for you')
if age > 21:
    print('have a drink on me')
    
age = 24
if age < 21:
    print('no booze for you')
if age > 21:
    print('have a drink on me')    

# IF THEN Statement
# you get a boolean True evaluation, it exits the loop and doesn't execute anything else
age = 21    
if age < 21:
    print('no booze for you')
elif age > 21: # it is "elif" in python NOT "elseif" like other languages
    print('have a drink on me')
else: # else is the "default case" when everything above fails to produce a boolean true
    print('Happy 21st!')

# FUNCTIONS
# begin with "def" for Define
# this is a function defined as "print_age"
def print_age(age):
    print("I am", age) 
    
# now use the print_age function
print_age(32)
print_age(332)
print_age(325)

def get_age(age):
    return "you are " + str(age) # the "+" operator on Strings will execute a concatenation 
print(get_age(32))

import matplotlib.pyplot as plt
# without the alias "plt" you would have to type out "matplotlib.pyplot"
# in order to plot you need x-axis values, and y-axis values
x_values = [1, 2, 3, 4, 5] # numbers
y_values = [1, 4, 9, 16, 25] # squares
plt.scatter(x_values, y_values)
plt.show

import matplotlib.pyplot as plt2
x_values = list(range(1, 101)) # numbers startng with 1 will end with 100
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values)
plt2.show

import matplotlib.pyplot as plt3
x_values = list(range(1, 101)) # numbers startng with 1 will end with 100
y_values = [x**2 for x in x_values]
plt.title("Squared Values", fontsize=24)
plt.xlabel("Number")
plt.ylabel("Squared") 
plt.scatter(x_values, y_values)
plt3.show

import matplotlib.pyplot as plt3
import json
x_values = []
y_values = []
with open('georgia_unemployment.json') as file:
    unemp_file = json.load(file) 
    for entry in unemp_file["data"]: 
        x_values.append(entry["month"])
        y_values.append(entry["rate"])
plt.title("Georgia Unemployment", fontsize=24)
plt.xlabel("Month")
plt.ylabel("Rate") 
plt.plot(x_values, y_values)
plt3.show