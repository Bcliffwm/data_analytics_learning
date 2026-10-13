my_string = 'Adam is learning Python'

# Examples of using the Python string methods to modify contents of a string
print('Original String:', my_string)
print()
print(my_string.lower()) # shows lower case of all letters in the string
print(my_string.upper()) # shows upper case of all letters in the string
print(my_string.title()) # shows capitalization of each word in the string

# Examples of using Python string methods to find specific content of a string
print('Original String:', my_string)
print()

print(my_string.find('Adam')) # finds the first index of a specified word or substring in a given string
print(my_string.find('Bishop')) # if word or substring is not in the given string, then -1 is returned


print(my_string.rfind('Adam')) # finds the starting position of the last occurrence of a specified word or substring in a given string
print('How much wood would a woodchuck chuck if a woodchuck could chuck wood'.rfind('wood'))

print(my_string.index('Adam'))

# Examples of using Python string methods to see if it meets conditions
print('Original String:', my_string)
print()

print(my_string.isalpha()) # Returns True if each char of string is alphanumeric
print(my_string.replace(' ', '').isalpha())

print(my_string.isalnum()) # Returns True if each char of string is a letter
print(my_string.isdecimal()) # Returns True if each char of string is a number
print(my_string.isascii()) # Returns True if each char of string is in the ascii format
print(my_string.isupper()) # Returns True if each char of string is in uppercase

# Examples of using Python string methods to manipulate strings
print('Original String:', my_string)
print()

print(my_string.replace('Adam', 'Bishop')) # Finds an old piece of the str and replaces it with a new string
print(my_string.splitlines()) # Converts each string element into a list delimited by a space
print(my_string.encode()) # Encodes the string data into a desired encoding -> By default, UTF-8 is used
print(my_string.strip())

# Examples of Python string methods and other functions to discover more about strings
print('Original String:', my_string)
print()

print(len(my_string)) # Returns the total number of chars used to build the string -- Keep in mind spaces are also considered as chars
print(my_string, 'and Ben is teaching him.') # prints a concatenation of my_string and new text
print(my_string + ' and Ben is teaching him.')

# String formatting with f-Strings
fruit = 'pineapple'
tester_string = f'Original:\nWhat I would give for a {fruit}'
print(tester_string)

print()
tester_string = f'What I would give for a {fruit.upper()}'
print(tester_string)

tester_string = f'What I would give for a {fruit.capitalize()}'
print(tester_string)

tester_string = f'What I would give for a {fruit[4:]}'
print(tester_string)

# manipulating f-string with more code
vowels = ['a', 'e','i','o','u', 'A', 'E','I','O','U'] # list of words

fruit = 'cherry' # assigning string value to my variable
fruit = ''.join([letter if letter not in vowels else letter.capitalize() for letter in fruit]) # code to check each letter of fruit values

tester_string = f'What I would give for an {fruit}' if fruit[0] in vowels else f'What I would give for a {fruit}' # conditional assignment of string variable
print(tester_string)