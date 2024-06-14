# Extracting Sublist from a List of Temperatures
# Objective: Given a list of daily temperatures for a month, extract the temperatures for a specific week (e.g., week 2).
# temperatures = [22, 24, 20, 25, 23, 26, 24, 
# 25, 27, 29, 30, 28, 26, 27, 24, 23, 22, 21, 25, 24, 26
# , 27, 29, 28, 26, 25, 24, 23, 22, 21]
temp = [22, 24, 20, 25, 23, 26, 24, 25, 27,
        29, 30, 28, 26, 27, 24, 23, 22, 21, 25,
        24, 26, 27, 29, 28, 26, 25, 24, 23, 22, 21]
week_1 = temp[0:7]
week_2 = temp[7:14]
week_3 = temp[14:21]
week_4 = temp[21: 28]
print("Week 1 temperature is " + str(week_1))
print("Week 2 temperature is " + str(week_2))
print("Week 3 temperature is " + str(week_3))
print("Week 4 temperature is " + str(week_4))

"""
Extracting a Substring from a Sentence
Objective: Given a sentence, extract and print a specific word using string slicing.
sentence = "The quick brown fox jumps over the lazy dog"
extract third word "brow"
"""
sen = ["the quick brown fox jumped over the lazy dog"]
subtrct = "brow"
result = [s.replace(subtrct, "") for s in sen]
print(result)

# Write a Python program to check if a list is empty or not.
# 1. output the numbers from 1 to 10 using range function and for loop
# output should be like
# 1
# 2
# 3
# etc
# 2. output the numbers from 35 to 50 using range function and for loop
# output should be like
# 35
# 36
# 37
# etc
empty_list = []
non_empty_list = [1, 2, 3, 4]
print("the non empty list " + str(non_empty_list))
print("the empty list " + str(empty_list))
print("1 to 10 numbers")
for i in range(1, 10):
        print(i)
print("numbers 35 to 50")
for i in range(35, 50):
        print(i)
print("numbers negative -15 to -25")
for i in range(-15, -25):
        print(i)
print("numbers negative to positive -15 to 10")
for i in range(5, -10):
        print(i)
print("numbers 0 to 50 incremented by 3")
for i in range(3, 50, 3):
        print(i)

# 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop
# output format should be like
# 2 x 1 = 2
# 2 x 2 = 4
# etc
table = 2
for i in range(1 , 11):
        print(str(table) + " x " + str(i) + " = " + str(table * i))

# 7. Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]
# output should be 15
x = 0
l_3 = [3, 5, 2, 1, 4]
for i in l_3:
        x = x + i
        print(x)

# Count Even and Odd Numbers in a List
# Objective: Write a Python program that counts 
# the number of even and odd numbers in a given list.
numbers = [12, 7, 9, 24, 18, 5, 3, 20]
for i in numbers:
        if i % 2 == 0:
                print(str(i) + " is even")
        else:
                print(str(i) + " is odd")

# Print List Elements with Their Indices
# Objective: Write a Python program that prints
# each element of a list along with its index.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for i in range(len(fruits)):
        print(str(i) + " " + str(fruits[i]))

# Create a List of Even Numbers from 1 to 20
# Objective: Write a Python 
# program that creates a list of all even numbers from 1 to 20.
even = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_1 = []
for i in even:
        if i % 2 == 0:
                even_1.append(i)
print(even_1)
# Find the Length of Each String in a List
# Objective: Write a Python program that finds 
# and prints the length of each string in a given list.
strings = ["apple", "banana", "cherry", "date"]
for i in strings:
        print(str(i) + " is " + str(len(i)) + " characters long")
# Find Common Elements Between Two Lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3=(set(list1).intersection(list2))
print(list3)
# 8. Write a Python program to get the largest number
# from a list and use for loop consider the 
l_list = [3, 5, 2, 1, 4]
max_list = max(l_list)
print(max_list)
"""
Extracting a Sublist of Favorite Colors
Objective: Given a list of favorite colors, extract a sublist of the first three colors using list slicing.
favorite_colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
extract first three colors
"""
favorite_colors = ["red", "blue", "green", "yellow", "purple"]
first_three_colors = favorite_colors[0:3]
print(first_three_colors)
# Exercise 1: Sum of Elements in a List
# Objective: Write a Python program that 
# calculates the sum of all elements in a given list.
numbers = [10, 20, 30, 40, 50]
sum_of_elements = sum(numbers)
print(sum_of_elements)