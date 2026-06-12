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


#1-задача: **расчет стоимости заказа**
#Вам нужно создать **функцию** для расчета итоговой стоимости заказа в интернет-магазине.



def total_amount(price, quantity, shipping):
    result = price * quantity + shipping
    return  result


total = total_amount(500.0, 3, 150.0)
print(total)



#2 задача: вычисление периметра и площади четырёхугольника
#Создайте две отдельные функции:
#Первая функция должна вычислять периметр четырёхугольника. Функция должна принимать длины всех четырёх сторон в качестве параметров и возвращать периметр.

def perimeter_qua(a, b, c, d):
    formula = a + b + c + d
    return formula

def area_recqua(a, b):
    formula = a * b
    return formula


result1 = perimeter_qua(1, 2, 3, 4)
result2 = area_recqua(2, 3)

print(result1)
print(result2)


#3 задача: вычисление среднего значения пяти чисел
#Создайте функцию, которая принимает пять чисел в качестве аргументов в соответствующие параметры.
#Функция должна:
#Рассчитывать среднее арифметическое этих чисел.
#Возвращать результат в виде целого числа.

def arithmetic_mean_of_numbers(num1, num2, num3, num4, num5):
    result = (num1 + num2 + num3 + num4 + num5) / 5
    result = int(result)
    return  result

result1 = arithmetic_mean_of_numbers(1, 2, 3, 4, 5)
print(result1)