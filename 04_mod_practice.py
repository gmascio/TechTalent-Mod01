#!/usr/bin/env python
# coding: utf-8

# Data Science Fundamentals: Python |
# [Table of Contents](../index.ipynb)
# - - - 
# <!--NAVIGATION-->
# Module 1. [Basic Python Syntax](./01_mod_python_syntax.ipynb) | [Variables and Objects](./02_python_variables_objects.ipynb) | [Operators](./03_python_operators.ipynb) | **[Exercises](./04_mod_practice.ipynb)**

# # Module 1: Practice Exercises
# Please remember to submit this file to Titus

# ### Exercise 1: Accept the user's first and last name and print them in reverse order with a space between them.

# In[1]:


first_name = input("Insert a first name")
last_name = input("insert a last name")

print(last_name, "", first_name)


# ### Exercise 2. Accept an integer (n) input from the user and compute the value of n+nn+nnn
# For example if `n=4` then `n + nn + nnn = 4 + 44 + 444 = 492`

# In[5]:


number = input("place number here")
number_integer = int(number)
total = number_integer + number_integer**2 + number_integer**3
print(total)


# ### Exercise 3. Ask the user "What country are you from?" then print the following statement: "I have heard that [input] is a beautiful country!"

# In[6]:


country = input("what country are you from")
print( "I have heard that " + country + " is a beautiful country")


# ### Exercise 4. What is the output of the following python code?

# In[1]:


x = 10
y = 50
if (x ** 2 > 100 and y < 100):
    print(x, y)


# Nothing

# ### Exercise 5: What is the output of the following addition `+` operator, and why does this code chunk execute this way??

# a = [10, 20]
# b = a
# b += [30, 40]
# print(a)
# print(b)

# a,b = [10,20,30,400]

# ### Exercise 6. What is the output of the following code, and what operator is being used here?

# print(2%6)

# The answer will be 2, because we are using a modulus operator to calculate the remainder of 2 when dividing by 6. But because that results in a decimal value, the remainder would just be 2 itself.

# ### Exercise 7: What is the output of the following code, and what arithmetic operators are used in this code?

# In[12]:


print(2 * 3 ** 3 * 4)


# 216 ; multiplication and exponentials are used 

# ### Exercise 8: What is a text editor?

# A text editor is an inteface that allows you to manipulate text and display in various formats

# ### Exercise 9: What is python?

# Python is a coding language used in many fields including: software development and data science

# ### Exercise 10: What is jupyter notebook, what type of python environment is it, and what alternatives are there to jupyter notebook?

# Jupyter notebook is an applicaton that allows the editing and hosting of python code that utilizes a conda environment. Alternatives to a jupyter notebook are VS Code, Eclipse and Kite 

# ### Please remember to submit this file to Titus!

# <!--NAVIGATION-->
# Module 1. [Basic Python Syntax](./01_mod_python_syntax.ipynb) | [Variables and Objects](./02_python_variables_objects.ipynb) | [Operators](./03_python_operators.ipynb) | **[Practice](./04_mod_practice.ipynb)**
# <br>
# [top](#)

# - - -
# 
# Copyright © 2020 Qualex Consulting Services Incorporated.
