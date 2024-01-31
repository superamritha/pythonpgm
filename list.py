# Reverse a list in Python
# lst1 = [100,200,300]
# lst1.reverse()
# print(lst1)
# Concatenate two lists index-wise
# lst1 = ['d','dd', 'edc']
# lst2 = ['ab', 'c', 'de']
# lst3 = lst1 + lst2
# print(lst3)
# square of numbers
# lst1=[1,2,3,4]
# res=[]
# for i in lst1:
# res.append(i*i)
# print(res)
# Program to check if the Given List is in Ascending Order or Not
# number_list = []
# n = int(input("Enter the list size "))
# print("\n")
# for i in range(0, n):
# print("Enter number at index", i, )
# item = int(input())
# number_list.append(item)
# print("User list is ", number_list)
# temp_list = number_list[:]
# number_list.sort()
# if temp_list == number_list:
# print("Given List is in Ascending Order")
# else:
# print("Given List is not in Ascending Order")
# print(number_list)

# Program to Find Even Numbers From a List
# n = int(input("Enter number of items in the list"))
# nlist = []
# print("\n")
# for i in range(0, n):
# print("enter the number at index", i)
# items = int(input())
# nlist.append(items)
# for i in nlist:
# if i % 2 == 0:
# print("even")
# else:
# print("odd")

# Program to Merge Two Lists
# listbn1 = []
# n1 = int(input("Enter the number for first list"))
# print("\n")
# for i in range(0, n1):
# print("Enter number at index", i)
# items = int(input())
# listbn1.append(items)
# listbn2=[]
# n2=int(input("enter the numbers of second list"))
# print("\n")
# for i in range(0, n2):
# print("Enter number at index", i)
# items = int(input())
# listbn2.append(items)
# listbn1.extend(listbn2)
# print(listbn1)

# Write a Python program to sum all the items in a list
# listbn1 = []
# sum=0
# n1 = int(input("Enter the number for first list"))
# print("\n")
# for i in range(0, n1):
# print("Enter number at index", i)
# items = int(input())
# listbn1.append(items)
# for i in listbn1:
# sum += i
# print(sum)

# Write a Python program to multiply all the items in a list
# listbn1 = []
# mul = 1
# n1 = int(input("Enter the number for first list"))
# print("\n")
# for i in range(0, n1):
# print("Enter number at index", i)
# items = int(input())
# listbn1.append(items)
# for i in listbn1:
# mul *= i
# print(mul)

# Write a Python program to get the largest number from a list.
# listbn1 = []
# n1 = int(input("Enter the number for first list"))
# print("\n")
# for i in range(0, n1):
# print("Enter number at index", i)
# items = int(input())
# listbn1.append(items)
# large = listbn1[0]
# for i in listbn1:
# if i > large:
# large = i
# print(large)

# Write a Python program to get the smallest number from a list
# listbn1 = []
# n1 = int(input("Enter the number for first list"))
# print(n1)
# for i in range(0, n1):
# print("Enter number at index", i)
# items = int(input())
# listbn1.append(items)
# print(listbn1)
# large = listbn1[0]
# for i in listbn1:
# if i < large:
# large = i
# print(large)
# How to iterate over 2+ lists at the same time
# l1=[1,2,3,4]
# l2=['baby','kakai','docu']
# z=zip(l1,l2)
# for l1,l2 in z:
# print(l1, l2)
# Python program to interchange first and last elements in a list
# list1=[]
# n=int(input("Enter number of elements in the list"))
# print("\n")
# for i in range(0,n):
# print("Enter the numbers")
# I=int(input())
# list1.append(I)
# print(list1)
# list1[0], list1[-1] = list1[-1], list1[0]
# print(list1)
# Python program to interchange first and last elements in a list tell position
# list1=[]
# n=int(input("Enter number of elements in the list"))
# print("\n")
# p=int(input("Enter position"))
# print("\n")
# for i in range(0,n):
# print("Enter the numbers")
# I=int(input())
# list1.append(I)
# print(list1)
# list1[1], list1[p-2] = list1[p-2], list1[1]
# print(list1)
# Write a Python program to remove duplicates from a list
# list1=[]
# n=int(input("Enter number of elements in the list"))
# print("\n")
# for i in range(0,n):
# print("Enter the numbers")
# I=int(input())
# list1.append(I)
# newlist=[]
# for item in list1:
# if item not in newlist:
# newlist.append(item)
# print("List after removing duplicates:", newlist)

# Write a Python program to check if a list is empty or not
# list1=[]
# n=int(input("Enter number of elements in the list"))
# print("\n")
# for i in range(0,n):
# print("Enter the numbers")
# I=int(input())
# list1.append(I)
# print(list1)
# if I in list1:
# print("Present")
# else:
# print("No")

# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# list1 = []
# p = int(input("Enter position you want to remove"))
# print("\n")
# n = int(input("Enter number of elements in the list"))
# print("\n")
# for i in range(0, n):
# print("Enter the numbers")
# I = int(input())
# list1.append(I)
# print(list1)
# list1.pop(p)
# print(list1)
# Write a Python program to access the index of a list
# list1=[]
# n=int(input("Enter number of elements in the list"))
# print("\n")
# for i in range(0,n):
# print("Enter the numbers")
# I=int(input())
# list1.append(I)
# print(list1)
# list1[0], list1[-1] = list1[-1], list1[0]
# print(list1)
# for index, element in enumerate(list1):
# print(f"Index: {index}, Element: {element}")
# Write a Python program to convert a list of characters into a string
# Define a list 's' containing individual characters
# s = ['a', 'b', 'c', 'd']

# Use the 'join' method to concatenate the characters in the list 's' into a single string
# str1 = ''.join(s)

# Print the concatenated string 'str1'
# print(str1)
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# input_string = input("Enter a list of strings separated by spaces: ")
# list_of_strings = input_string.split(',')
# print(list_of_strings)
# large = list_of_strings[0]
# print(type(list_of_strings))
# for i in list_of_strings:
# if len(i) > len(large):
# large = i
# print(large)
# input_string = input("Enter a string: ")
# list_of_characters = list(input_string)

# print("List of characters:", list_of_characters)
#
# input_string = input("Enter a comma-separated string: ")
# list_of_values = input_string.split(',')

# print("List of values:", list_of_values)
# list_of_characters = ['h', 'e', 'l', 'l', 'o']
# resulting_string = ''.join(list_of_characters)

# print("Resulting string:", resulting_string)

# my_list = []  # This is an empty list

# if not my_list:
# print("The list is empty.")
# else:
# print("The list is not empty.")
# str1="amritha"
# duplicates=[]
# for i in str1:
#     if str1.count(i)>1 and i not in duplicates:
#         duplicates.append(i)
#         print(duplicates)


# list1 = []
# n = int(input("Enter number of elements in the list"))
# print("\n")
# for i in range(0, n):
#     print("Enter the numbers")
#     I = int(input())
#     list1.append(I)
# newlist = []
# for item in list1:
#     if list1.count(item) > 1 and item not in newlist:
#         newlist.append(item)
#         print("List after removing duplicates:", newlist)

# n = int(input("Enter the number of elements"))
# mylist = []
# for i in range(0, n):
#     print("Enter the numbers")
#     I = int(input())
#     mylist.append(I)
# print(mylist)
# counter = 0
# for i in set(mylist):
#     print(i,mylist.count(i))

# n = int(input("Enter the number of elements"))
# mylist = []
# for i in range(0, n):
#     print("Enter the numbers")
#     I = int(input())
#     mylist.append(I)
# print(mylist)
# n2 = int(input("Enter the number of elements"))
# mylist2 = []
# itemsl=[]
# for i in range(0, n):
#     print("Enter the numbers")
#     I = int(input())
#     mylist2.append(I)
# print(mylist2)
# for item in mylist:
#     if item in mylist2:
#         print("match", item)
#         itemsl.append(item)
# print(itemsl)