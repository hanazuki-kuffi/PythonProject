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