# We have combined two conditions using the and operators. This means that in this branch, the code block is executed only if both conditions are met  simultaneously!
# logical operator "AND"
# age = int(input("How old are you? "))
# grade = int(input("What grade are you in? "))
# if age >= 12 and grade >= 7:
#     print("Access allowed!")
# else:
#     print("Access denied!")
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
river1 = "Neva"
river2 = "Ind"

print(river1 == "Bug" and river2 != "Oder"or river1 == "Neva") # False and True or True → True (or имеет приоритет)
print(river1 != "Elba" and river1 != "Sena" and river1 != "Ind")  #True and True and True → True (все условия != выполнены)
## != означает "не равно", возвращает True если значения разные