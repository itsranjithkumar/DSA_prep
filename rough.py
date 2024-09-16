# def romanNumbers(s):

#     roman_values = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#     total = 0 
#     prev_values = 0
#     for char in s:
#         values = roman_values[char]
#         if values > prev_values:
#             total += values -2 * prev_values
#         else:
#             total += values
#             prev_values = values

#     return total

# print (romanNumbers("III"))


# code explanation:

# total += values -2 * prev_values

# first  2 multiples the prev_values and we need to subtract the values


"""-------------------------------------------------------------------------------------------------"""
# write a python program to check if a string is a palindrome ?


'''def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

 # Test the function
S = "racecar"
if is_palindrome(S):
    print(f"{S} is a palindrome")
else:
    print(f"{S} is not a palindrome")'''

'''------------------------------------------------------------------------------------------------------------'''
# write a python program to find the factorial of a number ?

'''def factorial (number):
    if number == 0:
        return 1
    else:
        return number  * factorial(number - 1)

# Two methods of factorial answers


print (factorial(5))

number =5
result = factorial(number)
print(f'the factorial {number} is {result}')'''



'''-------------------------------------------------------------------------------------------------------------------'''
# Write a python progream to find the largest element in a list ?

# def find_largest(numbers):
#     largest = numbers[0]
#     for num in numbers:
#         if num > largest:
#             largest = num
#     return largest

# # Test the function
# nums = [10, 5, 8, 20, 3]
# largest_num = find_largest(nums)
# print(f"The largest number is {largest_num}")

'''----------------------------------------------------------------------------'''

# Write  a python program to reverse a string ?


# def reverse_string(string):
#     return string[::-1]

# text = "Ronaldo"

# reverse_text = reverse_string(text)

# print(reverse_text)


'''-------------------------------------------------------------------------------------------------------------'''
# Write a Python program to count the frequency of each element in a list.

# def count_frequency (number):
#     frequency = {}
#     for num in number:
#         if num in frequency: 
#             frequency[num] += 1
#         else:
#             frequency [num] = 1

#     return frequency

# int = [1,2,2,3,4,5,5,6]
# frequency_count = count_frequency(int)
# print(count_frequency(int))
# print (frequency_count)


'''----------------------------------------------------------------------------------------------------------'''
# Write a Python program to check if a number is prime number ?

# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# # Test the function
# num = 17
# if is_prime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")


'''---------------------------------------------------------------------------------------------------------------------'''

# list1 = [1,2,3,4,5]
# list2 = [6,2,8,9,1]


# common_element = []

# for i in list1:
#     if i in list2:
#         common_element.append(i)

# print(common_element)

'''-------------------------------------------------------------------------------------------------------------------'''

# Write a Python program to remove duplicates from a list.

# def remove_duplicate(numbers):
#    unique_numbers=[] 

#    for num in numbers:
#       if num not in unique_numbers:
#          unique_numbers.append(num)
#    return unique_numbers
   
# nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]

# unique_nums = remove_duplicate(nums)
# print(unique_nums)

'''----------------------------------------------------------------------------------------------------------------------------'''

# a_list = ['data', 'camp' , 'tutorial']

# a_list.append('python')

# print(a_list)

'--------------------------------------------------------------------------------------------------------------------------'

# Tuple
# Immutable: Once a tuple is created, its elements cannot be changed (no adding, removing, or modifying elements).

# if we need to add list in tuple

# Example:

# a_tuple = ('data', 'camp', 'tutorial')

# To "add" an element, create a new tuple
# a_tuple = a_tuple + ('python',)

# print(a_tuple)





# find missing array ?

# def find_missing(input_list):

#   sum_of_elements = sum(input_list)
 
#    There is exactly 1 number missing
#   n = len(input_list) + 1
#   actual_sum = (n * ( n + 1 ) ) / 2
 
#   return int(actual_sum - sum_of_elements)
# list_1 = [1,5,6,3,4]


# find_missing(list_1)
# 2


'---------------------------------------------------------------------------------------------------------------------------------'

# text = 'ranjith'

# uppercase_text = text.upper()

# lowercase_text = text.lower()


# print(f"Uppercase: {uppercase_text}")

# print(f"Lowercase: {lowercase_text}")


'----------------------------------------------------------------------------------------------------------------------------------'
# Write a Python program to find the sum and average of elements in a list.


# numbers = [1, 2, 3, 4, 5]



# total_sum = sum(numbers)

# average = total_sum / len(numbers)


# print(average)

'------------------------------------------------------------------------------------------------------------------------------------'
# Write a Python program to check if a string contains a specific substring


# text = "this is string"
# substr = "is"
# if substr in text:
#   print(f'the string{substr} is present in the {text}')

# else:
#   print(f'the string{substr} is not present in the {text}')


'-----------------------------------------------------------------------------'

# Create a dictionary from a list of key-value pairs:

# key_value_pairs = [("name", "Alice"), ("age", 30), ("city", "New York")]



# my_dict = dict(key_value_pairs)


# print(f"Dictionary: {my_dict}")


"----------------------------------------------------------------------------------------------------------------"

#  How can you handle exceptions in Python?

# try:
#     e = 10 
# except Exception as e:
#     print("Error:", e)
# else:
#     print("No errors occurred")
# finally:
#     print("This runs no matter what")

'-------------------------------------------------------------------------------------------------------------------'
# What is a lambda function in Python? Provide an example.

# add = lambda x,y: x+y 

# print(add(5,5))

'---------------------------------------------------------------------------------------------------------------------'
# Explain list comprehension and give an example.

# L = [x*3 for x in range (10)]

# print(L)


'-------------------------------------------------------------------------------------------------------------------'
# How do you merge two dictionaries in Python?

# dic1 = {'a':1, 'b':2, 'c':3}
# dic2 = {'d':4, 'e':5, 'f':6}

# dic1.update (dic2)

# print(dic1)

'--------------------------------------------------------------------------------------------'
# How can you create a dictionary from two lists in Python?

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# my_dict = dict(zip(keys, values))
# print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

'--------------------------------------------------------------------------------------------'

# Explain the difference between continue, break, and pass in Python loops.

# for i in range (10):
#     if i == 3:
#         continue
#     if i == 8:
#         break 
#     print (i)

'-----------------------------------------------------------------------------------------------'

# What are lists and tuples? What is the key difference between the two?

# my_tuple = ('sara', 6, 5, 0.97)
# my_list = ['sara', 6, 5, 0.97]


# my_list [0]='Ranjith'

# print(my_list[0])


# my_tuple [0]='Ranjith'

# print(my_tuple[0])

# In list we can change the strint or number

# but in tuple we can't change the strint or number


'-----------------------------------------------------------------------------------------------'
# What is __init__? 

# class developers:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

# E1 = developers('Ranjith', 21, 25000)

# print(E1.name)
# print(E1.age)
# print(E1.salary)


# Reverse the order of a list

# x = ['Ranjith', 'Kumar', 'gokul', 'Rajesh']

# R = x[::-1]

# print(R)



# What are docstrings in Python?

# x = 10
# y = 2
# z = x/y

# print(z)



# Why do we use join() function in Python?

# x = 'rohan'

# y = 'ab'

# y = x.join(y)

# print(y)


# Explain the concept of conditional statements in Python.

# age = 20
# if age >= 18:
#     print('you are an adult')
# else:
#     print('you are not an adult')

'-------------------------------------------------------------------------------------------------'
# Converting an Integer into Decimals

# import decimal
# integer = 10

# print(decimal.Decimal(integer))
# print(type(decimal.Decimal(integer)))

# output :
# 10
# <class 'decimal.Decimal'>

'------------------------------------------------------------------------------------------------'
# Counting Vowels in a Given Word

# vowel = ['a', 'e', 'i', 'o', 'u']

# word = 'programming'
# count = 0

# for i in word:
#     if i  in vowel:
#         count += 1
# print(count)

'-----------------------------------------------------------------------------------------------'

# string = 'Ranjithh'

# word = 'h'
# count = 0

# for i in string:
#     if i in word:
#         count += 1  

# print(count)


'-----------------------------------------------------------------------------------------------'
# Finding the Maximum Number in a List

# number = [10,20,30,40]

# max_number = number[0]

# for num in number:

#     if max_number < num:
#         max_number = num
# print (max_number)

'--------------------------------------------------------------------------------'
# Finding the Middle Element in a List


# number = [1,2,3,4,5,6,7,8,9,10]

# middle_element = int(len(number) / 2)


# print(number[middle_element])



'---------------------------------------------------------------------------------'

# Converting a List into a String

# list = 'r', 'a', 'n', 'j', 'i', 't', 'h'

# string = ''.join(list)

# print(string)
# print(type(string))

# output:
# ranjit
# <class 'str'>

'-----------------------------------------------------------------------------------------'

# list1 = [1,2,3,4,5]
# list2 = [6,2,8,9,1]


# common_element = []

# for i in list1:
#     if i in list2:
#         common_element.append(i)

# print(common_element)





# for i in range(1,11):
#     if 1 % 2 == 0:
#         continue
#     if i == 7:
#         break

# print(i)

# --------------------------------------------------------------------------------------------

# - workout

# Finding the Maximum Number in a List

# number = [10,20,30,40]

# max_number = number[0]

# for num in number:
#     max_number < num
#     max_number = num

# print(max_number)



# reverse string

# x = 'ranjith'

# reverse_string = x[::-1]

# print(reverse_string)

'--------------------------------------------------------------------------------------------------------'
# Orginal String is  PYnative
# Printing only even index chars
# P
# n
# t
# v


# x = 'PYnative'

# for i in range (0,len(x),2):
#     print(x[i])

'--------------------------------------------------------------------------------------------------------'
# remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
# remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string
# code in python



# x = 'PYnative'

# r = x[4::]

# s = x[2::]

# print (s)


'------------------------------------------------------------------------------------------------------------------'

# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False


# x = [10, 20, 30, 40, 10]
# y = [75, 65, 35, 75, 30]

# def same_number(y):
#     return y[0] == y[-1]
# print (same_number(y))

# output : False

'----------------------------------------------------------------------'
# Test


# for i in x:
#     if i%2!=0:
#      print(i)

# for i in range(21,30,2):
#         print(i)


# for i in range(20,32,2):
#         print(i)


# def palindrom(string):
        
#         return string == string[::-1]
# S = 'amma'

# print(palindrom(S))


# s = 'Ranjith' 
# print(s.count('i'))