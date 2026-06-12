#
# def welcome_user(name, is_returning_user=True):
#     """Output greeting with the provived name."""
#     if is_returning_user:
#         message = f"Welcome back {name}!"
#     else:
#         message = f"Welcome {name}!"
#
#     print(message)
#
# welcome_user(name="Kuffi")
# welcome_user("c: c:", is_returning_user=True)
# welcome_user("Ali", False)
#
#
#
# one = True
#
# while one:
#     print("Регистрация\n")
#     name = input("Ваше имя: ")
#     password_ = input("Придумайте пароль: ")
#     password__ = input("Подтвердите пароль: ")
#
#     if password_ != password__:
#         print("Неверный пароль, начните заново!")
#     else:
#         print("Данные сохранены!\n")
#
#         while one:
#             print("Авторизация")
#
#             login = input("Введите логин: ")
#             password = input("Введите пароль: ")
#
#             if not (login == name and password == password_):
#                 print("Вход не выполнен")
#             else:
#                 print("Вход выполнен")
#                 one = False
#
#
#
# def reg():
#     while True:
#         print("Регистрация\n")
#         login = input("Ваше имя: ")
#         password = input("Придумайте пароль: ")
#         password_ = input("Подтвердите пароль: ")
#
#         if password != password_:
#             print("Неверный пароль, начните заново!")
#         else:
#             print("Данные сохранены!\n")
#             return login + password
#
#
# def auto(user_data):
#     while True:
#         print("Авторизация")
#
#         login = input("Введите логин: ")
#         password = input("Введите пароль: ")
#
#         if not (login + password == user_data):
#             print("Вход не выполнен")
#         else:
#             print("Вход выполнен")
#             break



#1-задача: **расчет стоимости заказа**
#Вам нужно создать **функцию** для расчета итоговой стоимости заказа в интернет-магазине.

def total_amount(price, quantity, shipping):
    result = price * quantity + shipping
    return  result


total = total_amount(500.0, 3, 150.0)
print(total)