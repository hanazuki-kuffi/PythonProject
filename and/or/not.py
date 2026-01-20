# We have combined two conditions using the and operators. This means that in this branch, the code block is executed only if both conditions are met  simultaneously!
# logical operator "AND"
# age = int(input("How old are you? "))
# grade = int(input("What grade are you in? "))
# if age >= 12 and grade >= 7:
#     print("Access allowed!")
# else:
#     print("Access denied!")

# logical operator "AND"
# age = int(input("How old are you?: "))
# grade = int(input("What grade are you in?: "))
# city = input("What city do you live in?: ")
# if age >= 12 and grade >= 7 and city == "Astana ":
#     print("Access allowed!")
# else:
#     print("Access denied! ")

# logical operator "OR"
city = input("What city do you live in?: ")
if city == "Astana" or city == "Karaganda" or city == "Zhezqazgan":
    print("Access allowed!")
else:
    print("Access denied!")