# 1 пример
# has_ticket = True
# age = 20
#
# if has_ticket == True:
#     print("The ticket is valid. We are checking age...")
#     if age >= 18:
#         print("Welcome to the movie!")
#     else:
#         print("Sorry, this movie is or adults only")
# else:
#     print("No entry. Buy the ticket first!")
#
#
# 2 пример
# login = input("Введите логин: ")
# # password = input("Введите пароль: ") # если мына жерге койсан то тогла ответ и запрос сразу бирге шыгат
#
#
# if login == "user":
#     print("Логин введен верно")
#     password = input("Введите пароль: ")
#     if password == "JQr12345": #мына жерге койсан команданы то тогда запрос поэтапно и ответтери шаг за шагом шыгат
#         print("Пароль введен верно")
#     else:
#         print("Пароль введен неверно!")
# else:
#     print("Логин введен неверно. Попробуйте еще раз!")
#
#
# 3 пример
# print("START")
#
# has_ticket = False
# age = 20
#
# if age >= 14:
#     if has_ticket:
#         print("The ticket is valid.")
#     else:
#         print("No entry. Buy the ticket first!")
# else:
#     print("No entry.")
#
# print("END")
#
#
# age = int(input("Напишите свой возраст: "))
# outfit = input("Есть ли у вас дресс-код?(да/нет)")
# if age >= 18:
#     if outfit == "да":
#         print("Добро пожаловать!")
#     else:
#         print("Извините, в спортивках нельзя")
# else:
#     print("Вход только для взрослых")
#
#
# city = input("Напишите город: ")
# weight = int(input("Напишите вес: "))
#
# if city == "Москва":
#     if weight <= 5:
#         print("стоимость 300 руб")
#     else:
#         print("стоимость 500 руб.")
#         if city == "Питер":
#             if weight <= 5:
#                 print("стоимость 400 руб")
#             else:
#                 print("стоимость 700 руб.")
#
# else:
#     print("В этот город доставки нет")

#
# level_player =  int(input("Введите свой уровень: "))
#
#
# if level_player > 10:
#     gold_value = int(input("Введите количество золото: "))
#     if gold_value > 100:
#         print("Меч куплен!")
#     else:
#         print("Уровень подходит, но не хватает золота!")
# else:
#     print("Вам не хватает уровней!")


# colour = "красный"
# size = "большой"
#
# if colour == "красный":
#     if size == "маленький":
#         print("клубника")
#     else:
#         print("арбуз")
# else:
#     if size == "большой":
#         print("Медведь")
#     else:
#         print("Мышь")

# 1 вариант
month = input("Введите число или название месяца: ")

if month == "1":
    print("Название этого месяца: Январь")
else:
    if month == "Январь":
        print("Число этого месяца: 1")
    else:
        if month == "2":
            print("Введите число или название месяца: Февраль")
        else:
            if month == "Февраль":
                print("Число этого месяца: 2")
            else:
                if month == "3":
                    print("Введите число или название месяца: Март")
                else:
                    if month == "Март":
                        print("Число этого месяца: 3")
                    else:
                        print("Такого месяца не существует")


# 2 вариант
month = input("Введите число или название месяца: ")

if month == "1":
    print("Название этого месяца: Январь")
elif month == "Январь":
    print("Число этого месяца: 1")
elif month == "2":
    print("Название этого месяца: Февраль")
elif month == "Февраль":
    print("Число этого месяца: 2")
elif month == "3":
    print("Введите число или название месяца: Март")
elif month == "Март":
    print("3")
else:
    print("Такого месяца не существует")



month = input("Введите число или название месяца: ")

if month == "1":
    print("Название этого месяца: Январь")
    if month == "Январь":
        print("Число этого месяца: 1")
    else:
        if month == "2":
            print("Введите число или название месяца: Февраль")
            if month == "Февраль":
                print("Число этого месяца: 2")
            else:
                if month == "3":
                    print("Введите число или название месяца: Март")
                    if month == "Март":
                        print("Число этого месяца: 3")
else:
    print("Такого месяца не существует")