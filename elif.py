# num1 = int(input())
# num2 = int(input())
# if num1 < num2:
#     print(num1, 'less than', num2)
# if num1 > num2:
#     print(num1, 'more than', num2)
#
# if num1 == num2: #we use double quality
#     print(num1, 'equals', num2)
# if num1 != num2:
#     print(num1, 'not equal', num2)
# from number import last_digit, first_digit

# answer = input('What programming language are we learning?')
# if answer == 'Python':
#     print('That is right! You are genius c: c:')
#     print('Python - an awesome language!')
# else:
#     print('Not quite like that!')


# age = int(input())
# if 3 <= age <= 6:
#     print('You child!')


# word = input()
# if word =='Python':
#     print('YES')
# else:
#     print('NO')
# a = int(input())
# b = int(input())
# c = int(input())
# if a != b != c:
#     print('numbers are not equal')
# else:
#     print('numbers are equal')

# number = int(input())
# last_digit2 = number % 10    # последняя цифра числа
# first_digit1 = number // 10  # первая цифра числа
# if last_digit2 == first_digit1:
#     print('ДА')
# else:
#     print('НЕТ')

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# counter = 0
# if num1 % 2 == 0:
#     counter = counter + 1
# if num2 % 2 == 0:
#     counter = counter + 1
# if num3 % 2 == 0:
#     counter = counter + 1
# print(counter)


 # Присутствие  двоеточия : в блоке if после условия
# if num % 10 == 0:
#      print('The number is a multiple of 10')
#
# Использование оператора сравнения ==. вместо оператора присвайвание ==.
# if num == 10
#     print('The number is equal to 10')
#
# if и else на одном уровне:
# if num == 777:
#     print('The number is equal to 777')
# else:
#     print('The number not equal to 777')

# Запомните, что операторов =>, =<, =! в Python не существует! Существуют только >=, <=, !=.
# if x >= 10:
#     print('x is greater than or equal to 10')
# if y <= 20:
#     print('y is less than or equal to 20')
# if z != 30:
#     print('z is not equal to 30')


# if do some code only IF some condition is True
#     Else do something else
# age = int(input("Enter your age: "))
#
# if age >= 100:
#     print("You are too old to sign up!")
# elif age >= 18:
#     print('You are now signed up!')
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print('You must be 18+ to sign up!')

# responce = input("Would you like food? (Y/N) ")
#
# if responce == "Y":
#     print("Have you some food!")
# else:
#     print("No food for you!")

# name = input("Enter your name: ")
#
# if name == "":
#     print("You did not type in your name!")
# else:
#     print(f"Hello {name}")

# for_sale = False/True
#
# if for_sale:
#     print("This item is for sale ")
# else:
#     print("This item is NOT for sale")


# online = True/False
# if online:
#     print("The user is ONLINE")
# else:
#     print("The user is OFFLINE")

# Напишите программу, ''которая сравнивает пароль'' и его подтверждение
# password1 = input()
# password2 = input()

# if password1 == password2:       #которая сравнивает пароль
    # print(f"Пароль принят")
# else:
    # print(f"Пароль не принят")


#Напишите программу, которая определяет, является число четным или нечетным.
# number_line = int(input())
#
# if number_line % 2:  #которая определяет, является число четным или нечетным.
#     print("Нечетное")
# else:
#     print("Четное")

# Напишите программу, которая определяет, разрешён ли пользователю доступ к интернет-ресурсу или нет.
# age = int(input())
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

#Напишите программу, которая определяет наименьшее из двух чисел.
# integer1 = int(input())
# integer2 = int(input())
#
# if integer1 < integer2:
#     print(integer1)
# if integer1 > integer2:
#     print(integer2)

# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.
#
# Формат входных данных
# На вход программе подаются три целых числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести «YES» (без кавычек) или «NO» (без кавычек) в соответствии с условием задачи.
# a = int(input())
# b = int(input())
# c = int(input())
#
# if ( b - a) + b == c:
#     print("YES")
# else:
#     print("NO")

#Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.

#Формат входных данных
# На вход программе подаётся одно целое положительное четырёхзначное число.
#
# Формат выходных данных
# Программа должна вывести «ДА» (без кавычек), если соотношение выполняется, или «НЕТ» (без кавычек) в противном случае.


# integer_4 = int(input("Напиши одно целое положительное четырёхзначное число: "))
# a = (integer_4 // 1000) # (//) деление без остатка пример 1234 // 1000 = 1 это целочисленнный деление a = 1
# b = (integer_4 % 1000) // 100  # (%) это остаток от деления прмиер 1234 % 1000 = 234--> 234 // 100 = 2; b = 2
# c = (integer_4 % 100) // 10 # 1234 % 100 = (1200/100=12)= 34--> 34 // 10 = 3; c = 3
# d = (integer_4 % 10) # 1234 % 10 = (1230/10)= 4 - остаток от деления на 10 - это последняя цифра; d = 4
#
# if a + d == b - c:
#     print("ДА")
# else:
#     print("НЕТ")

#Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

# Формат входных данных
# На вход программе подаются три целых числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести одно число – сумму положительных чисел.

# a = int(input())
# b = int(input())
# c = int(input())
# sum = 0 #подсчитывает сумму
#
# if a > 0: #только положительных чисел.  # читается: "если a больше нуля"
#    sum = sum + a
# if b > 0: #только положительных чисел. # читается: "если b больше нуля"
#     sum = sum + b
# if c > 0: #только положительных чисел.  # читается: "если c больше нуля"
#     sum = sum + c
#
# print(sum)

# age = int(input())
#
# if age <= 13:
#     print("детство")
# if 14 <= age <= 24:
#     print("молодость")
# if 25 <= age <= 59:
#     print("зрелость")
# if age >= 60:
#     print("старость")


# integer_1 = int(input())
# integer_2 = int(input())
# integer_3 = int(input())
# integer_4 = int(input())
#
# if integer_1 < integer_2:
#     print(integer_1)
# elif integer_1 < integer_3:
#     print(integer_1)
# elif integer_1 < integer_4:
#     print(integer_1)

#1-задача.

# print("Введите месяца: ", end=" ")
# month_number = int(input())
#
# if month_number == 1 or month_number == 2 or month_number == 3 or month_number == 4 or month_number == 5 or month_number == 6 or month_number == 7 or month_number == 8 or month_number == 9 or month_number == 10 or month_number == 11 or month_number == 12:
#     print("Существует")
# else:
#     print("Не существует")
#
#
# print("Введите месяца: ", end=" ")
# month_number = int(input())
#
# if month_number < 12 and month_number > 0:
#     print("Существует")
# else:
#     print("Не существует")
# #
#
# #2-задача.
#
# print("Введите день: ", end=" ")
# day = int(input())
#
# if day < 31 and day >= 0:
#     print("Существует")
# else:
#     print("")

# ДОПОЛНИТЕЛЬНАЯ ЗАДАЧИ ОТ КЛАУДИ

##A — Лёгкие

#1. Запроси число и выведи "Положительное и чётное" если оба условия верны, иначе "Нет"
# print("Введите число:", end=" ")
# digit = int(input())
#
# if digit % 2 == 0 and digit > 0: #Положительное — это строго больше нуля.
#     print("True")
# else:
#     print("False")

#2. Запроси возраст и выведи "Можно смотреть" если от 6 до 18 лет, иначе "Нельзя"

# print("Введите возраст:", end=" ")
# age = int(input())
#
# if age >= 6 and age <= 18:
#     print("Можно смотреть")
# else:
#     print("Нельзя")

#3. Запроси число и выведи "Не ноль" если число не равно нулю (используй not)
# print("Введите число:", end=" ")
# number = int(input())
#
# if not number == 0:
#     print("Не ноль")
# else:
#     print("Да, ответ 0")


##B — Средние
#4. Запроси три числа и выведи "Все положительные" если все три больше нуля, иначе "Не все"
#
# print("Введите первое числo:", end=" ")
# number1 = int(input())
#
# print("Введите второе числo:", end=" ")
# number2 = int(input())
#
# print("Введите третье числo:", end=" ")
# number3 = int(input())
#
# if number1 > 0 and number2 > 0 and number3 > 0:
#     print("Все положительные")
# else:
#     print("Не все")

#5. Запроси логин и пароль. Если логин "admin" И пароль "1234" — выведи "Добро пожаловать", иначе "Ошибка"
# print("Введите логин:", end=" ")
# login = input()
#
# print("Введите пароль:", end=" ")
# password = input()
#
#
# if login == "admin" and password == "1234":
#     print("Добро пожаловать")
# else:
#     print("Ошибка")

#6. Запроси число и выведи "Выходной" если это суббота (6) или воскресенье (7), иначе "Рабочий день"

# print("Введите число:", end=" ")
# day = int(input())
# 
# if day == 6 or day == 7:
#     print("Выходной")
# else:
#     print("Рабочий день")

#7. Запроси год и выведи "Високосный" если год делится на 4, но НЕ делится на 100. Или делится на 400
# print("Введите год:", end=" ")
# year = int(input())
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Високосный")
# else:
#     print("Не високосный")

#8. Запроси три стороны треугольника. Выведи "Треугольник существует" если сумма любых двух сторон больше третьей (нужно проверить все три комбинации через and)
#
# print("Введите первой стороны трeугольника:", end=" ")
# triangle1 = int(input())
#
# print("Введите второй стороны трeугольника:", end=" ")
# triangle2 = int(input())
#
# print("Введите третьe стороны трeугольника:", end=" ")
# triangle3 = int(input())
#
#
# if triangle1 + triangle2 > triangle3 and triangle1 + triangle3 > triangle2 and triangle2 + triangle3 > triangle1:
#     print("Треугольник существует")
# else:
#     print("Треугольник не существует")

# 1-задача.Создайте программу, которая будет определять, существует ли указанный день в календаре.
#Для этого программа должна запрашивать у пользователя номер месяца (в виде числа) и номер дня,
#а затем выводить на экран сообщение о том, существует ли такой день или нет.

# print("Введите месяц:", end=" ")
# month = int(input())
#
# print("Введите день:", end=" ")
# day = int(input())
#
# if not (month >= 1 and month <= 12):
#     print("Такого дня не существует")
# else:
#     if month == 2:
#         end_day = 28
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         end_day = 30
#     else:
#         end_day = 31
#     if day >= 1 and day <= end_day:
#         print("Такой день существует")
#     else:
#         print("Такого дня не существует")

# 2-задача.Напишите программу, которая определяет, является ли год високосным или нет.
#Пользователь вводит год, после чего программа должна выводить сообщение является ли год високосным или нет.

# print("Введите год:", end=" ")
# year = int(input())
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Високосный год")
# else:
#     print("Не високосный год")

#3-задача.Напишите программу, которая запрашивает у пользователя день, месяц и год.
#Программа должна вывести на экран полную дату в правильной форме.
#Если день и месяц являются однозначными числами, то перед этим числом должен быть добавлен нулевой префикс.


# print("Введите день:", end=" ")
# day = int(input())
#
# print("Введите месяц:", end=" ")
# month = int(input())
#
# print("Введите год:", end=" ")
# year = int(input())
#
# if day >= 1 and day <= 9 and month >= 1 and month <= 9:
#     print(f"0{day}.0{month}.{year}")
# elif day >= 1 and day <= 9:
#     print(f"0{day}.{month}.{year}")
# elif month >= 1 and month <= 9:
#     print(f"{day}.0{month}.{year}")
# else:
#     print(f"{day}.{month}.{year}")