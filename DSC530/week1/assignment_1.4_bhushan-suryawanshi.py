# -*- coding: utf-8 -*-
"""
Assignment 1.4 - Using Anaconda

File: assignment_1.4_bhushan-suryawanshi.py
Author: Bhushan Suryawanshi
Date:Monday, June 01, 2020
Course: DSC530-T301 Data Exploration and Analysis (2207-1)

Desc: This program will demonstrate -

1. Display the text “Hello World! I wonder why that is always the default 
                  coding text to start with”
2. Add two numbers together
3. Subtract a number from another number
4. Multiply two numbers
5. Divide between two numbers
6. Concatenate two strings together 
7. Create a list of 4 items 
8. Append an item to your list 
9. Create a tuple with 4 items 

"""

print(f'Hello World! I wonder why that is always the default coding text to start with')

a = 23
b = 56

print(f'Add two numbers : {a} + {b} = {a + b}')

print(f'Subtract two numbers : {b} - {a} = {b - a}')

print(f'Multiply two numbers : {a} * {b} = {a * b}')

print(f'Divide between two numbers : {b} / {a} = {b / a} \n \
      after rounding to two decimal : {round(b/a , 2)}')

str1 = "Exploratory"
str2 = "Analysis"

print(f'Concatenate two strings together : {str1}, {str2} = {str1 + str2}')

list_of_items = [a, b, str1, str2]
print(f'Type of variable "list_of_items" : {type(list_of_items)}')
print(f'Create a list of 4 items : {list_of_items}')

list_of_items.append("new item")
print(f'Append an item to your list : {list_of_items}')

tuple_of_four_items = (a, b, str1, str2)
print(f'Type of variable "tuple_of_four_items" : {type(tuple_of_four_items)}')
print(f'Create a tuple with 4 items : {tuple_of_four_items}') 

