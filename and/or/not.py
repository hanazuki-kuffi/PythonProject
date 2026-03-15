# We have combined two conditions using the and operators. This means that in this branch, the code block is executed only if both conditions are met  simultaneously!
# logical operator "AND"
# age = int(input("How old are you? "))
# grade = int(input("What grade are you in? "))
# if age >= 12 and grade >= 7:
#     print("Access allowed!")
# else:
#     print("Access denied!")
from platform import android_ver
from selectors import SelectSelector
from termios import INPCK

# logical operator "AND"
# age = int(input("How old are you?: "))
# grade = int(input("What grade are you in?: "))
# city = input("What city do you live in?: ")
# if age >= 12 and grade >= 7 and city == "Astana ":
#     print("Access allowed!")
# else:
#     print("Access denied! ")

# logical operator "OR"
#Access will be allowed if at least one of the conditions is met.
# city = input("What city do you live in?: ")
# if city == "Astana" or city == "Karaganda" or city == "Zhezqazgan":
#     print("Access allowed!")
# else:
#     print("Access denied!")

# logical operator "OR" & "AND"
# age = int(input("How old are you?: "))
# grade = int(input("What grade are you in?: "))
# city = input("What city do you live in ?: ")
# if age >= 12 and grade >= 7 and (city == "Astana" or city == "Almaty"):
#     print("Access allowed! ")
# else:
#     print("Access denied! ")


# logical operator "NOT"
#Технически NOT не обязателен — всегда можно переписать. Но он делает код читабельнее, когда ты думаешь "от обратного" — "если НЕ дождь", "если НЕ залогинен", "если НЕ готово".
# age = int(input("How old are you?: "))
# if not (age < 12):
#     print("Access allowed! ")
# else:
#     print("Access denied! ")


#  Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным.

# num = int(input("Enter the number: "))
#
# if 100 <= num <= 999:
#     print("The number is three-digit! ")
# else:
#     print("The number is not three-digit! ")

#  Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.

# num = int(input("Enter the number: "))

# digit_3 = num % 10
# digit_2 = num % 100 // 10
# digit_1 = num // 100
#
# if digit_3 != digit_2 and digit_3 != digit_1 and digit_2 != digit_1:
#     print("The numbers are different! ")
# else:
#     print("The numbers are not different! ")


#Задача 3. Напишите программу, которая по координатам точки, не лежащей на осях координат, определяет номер координатной четверти, в которой она находится.

# x = int(input("Enter the X number of a axis: "))
# y = int(input("Enter the Y number of a axis: "))
#
# if x > 0 and y > 0:
#     print("1st quarter!")
# if x < 0 and y > 0:
#     print("2nd quarter!")
# if x < 0 and y < 0:
#     print("3st quarter!")
# if x > 0 and y < 0:
#     print("4th quarter!")


# river1 = "Volga"
# river2 = "Elba"
#
# print(river1 == "Bug" and river2 == "Oder")
# print(river2 != "Elba" or river1 != "Lena")

# river1 = "Irtysh"
# river2 = "Yantze"
#
# print(river1 == "Amur" or river1 == "Irtysh")
# print(river2 != "Kama" or river2 == "Po")

# river1 = "Rain"
# river2 = "Ind"
#
# print(river1 != "Amur" or river1 != "Dunai")
# print(river2 != "Kama" and river2 != "Ind")

# == равно, != не равно
# river1 = "Neva"
# river2 = "Ind"
#
# print(river1 == "Bug" and river2 != "Oder"or river1 == "Neva") # False and True or True → True (or имеет приоритет)
# print(river1 != "Elba" and river1 != "Sena" and river1 != "Ind")  #True and True and True → True (все условия != выполнены)
# != означает "не равно", возвращает True если значения разные

# num1 = 34
# num2 = 81
#
# if num1 // 9 or num2 % 9 == 0:
#     print("number", num1, "won")
# else:
#     print("number", num2, "won")

# a = int(input())
#
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
#                       A challenge for attentivetess! DO NOT get carried  away in this conditions. Identation is very inportant in Python!
# p = (a + b) * (a + b)
# print(p)


# x = int(input())
#
# if x > -1 and x < 17:
#     print("Belongs")
# else:
#     print("Doesn't belong")


# x = int(input())
#
# if -3 >= x or 7 <= x:
#     print("Belongs")
# else:
#     print("Doesn't belong")


# x = int(input())
#
# if  -30 < x <= -2 or 7 < x <= 25:
#     print("Belongs")
# else:
#     print("Doesn't belong")

# digit_0 = int(input("Enter the number: "))
#
# if 1000 <= digit_0 <= 9999 and (digit_0 % 7 == 0 or digit_0 % 17 == 0):
#     print("YES")
# else:
#     print("NO")


# a = int(input("Enter the 1st number: "))
# b = int(input("Enter the 2nd number: "))
# c = int(input("Enter the 3th number: "))
#
# if a + b > c and a + c > b and b + c > a:
#     print("YES")
# else:
#     print("NO")

# sj we can write through negative not()

# a, b, c = int(input()), int(input()), int(input())
#
# if not (a + b <= c or a + c <= b or b + c <= a):
#     print("YES")
# else:
#     print("NO")

# calendar = int(input())
#
# if calendar % 4 == 0 and (calendar % 100  or calendar % 400 == 0):
#     print("YES")
# else:
#     print("NO")

#Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от
# 1
# 1 до
# 8
# 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES» (без кавычек), если из первой клетки ходом ладьи можно попасть во вторую, или «NO» (без кавычек) в противном случае.
# x1 = int(input("Choose these numbers around 1-8: "))
# x2 = int(input("Choose these numbers around 1-8: "))
# y1 = int(input("Choose these numbers around 1-8: "))
# y2 = int(input("Choose these numbers around 1-8: "))
#
# if x1 == y1 or x2 == y2: #Чтобы ладья могла перейти с одной клетки на другую, нам достаточно проверить, что координаты этих клеток равны по вертикали или по горизонтали.
#     print("YES")
# else:
#     print("NO")


# x1 = int(input())
# x2 = int(input())
# y1 = int(input())
# y2 = int(input())
#
# if x1 == x2 and :
#     print("YES")
# else:
#     print("NO")


# королль у нас ходит по горизонтали по вертикали и по диагонали но только на одну клетку
# у нас есть два различных клеток и каждый из них чередуется между собой
# чтоб король мог двигаться с одной клетки на другую координата по вертикали отличается не более чем на 1 и по горизонтали отличается не более чем на 1

#
#
# if condition1:
#     print()
# else:
#     if condition2:
#         print()
#     else:
#         if condition3:
#             print()


# x = int(input())
# y = int(input())

# if x > 0:
#     if y > 0:
#         print("First quarter")
#     else:
#         print("Fourth quarter")
# else:
#     if y > 0:
#         print("Second quarter")
#     else:
#         print("Third quarter")


# grade = int(input("Please enter your score out of 100: "))

# if grade >= 90:
#     print(5)
# else:
#     if grade >= 80:
#         print(4)
#     else:
#         if grade >= 70:
#             print(3)
#         else:
#             if grade >= 60:
#                 print(2)
#             else:
#                 print(1)


# grade = int(input("Please, enter your score out of 100: "))
#
# if grade >= 90:
#     print(5)
# elif grade >= 80:
#     print(4)
# elif grade >= 70:
#     print(3)
# elif grade >= 60:
#     print(2)
# else:
#     print(1)

# traffic_light_signal = input("Enter the traffic light signal: ")
#
# if traffic_light_signal == "red":
#     print("Stop!")
# elif traffic_light_signal == "yellow":
#     print("Get ready!")
# elif traffic_light_signal == "green":
#     print("Go!")

# num_a = int(input("Enter the number: "))
# num_b = int(input("Enter the number: "))
# num_c = int(input("Enter the number: "))
#
# if num_a == num_b:              # Если a равно b
#     if num_b == num_c:          # И b равно c
#         print(3)                # → Значит все три равны!
#     else:                       # Иначе (b не равно c)
#         print(2)                # → Только a и b равны
# else:                           # иначе
#     if num_a == num_c:          # Проверяем, может a равно c?
#         print(2)                # → a и c равны
#     else:                       # a не равно c
#         if num_b == num_c:      # Проверяем, может b равно c?
#             print(2)            # → b и c равны
#         else:
#             print(0)            # Все разные


# num_a = int(input())
# num_b = int(input())
# num_c = int(input())
#
# if num_a == num_b:
#     if num_b == num_c:
#         print(3)
#     else:
#         print(2)
# else:
#     if num_a == num_c:
#         print(2)
#     else:
#         if num_b == num_c:
#             print(2)
#         else:
#             print(0)


#САМЫЙ ИДЕЛАЬНЫЙ И ЧИТАБЕЛЬНЫЙ КОД КАК МЫ ПОЛОГАЕМ
# num_a = int(input())
# num_b = int(input())
# num_c = int(input())
#
# if num_a == num_b == num_c:
#     print(3)
# elif num_a == num_b:
#     print(2)
# elif num_b == num_c:
#     print(2)
# elif num_a == num_c:
#     print(2)
# else:
#     print(0)


# num_a = int(input())
# num_b = int(input())
# num_c = int(input())
#
# if num_a == num_b == num_c:
#     print(3)
# elif num_a == num_b or num_b == num_c or num_b == num_c:
#     print(2)
# else:
#     print(0)

# angle = int(input())
#
# if angle % 90 == 0:
#     print("тут ничего нет ")
#     if angle == 0:
#         print("Нулевой")
#     elif angle == 90:
#         print("Прямой")
#     elif angle == 180:
#         print("Развернутый")
# else:
#     if 0 < angle < 90:
#         print("Острый")
#     elif 90 < angle < 180:
#         print("Тупой")
#     elif 180 < angle < 270:
#         print("Выпуклый")
#     else:
#         print("Ни тупой ни острый, ни выпуклый") # вот тут можно ставить 291 а не 360 и вот почему в else показал 291 а в 360 вообще ничего не вышло в чем разница


# zume_n = int(input())
# flash_k = int(input())
#
# if zume_n > flash_k:
#     print("NO")
# elif flash_k > zume_n:
#     print("YES")
# else:
#     print("Don't know")


# triangle_1 = int(input())
# triangle_2 = int(input())
# triangle_3 = int(input())
#
# if triangle_1 == triangle_2:
#     if triangle_2 == triangle_3:
#         print("Равносторонний")
#     else:
#         print("Равнобедренный")
# else:
#     if triangle_1 == triangle_3:
#         print("Равнобедренный")
#     else:
#         if triangle_2 == triangle_3:
#             print("Равнобедренный")
#         else:
#             print("Разносторонний")
#
#
# triangle_1 = int(input())
# triangle_2 = int(input())
# triangle_3 = int(input())
#
# if triangle_1 == triangle_2 == triangle_3:
#     print("Равносторонний")
# elif triangle_1 == triangle_2:
#     print("Равнобедренный")
# elif triangle_2 == triangle_3:
#     print("Равнобедренный")
# elif triangle_1 == triangle_3:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")
#



# сперва числоларды сортировать ету керек типо томеннен жогары карай
# потом после этого есть готовые формулы соган салып корип кодты проверка жасау керек
#

# digit_1 = int(input())
# digit_2 = int(input())
# digit_3 = int(input())
#
# if digit_1 < digit_2 < digit_3:
#     print(digit_2)
# elif digit_3 < digit_1 < digit_2:
#     print(digit_1)
# elif digit_1 < digit_3 < digit_2:
#     print(digit_3)
# elif digit_3 < digit_2 < digit_1:
#     print(digit_2)
# elif digit_2 < digit_1 < digit_3:
#     print(digit_1)
# elif digit_2 < digit_3 < digit_1:
#     print(digit_3)


# digit_1 = int(input())
# digit_2 = int(input())
# digit_3 = int(input())
#
# if digit_1 < digit_2 < digit_3 or digit_3 < digit_2 < digit_1:
#     print(digit_2)
# elif digit_3 < digit_1 < digit_2 or digit_2 < digit_1 < digit_3:
#     print(digit_1)
# else:
#     print(digit_3)


# month_ordinal_number = int(input("Enter the month ordinal number: "))
#
# if month_ordinal_number == 1 or month_ordinal_number == 3 or month_ordinal_number == 5 or month_ordinal_number == 7 or month_ordinal_number == 8 or month_ordinal_number == 10 or month_ordinal_number == 12:
#     print(31)
# elif month_ordinal_number == 4 or month_ordinal_number == 6 or month_ordinal_number == 9 or month_ordinal_number == 11:
#     print(30)
# else:
#     print(28)


# boxer_weight = int(input())
#
# if boxer_weight < 60:
#     print("Легкий вес")
# elif boxer_weight < 64:
#     print("Первый полусредний вес")
# else:
#     print("Полусредний вес")

# number_1 = int(input("Enter the number: "))
# number_2 = int(input("Enter the number: "))
# operator = input("Enter an operator ( +, -,  *, / ): ")
#
# if operator == "+":
#     result = number_1 + number_2
#     print(result)
# elif operator == "-":
#     result = number_1 - number_2
#     print(result)
# elif operator == "*":
#     result = number_1 * number_2
#     print(result)
# elif operator == "/":
#     if number_2 == 0:
#         print("На ноль делить нельзя!")
#     else:
#         result = number_1 / number_2
#         print(result)
# else:
#     print("Неверная операция")



# colour_1 = input("Enter the colour (red,blue,yellow): ")
# colour_2 = input("Enter the colour (red,blue,yellow): ")
#
# if colour_1 == "red" and colour_2 == "blue":
#     print("Purple")
# elif colour_1 == "red" and colour_2 == "yellow":
#     print("Orange")
# elif colour_1 == "blue" and colour_2 == "yellow":
#     print("green")
# elif colour_1 == "red" and colour_2 == "red":
#     print("red")
# elif colour_1 == "yellow" and colour_2 == "yellow":
#     print("yellow")
# elif colour_1 == "blue" and colour_2 == "blue":
#     print("blue")
# else:
#     print("colour error")



# colour_1 = input()
# colour_2 = input()
#
# if colour_1 == "красный" and colour_2 == "синий" or colour_1 == "синий" and colour_2 == "красный":
#     print("фиолетовый")
# elif colour_1 == "красный" and colour_2 == "желтый" or colour_1 == "желтый" and colour_2 == "красный":
#     print("оранжевый")
# elif colour_1 == "синий" and colour_2 == "желтый" or colour_1 == "желтый" and colour_2 == "синий":
#     print("зеленый")
# elif colour_1 == "красный" and colour_2 == "красный":
#     print("красный")
# elif colour_1 == "желтый" and colour_2 == "желтый":
#     print("желтый")
# elif colour_1 == "синий" and colour_2 == "синий":
#     print("синий")
# else:
#     print("ошибка цвета")


# pocket = int(input())
#
# if pocket == 0:
#     print("Green")
# elif 1 <= pocket <= 10:
#     if pocket % 2 == 0:
#         print("Black")
#     elif pocket % 2 == 1:
#         print("Red")
# elif 11 <= pocket <= 18:
#     if pocket % 2 == 0:
#         print("Red")
#     elif pocket % 2 == 1:
#         print("Black")
# elif 19 <= pocket <= 28:
#     if pocket % 2 == 0:
#         print("Black")
#     elif pocket % 2 == 1:
#         print("Red")
# elif 29 <= pocket <= 36:
#     if pocket % 2 == 0:
#         print("Red")
#     elif pocket % 2 == 1:
#         print("Black")
# else:
#     print("ошибка ввода")


a_1 = int(input())
b_1 = int(input())
a_2 = int(input())
b_2 = int(input())

result = a_1 < b_1 and a_2 < b_2

if a_1
    x = int(input())
    y = int(input())

    if x > 0:
        if y > 0:
            print('Первая четверть')
        else:
            print('Четвертая четверть')
    else:
        if y > 0:
            print('Вторая четверть')
        else:
            print('Третья четверть')