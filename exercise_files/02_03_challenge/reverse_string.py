"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.

# Adding all chars separately into Stack
for char in string:
    s.push(char)

# Popping the chars one by one with pop() and build reversed_string
while not s.is_empty():
    reversed_string += s.pop()

print(reversed_string)
