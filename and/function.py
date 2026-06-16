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
#
# def arithmetic_mean_of_numbers(num1, num2, num3, num4, num5):
#     result = (num1 + num2 + num3 + num4 + num5) / 5
#     result = int(result)
#     return  result
#
# result1 = arithmetic_mean_of_numbers(1, 2, 3, 4, 5)
# print(result1)
#
# def copy_file(source_filename, destination_filename):
#     source = open(source_filename, "r", encoding="UTF-8")
#     file = source.read()
#     source.close()
#
#     destination = open(destination_filename, "w", encoding="UTF-8") #"w" нужен для копирования!
#     destination.write(file)
#     destination.close()
#
#
# copy_file("file1.txt", "destination1.txt")


# 2-задача: объединение файлов
#Напишите функцию, которая объединяет содержимое трёх текстовых файлов в один выходной файл.
#Функция должна:
#Принимать четыре аргумента:
#
# def merge_files(file1, file2, file3, output_file):
#
#     file_1 = open(file1, "r", encoding= "UTF-8")
#     file_11 = file_1.read()
#     file_1.close()
#
#     file_2 = open(file2, "r", encoding= "UTF-8")
#     file_22 = file_2.read()
#     file_2.close()
#
#     file_3 = open(file3, "r", encoding= "UTF-8")
#     file_33 = file_3.read()
#     file_3.close()
#
#     output = open(output_file, "a", encoding= "UTF-8")
#     output.write(file1 + "\n" + file2 + "\n" + file3 )
#     output.close()
#
#
#
# def convert_seconds(conver_sec):
#
#     conver_sec = int(conver_sec) #: 100 000
#
#     day = conver_sec // 86400 # 100 000 // 86 400 = 1 day
#     hour = (conver_sec % 86400) // 3600 #100 000 - 86 400 = 13 600 // 3600 = 3 hour
#     minute = (conver_sec % 3600) // 60 #100 000 % 3600 = 2800 // 60 = 46 min
#     seconds = conver_sec % 60
#
#     result = f"{str(day)}:{str(hour)}:{str(minute)}:{str(seconds)}" #1:3:46:40
#     return result
#
#
# result1 = convert_seconds(86400)
# print(result1)
# result1 = convert_seconds(59)
# print(result1)
# result1 = convert_seconds(3661)
# print(result1)
# result1 = convert_seconds(172800)
# print(result1)
# result1 = convert_seconds(100000)
# print(result1)
