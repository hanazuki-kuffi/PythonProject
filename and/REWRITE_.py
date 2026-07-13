# FUNCTION def

# PRACTICE TIME

#1-задача: **расчет стоимости заказа**
#Вам нужно создать **функцию** для расчета итоговой стоимости заказа в интернет-магазине.  total_amount (price, quantity, shipping)
#
# def total_amount(price, quantity, shipping):
#
#     result = price * quantity + shipping
#     return result
#
# total = total_amount(120, 3, 990)
# print(total)
from ftplib import all_errors


#2 задача: вычисление периметра и площади четырёхугольника
#Создайте две отдельные функции:
#Первая функция должна вычислять периметр четырёхугольника. Функция должна принимать длины всех четырёх сторон в качестве параметров и возвращать периметр.

#
# def perimeter_triangle(a, b, c, d):
#
#     perimeter = a + b + c + d
#     return perimeter
#
# def area_recqua(a, b):
#
#     area = 2 * (a + b)
#     return area
#
#
# result_1 = perimeter_triangle(1, 2, 3, 4)
# print(result_1)
#
# result_2 = area_recqua(1, 2)
# print(result_2)

#3 задача: вычисление среднего значения пяти чисел
#Создайте функцию, которая принимает пять чисел в качестве аргументов в соответствующие параметры.
#Функция должна:
#Рассчитывать среднее арифметическое этих чисел.
#Возвращать результат в виде целого числа.

# def arithmetic_number_of_means(a, b, c, d, e):
#
#     result = (a + b + c + d + e) // 5
#     return result
#
# total = arithmetic_number_of_means(90, 98, 95, 100, 85)
# print(total)



#PRACTICE
#
# def copy_file(source_filename, destination_filename):
#
#     file = open(source_filename, "r", encoding="UTF-8")
#     read_file = file.read()
#     file.close()
#
#     copy_file = open(destination_filename, "w", encoding="UTF-8")
#     copy_file.write(read_file)
#     copy_file.close()
#
# copy_file("file2.txt", "destination_01.txt")

# # 2-задача: объединение файлов
# #Напишите функцию, которая объединяет содержимое трёх текстовых файлов в один выходной файл.
# #Функция должна:
# #Принимать четыре аргумента:
#
def merge_files(file1, file2, file3, output_file):

    file = open(file1, "r", encoding= "UTF-8")
    read_file = file.read()
    file.close()

    file = file2, file3

    output_file = open(file, "w", encoding= "UTF-8")
    output_file.write(file1 + "\n\n" + file2 + "\n\n" + file3)

    return o