#! /bin/python3

# ================================================== #

# 1. Reverse a String
# word = 'Mamoun'
# print('Reversed: ', word[::-1])

# ================================================== #

# 2. Check if a String is a Palindrome 
# word = 'LOL'
# print(word == word[::-1])

# ================================================== #

# 3.Remove Duplicates from a String 
# word = 'test'
# print(''.join(set(word)))

# ================================================== #

# 4.Find the Longest Word in a String  
# word = 'Python is a great programming language'
# print(max(word.split(' '), key=len))

# ================================================== #

# 5.Find Common Elements Between Two Tuples
# tuple1 = (1, 2, 3)
# tuple2 = (2, 3, 4)
# print(tuple(set(tuple1).intersection(set(tuple2))))

# ================================================== #

# 6.Find the Maximum and Minimum Value in a Dictionary
# my_dict = {"a": 10, "b": 20, "c": 5}
# print("min: ", min(list(my_dict.values())), "max: ", max(list(my_dict.values())))

# ================================================== #

# 7.Merge Two Dictionaries
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# print(dict(list(dict1.items()) + list(dict2.items())))

# ================================================== #

# 8.Find Common Keys in Two Dictionaries
# dict1 = {"a": 1, "b": 2, "c": 3} 
# dict2 = {"b": 2, "c": 4, "d": 5} 
# print(set(dict1.keys()).intersection(set(dict2.keys())))

# ================================================== #

# 8.Find the longest ordered seq in string
# string = 'abdulrahman'
# longest = current = string[0]
# for index in range(1, len(string)):
#     if string[index] > string[index - 1]: current = current + string[index]
#     else: current = string[index]
#     if len(current) > len(longest): longest = current[::]

# print(longest)

# ================================================== #