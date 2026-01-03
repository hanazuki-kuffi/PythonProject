# This is my first Python code!!
# print("I like pizza!")
# print("It is really good!")


# Variable = A container for value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings
# first_name = "Kuffi"
# food = "Soup"
# email = "midorikuffi123@fake.com"

# print(f"Hello {first_name}!")
# print(f"You like {food}")
# print(f"Your email: {email}")


# Integers
# age = 21
# quantity = 4
# num_of_students = 16

# print(f"You are {age} years old!")
# print(f"You are buying {quantity} items!")
# print(f"Your class has {num_of_students} students")

# Float
# price = 10.99
# gpa = 3.1
# distance = 19.54

# print(f"The price is: ${price}")
# print(f"Your gpa is {gpa}")
# print(f"You walk {distance}km")

# Boolean

# is_student = False/True
# for_sale = False
# is_online = False

# if is_online:
#     print("You are online!")
# else:
#     print("You are offline")

# if for_sale:
#     print("That item is for sale")
# else:
#     print("That item is NOT available")


# if is_student:
#     print(f"You are student!")
# else:
#     print(f"You are NOT student!")
# print(f" Are you a student?: {is_student}")


# BRO COMMENT
# nickname = "Bro"
# year = 2025
# pi = 3.14
# is_admin = False

# print(f"Your nickname: {nickname}")
# print(f"It is {year} year")
# print(f"Pi has a value: {pi}")
# if is_admin:
#     print("He is the admin of this channel")
# else:
#     print("He is NOT admin of this channel")

#TYPECASTING

#typecasting = the process of converting a variable from one date type to another
#           srt(), int(), float(), boolean()

# name = ""
# age = 21
# gpa = 3.1
# is_student = False
# print(type(is_student))

# SOME EXAMPLES
# 1) gpa = int(gpa)
# print(gpa)           ((age += 1 =====  age = age + 1))---> does the same thing

# 2)age = float(age)
# print(age)

# 3) age = str(age)
# age += "1"
# print(age)
#print(type(age))

# 4)  name = bool(name)     "Kuffi code", "K" --- если написать тут любой хреновых значений то на оутпуте всегда выходит как TRUE даже если ты не пишеш ничего просто оставишь пробел все равно выходит одно и тоже. а если ты там тут буквально ниченго не напишеш то в итоге выхолит как FALSE вот пример ""
# print(name)


# INPUT = A function that promts the user to enter data
#      Returns the entered data as a string

# name = input("What is your name?: ")
# age = input("How old are you?: ")
# age = int(age)
# age += 1    # or: age = age + 1
#
# print(f"Hello, {name}!")
# print("HAPPY BIRTHDAY!!!")
# print(f"You are {age} years old")


#EXERCISE 1 RECTANGLE AREA CALC

# length = float(input("Enter the length: "))  # кароче тут такое дело без float на оутпуте не выходит ничего кроме ошибки там инпуте мы якобы пишим строка а не интеджер поэтому нам следует написать такие функций как это типо int(), float()

# width = float(input("Enter the width: "))
# area = length * width
#
# print(f"The area is: {area} cm²")