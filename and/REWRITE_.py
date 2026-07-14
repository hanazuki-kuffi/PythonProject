# FUNCTION def
from difflib import restore
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



#HOMEWORK
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
#
# def merge_files(file1, file2, file3, output_file):
#
#     file_ = open(file1, "r", encoding="UTF-8")
#     read_file_ = file_.read()
#     file_.close()
#
#     file__ = open(file2, "r", encoding="UTF-8")
#     read_file__ = file__.read()
#     file__.close()
#
#
#     file___ = open(file3, "r", encoding="UTF-8")
#     read_file___ = file___.read()
#     file___.close()
#
#
#     output = open(output_file, "w", encoding="UTF-8")
#     output.write(read_file_ + "\n\n" + read_file__ + "\n\n" + read_file___)
#     output.close()
#
#
# merge_files("file1.txt", "file2.txt", "file3.txt", "destination123.txt")

#PRACTICE DEF IN DEF

# def merge_file(file1, file2, file3, output_file):
#
#     def read_file(file_name):
#
#         file = open(file_name, "r", encoding="UTF-8")
#         content = file.read()
#         file.close()
#
#         return content # потому что без этого файл будут просто читаться а не будут переносится куда-то
#
#     text_1 = read_file(file1)
#     text_2 = read_file(file2)
#     text_3 = read_file(file3)
#
#     output = open(output_file, "a", encoding="UTF-8")
#     output.write(text_1 + "\n\n" + text_2 + "\n\n" + text_3)
#     output.close()
#
#
# merge_file("file1.txt", "file2.txt", "file3.txt", "overall_file.txt")



# 1-задача: калькулятор скидок

def calculate_discount(total_amount, is_discount=False, is_loyal_customer=False):

    def main_discount(amount):

        summary1 = amount * 0.1
        return is_discount * summary1

    def loyalty_customer(amount):

        summary2 = amount * 0.05
        return is_loyal_customer * summary2


    result1 = main_discount(total_amount)
    total_amount = total_amount - result1

    result2 = loyalty_customer(total_amount)
    total_amount = total_amount - result2

    return total_amount


overall = calculate_discount(12000, is_discount=True, is_loyal_customer=True)
print(overall)




