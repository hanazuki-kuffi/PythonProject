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


age = int(input("Enter your age: "))

if age <= 13:
    print("детство")
if 14 <= age <= 24:
    print("молодость")
if 25 <= age <= 59:
    print("зрелость")
if age >= 60:
    print("старость")





