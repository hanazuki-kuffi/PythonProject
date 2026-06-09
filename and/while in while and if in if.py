# break Останавливает цикл полностью, даже если условие ещё True.
# import time
# i = 1
#
# while i <= 20:
#     time.sleep(1)
#     if i == 11:
#         break #Цикл должен был идти до 20, но мы остановили его на 10.
#     print(i)
#     i += 1

# students = ["Ali", "Nurailym", "Gulaiym", "Nurali"]
# search = input("Кого ищем?: ")
#
# i = 0
#
# while i < 4:
#     if students[i] == search:
#         print("Нашли!")
#         break
#     i += 1



#1-задача.
#Создайте программу, которая будет работать через меню.
#После запуска, программа должна вывести сообщение с возможными вариантами ввода:
#Подсчитать квадрат числа - 1
#Выход из программы - end
#Затем программа должна запросить выбор пункта из меню
#Если пользователь вводит 1, то программа должна попросить ввести число и вывести его квадрат.
#Программа должна работать до тех пор, пока пользователь не введет слово end.


# while True:
#     print("\nMenu:")
#     print("Подсчитать квадрат числа - 1")
#     print("Выход из программы - end")
#     print()
#     choice = input("Выберите пункт меню: ")
#
#     if choice == "1":
#         number = input("Введите число: ")
#
#         while not number.isdigit():
#             print("Ошибка - некорректные данные, повторите ввод")
#             number = input("Повторите ввод: ")
#
#         print(f"Квадрат этого числа: {int(number) ** 2}")
#     elif choice == "end":
#         break
#     else:
#         print("Неизвестная команда")

#2-задача.
#Создайте программу, которая просит пользователя ввести числа, затем выводит на экран квадрат этого числа.
#Если пользователь ввел не число, а что-то другое, программа должна вывести сообщение о некорректных данных, затем просить пользователя повторить ввод.

# name = "Kuffi"
#
# i = 1
# while i <= 5:
#     print(name, "ran", i, "lap around the stadium")
#     print(name, "ran inside the stadium")
#
#     g = 1
#     while g <= 10:
#         print(name, "ran", g, "lap around the infield")
#         g += 1
#     print("Ran out of the stadium")
#     print()
#     i += 1

# import time
#
# step = 1
#
# while step <= 10:
#     print(step)
#     time.sleep(1)
#     if step != 7:
#         print("Hello")
#     step += 1

#1-задача.
#Создайте программу, которая просит пользователя ввести числа, затем выводит на экран квадрат этого числа.
#Если пользователь ввел не число, а что-то другое, программа должна вывести сообщение о некорректных данных, затем просить пользователя повторить ввод.

# 1 VARIANT
# active = True
#
# while active:
#     number = input("Введите число: ")
#
#     if not number.isdigit():
#         print("Ошибка некорректных данных, повторите ввод: ")
#     else:
#         print(f"Квадрат этих чисел: {int(number) ** 2}")
#         active = False
#
# 2.1 VARIANT
# number = input("Введите число: ") # "Hello"
# while not number.isdigit():
#     print("Ошибка - некорректные данные, повторите ввод")
#     number = input("Повторите ввод: ") # "12"
#
# print(f"Квадрат этого числа: {int(number) ** 2}")
#
#
# # 2.1 VARIANT
# number = input("Введите число: ")
#
# while not number.isdigit():
#     print("Ошибка некорректных данных, повторите ввод: ")
#     number = input("Повторите ввод: ")
# else:
#     print(f"Квадрат этих чисел: {int(number) ** 2}")
#
# while True:
#     number = input("Введите число: ")
#
#     if number.isdigit():    #мынау нени билдиреди
#         break               #неушн нахуя колдандык
#     print("Ошибка ввод данных, повторите ввод: ")
#
# print(f"Квадрат этих чисел: {int(number) ** 2}")


# print("Здравствуйте, добро пожаловать в наш магазин.")
#
# print("\nВот список товаров: ")
# print("1. Сахар - 100 тг за кг")
# print("2. Конфеты - 300 тг за кг")
# print("3. Соль - 70 тг за кг")
# print("4. Хлеб - 80 тг за булку")
# print("5. Яйца - 220 тг за лоток")
# print()

# while True:
#     goods = input("Выберите товар: ")
#     quantity = input("Выберите количество: ")
#
#     if goods == "end" and quantity == "end":
#         break
#
#     while not goods.isdigit() or not quantity.isdigit():
#         print("Ошибка - некорректные данные, повторите ввод!")
#         goods = input("Повторите ввод 1: ")
#         quantity = input("Повторите ввод 2: ")
#     else:
#         if goods == "1":
#             result1 = 100 * int(quantity)
#             print(result1)
#         if goods == "2":
#             result2 = 300 * int(quantity)
#             print(result2)
#         if goods == "3":
#             result3 = 70 * int(quantity)
#             print(result3)
#         if goods == "4":
#             result4 = 80 * int(quantity)
#             print(result4)
#         if goods == "5":
#             result5 = 220 * int(quantity)
#             print(result5)
#         if goods == "end" and quantity == "end":
#             break
#
# print()
# print("Общая стоимость: ")



#A — Лёгкие
#1. Программа просит ввести число от 1 до 10. Если ввели что-то другое или число вне диапазона — просит повторить. Когда ввели верно — выводит его квадрат.

# number = input("Введите число от 1 до 10: ")
#
# activ = True
#
# while activ:
#
#     if not number.isdigit() or 1 > int(number) or 10 < int(number):
#         print("Ошибка некорректных данных - повторите ввод!")
#         number = input("Повторите ввод: ")
#     else:
#         print(f"Квадрат этого числа: {int(number) ** 2}")
#         activ = False

#2. Программа просит вводить слова бесконечно и выводит их обратно заглавными буквами. Останавливается когда ввели stop.

# while True:
#     word = input("Введите слово: ")
#
#     if not word.isalpha():
#         print("Ошибка некорректных данных - повторите ввод:")
#         word = input("Повторите ввод:")
#
#     elif word == "stop":
#         break
#     print(word.upper())


