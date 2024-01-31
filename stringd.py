# str1="amritha"
# rev=str1[::-1]
# print(rev)
#
# str1="amrithoooolllla"
# dup=[]
# count=0
# for i in str1:
#     if str1.count(i)>1 and i not in dup:
#         dup.append(i)
#         count+=1
# print(dup)
# print(count)
#
# str1="amrtitha"
# rem=input("enter letter")
# indices=str1.index(rem)
# print(f"Index numbers of '{rem}' in the string: {indices}")
# str3=" "
# str3=str1[:indices]+str1[indices+1:]
# print(str3)
#
# 1Create a string made of the first, middle and last character
# str=input("Enter the string")
# str1=str[0]
# str2=str[-1]
# str3=str[int(len(str)/2)]
# print(str1,str3,str2)
#
# 2Create a string made of the middle three characters
# str=input("Enter the string")
# strn=(len(str)//2)
# str1=str[strn]
# str2=str[strn-1]
# str3=str[strn+1]
# print(str1,str2,str3)
#
# 3Append new string in the middle of a given string
# str=input("Enter the string")
# strn=(len(str)//2)
# strnew=input("Enter the new string")
# strp=str[:strn]
# strpn=str[strn:]
# str2=strp+strnew+strpn
# print(str2)
#
# 4Arrange string characters such that lowercase letters should come first
# str = input("Enter the string")
# str1=''
# for i in str:
# if i.islower():
# str1 += i
# print(str1)
#
# 5Count all letters, digits, and special symbols from a given string
# str = input("Enter the string")
# counta=0
# countd=0
# counts=0
# for i in str:
# if i.isalpha():
# counta +=1
# elif i.isdigit():
# countd +=1
# else:
# counts +=1
# print(counta,countd,counts)
#
# 6String characters balance Test
# str1 = input("Enter the string 1")
# str2 = input("Enter the string 2")
# for char in str1:
# if char in str2:
# continue
# else:
# print("Characters in str1 are not balanced in str2")
# break
# else:
# print("Characters in str1 are balanced in str2")
#
# 7Python Program to compare two lists
# str1 = input("Enter the string 1")
# str2 = input("Enter the string 2")
# if str1==str2:
# print("yes")
# else:
# print("no")
#
# 8convert int to string in Python
# n = input("enter the number")
# ntos=str(n)
# print(type(n))
#
# 9Program to Remove Punctuation From a String
# str1 = input("Enter the string")
# result_str = ''
# for i in str1:
# if i.isalnum():
# result_str += i
# else:
# continue
# print(result_str)
#
# 10Removal all characters from a string except integers
# #str1 = input("Enter the string")
# intstr=''
# for i in str1:
# if i.isdigit():
# intstr += i
# print(intstr)
#
# 11Find the last position of a given substring
# str1 = input("Enter the string 1")
# str2 = input("Enter the substring")0
# last_position = str1.rfind(str2)
# print("Last occurrence starts at index:", last_position)
#
# 11Calculate the sum and average of the digits present in a string
# str1 = input("Enter the string ")
# intstr = ''
# total =0
# for i in str1:
# if i.isdigit():
# intstr += i
# print(intstr)
# avg=len(intstr)
# for i in intstr:
# total += int(i)
# print(total)
# print(total/avg)
#
# char_list = list("Python")
# print(char_list)
# How do you print duplicate characters from a string? (solution)
#
# Python program to check whether the string is Symmetrical or Palindrome
# str1="malayalam"
# str2=str1[::-1]
# print(str2)
# Ways to remove i’th character from string in Python
#
# Initializing String
# test_str = "amrithas"
#
# Removing char at pos 3
# using slice + concatenation
# new_str = test_str[:2] + test_str[3:]
#
# Printing string after removal
# removes ele. at 3rd index
# print("The string after removal of i'th character : " + new_str)
# Find length of a string in python (4 ways)
# str1="dog"
# count=0
# for i in str1:
# count+=1
# print(count)
# Python – Avoid Spaces in string length
# Python program to print even length words in a string
# str1 = "This is a python language"
# s = str1.split(" ")
# print(s)
# swr = " "
# for i in s:
#     leng = len(i)
#     if leng % 2 == 0:
#         swr += i
#         print(i)
# Python – Uppercase Half String
# str1="hello"
# strl=len(str1)//2
# print(strl)
# print(str1[strl])
# str2=""
# str2=str1[:strl]+(str1[strl:]).upper()
# print(str2)
# Python program to capitalize the first and last character of each word in a string
# str1="hello"
# str2=""
# str2=str1[0:-1].capitalize()+str1[-1].capitalize()
# print(str2)
# Python program to check if a string has at least one letter and one number
# str1="hewqw1234llo"
# num=""
# char=" "
# for i in str1:
#     if i.isdigit():
#         num+=i
#     elif i.isalpha():
#         char+=i
# print(char)
# print(len(char))
# print(num)
# print(len(num))
# Maximum frequency character in String
# duplicates = []
# input_str = "amritawwha"
# count = 0
#
# for char in input_str:
#     if input_str.count(char) > 1 and char not in duplicates:
#         duplicates.append(char)
#         count += 1
#
# print("Duplicates in the string:", duplicates)
# print("Number of duplicates:", count)
# duplicates
# str1="amritha"
# duplicates=" "
# for i in str1:
#     if str1.count(i)>1 and i not in duplicates:
#         str1[i]=duplicates
#         print(duplicates)
#
#
# str1="amWEDFfs Dritha dfvg efg def"
# counter=0
# for i in str1:
#     if i.isspace():
#         counter+=1
# print(counter)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
