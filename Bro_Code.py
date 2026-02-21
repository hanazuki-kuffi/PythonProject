# This is my first Python code!!
# print("I like pizza!")
# print("It is really good!")
from math import remainder
# from pickle import format_version

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

# EXERCISE 2 SHOPPING CART PROGRAM
# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity
#
# print(f"You have bought {quantity} x {item}/s")
# print(f"your total is: ${total}")
# print(total)


#Madlibs game
#Word game where you create a story
#By filling in blanks with random words

# adjective1 = input("Enter an adjective (description): ")
# noun1 = input("Enter a noun (person, place, thing): ")
# adjective2 = input("Enter an adjective (description): ")
# verb1 = input("Enter a verb ending with 'ing' ")
# adjective3 = input("Enter an adjective (description): ")
#
# print(f"Today I went to a {adjective1} zoo. ")
# print(f"In an exhibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}")

#ARITHMETIC OPERATORS & MATH FUNCTIONS & EXERCISES

# friends = 10

# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# remainder = friends % 3

# print(remainder)

# x = 3.14
# y = 4
# z = 5
# result = round(x) # это умное округление (как в математике)
# result = abs(y)
# result = pow(5, 3) # 4*4*4 типо кобейту и это пишется вот таким образом
# result = max(x, y, z)
# result = min(x, y, z)
# print(result)


import math # Подключаем модуль math, который содержит математические функции (корень, округление, пи, и т.д.)
from turtledemo.sorting_animate import enable_keys

# ceil и floor работают только с дробными числами. Если число уже целое, то оно остается таким же! ceil и floor - всегда в одну сторону! 😊
# x = 4.4
#
# print(math.pi) #Выводит число Пи (π ≈ 3.141592653589793)
# print(math.e) #Выводит число Эйлера (e ≈ 2.718281828459045)
#
# result = math.sqrt(x) # square root (квадратный корень) Вычисляет корень из x
# result = math.ceil(x) #ceiling (потолок) Округляет ВВЕРХ до ближайшего целого 9.1->10, 9.9->10
# result = math.floor(x) #Округляет ВНИЗ до ближайшего целого 9.1->9, 9.9->9
#
# print(math.sqrt(x))
# print(math.ceil(x))
# print(math.floor(x))

# import math
#
# radius = float(input("Enter the radius of a circle: "))
# circumference = 2 * math.pi * radius
# print(circumference)
# print(f"The circumference is: {round(circumference, 5)} cm") # 5 - это количество цифр после запятой, до которых нужно округлить.
# round(circumference, 5) = 62.83185 ✅ (оставили 5 цифр после запятой)

# import math
# radius = float(input("Enter the radius of a circle:" ))
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle is: {round(area, 2)}cm² ")

# import math
#
# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))
# c = math.sqrt(pow(a, 2) + pow(b, 2))
# print(f"Side C {c}")


# if = Do some code only IF some condition is TRUE
#    Else = do something else

# age = int(input("Enter your age: "))
#
# if age >= 100:
#     print("You are too old to sign up! ")
# elif age >= 18:
#     print("You are now signed up!")
# elif age < 0:
#     print("You haven't been born yet! ")
# else:
#     print("You must be 18+ to sign up! ")


#PYTHON CALCULATE OPERATOR

# operator = input("Enter an operator (+ - / *): ")
# num1 = input("Enter the 1st number: ")
# num2 = input("Enter the 2nd number: ")
#
# print(num1 + num2)


# operator = input("Enter an operator (+ - / *): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))
#
# print(num1 * num2)

# operator = input("Enter an operator (+ - / *): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))
#
# if operator == "+":
#     result = num1 + num2
#     print(result)
# elif operator == "-":
#     result = num1 - num2
#     print(result)
# elif operator == "*":
#     result = num1 * num2
#     print(result)
# elif operator == "/":
#     result = num1 / num2
#     print(result)

# operator = input("Enter an operator (+ - / *): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))
#
# if operator == "+":
#     result = num1 + num2
#     print(round(result))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result))

# operator = input("Enter an operator (+ - / *): ")
# num1 = float(input("Enter the 1sh number: "))
# num2 = float(input("Enter the 2nd number: "))
#
# if operator == "+":
#     result = num1 + num2
#     print(round(result, 3))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result, 3))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result, 3))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result, 3))
# else:
#     print(f"{operator} is not a valid operator!")

#PYTHON WEIGHT CONVERTER

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (K or L): ")
#
# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs"
#     print(f"your weight is {round(weight, 2)} {unit}")
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs"
#     print(f"your weight is {round(weight, 2)} {unit}")
# else:
#     print(f"{unit} is not valid!")

#PYTHON TEMPERATURE CONVERTER

# unit = input("Is this temperature in Celsius or Farenheit (C/F): ")
# temp = float(input("Enter the temperature: "))
#
# if unit == "C":
#     temp = round((9 * temp) / 5 + 32, 1)
#     print(f"The temperature in Farenheit is: {temp} ℉")
# elif unit == "F":
#     temp = round((temp - 32) * 5 / 9, 1)
#     print(f"The temperature in Celsius is: {temp} ℃")
# else:
#     print(f"{unit} is an invalid unit of measurement!")


#LOGICAL OPERATOR = evaluate multiple condition (or, and, not)
#                   or = at least one condition must be true
#                   and = both condition must be true
#                   not = inverts the condition (not False, not True)


# temp = 25
# is_raining = True
#
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is calceled!")
# else:
#     print("The outdoor event is still schedulled!")


# temp = 25
# is_sunny = False
#
# if temp >= 28 and is_sunny:
#     print("It is HOT outside 🥵")
#     print("It is SUNNY ☀️")
# elif temp <= 0 and is_sunny:
#     print("It is COLD outside 🥶")
#     print("It is SUNNY ☀️")
# elif 28 > temp > 0 and is_sunny:
#     print("It is WARM outside ☺️")
#     print("It is SUNNY ☀️")
# elif temp >= 28 and not is_sunny:
#     print("It is HOT outside 🥵")
#     print("It is CLOUDY ☁️️")
# elif temp <= 0 and not is_sunny:
#     print("It is COLD outside 🥶")
#     print("It is CLOUDY ☁️️")
# elif 28 > temp > 0 and not is_sunny:
#     print("It is WARM outside ☺️")
#     print("It is CLOUDY ☁️")

# name = input("Enter your full name: ")
# result = len(name) # len() number is characters
# print(result)

# name = input("Enter your full name: ")
# result = name.find("m") #любой мына жакша ишине любой символ  койып жазсак сол символга дин неше символ турганнын айтат
# print(result)

# name = input("Enter your full name: ")
# result = name.rfind("i") # например бир любой символ жазсак но сол символдын неше рет кайталанганын тауып берет
# print(result)

# name = input("Enter your full name: ")
# result = name.capitalize() # бас арипин жазып берет жазган оутпуттаг создерди
# print(result)

# name = input("Enter your full name: ")
# result = name.upper()
# print(result)

# name = input("Enter your full name: ")
# result = name.lower()
# print(result)

# name = input("Enter your full name: ")
# result = name.isdigit()
# print(result)

# name = input("Enter your full name: ")
# result = name.isalpha()
# print(result)

# phone_number = input("Enter your phone #: ")
# result = phone_number.count("-")
# print(result)

# phone_number = input("Enter your phone #: ")
# result = phone_number.replace("-", "")
# print(result)


# print(help(str))


#validate = user input exercise
# 1. username is no  more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

# username = input("Enter a username: ")
#
# if len(username) > 12:
#     print("Your username can't be more than 12 characters!")
# elif username.find(" "):
#     print("Your username must not contain spaces!")
# elif not username.isalpha():
#     print("Your username must not contain numbers!")
# else:
#     print(f"Welcome {username}")

# username = input("Enter a username:")
#
# if len(username) > 12:
#     print("Your username can't be more than 12 characters!")
# elif not username.find(" ") == -1:
#     print("Your username can't contain spaces!")
# elif not username.isalpha():
#     print("Your username can't contain numbers")
# else:
#     print(f"Welcome {username}!")