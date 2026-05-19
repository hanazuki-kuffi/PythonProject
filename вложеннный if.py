1 пример
has_ticket = True
age = 20

if has_ticket == True:
    print("The ticket is valid. We are checking age...")
    if age >= 18:
        print("Welcome to the movie!")
    else:
        print("Sorry, this movie is or adults only")
else:
    print("No entry. Buy the ticket first!")


2 пример
login = input("Введите логин: ")
# password = input("Введите пароль: ") # если мына жерге койсан то тогла ответ и запрос сразу бирге шыгат


if login == "user":
    print("Логин введен верно")
    password = input("Введите пароль: ")
    if password == "JQr12345": #мына жерге койсан команданы то тогда запрос поэтапно и ответтери шаг за шагом шыгат
        print("Пароль введен верно")
    else:
        print("Пароль введен неверно!")
else:
    print("Логин введен неверно. Попробуйте еще раз!")


3 пример
print("START")

has_ticket = False
age = 20

if age >= 14:
    if has_ticket:
        print("The ticket is valid.")
    else:
        print("No entry. Buy the ticket first!")
else:
    print("No entry.")

print("END")


age = int(input("Напишите свой возраст: "))
outfit = input("Есть ли у вас дресс-код?(да/нет)")
if age >= 18:
    if outfit == "да":
        print("Добро пожаловать!")
    else:
        print("Извините, в спортивках нельзя")
else:
    print("Вход только для взрослых")


city = input("Напишите город: ")
weight = int(input("Напишите вес: "))

if city == "Москва":
    if weight <= 5:
        print("стоимость 300 руб")
    else:
        print("стоимость 500 руб.")
        if city == "Питер":
            if weight <= 5:
                print("стоимость 400 руб")
            else:
                print("стоимость 700 руб.")

else:
    print("В этот город доставки нет")
