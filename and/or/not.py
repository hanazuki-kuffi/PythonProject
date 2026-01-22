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

num = int(input("Enter the number: "))

digit_3 = num % 10
digit_2 = num % 100 // 10
digit_1 = num // 100

if digit_3 != digit_2 and digit_3 != digit_1 and digit_2 != digit_1:
    print("The numbers are different! ")
else:
    print("The numbers are not different! ")