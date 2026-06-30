# 1. Создай список из 5 любимых фруктов и выведи каждый элемент через цикл for

# my_favorite_fruits = ["banana", "apple", "peach", "persimmon", "berries"]
#
# for fruit in my_favorite_fruits:
#     print(fruit.title())     #"hello world".capitalize() ➞ "Hello world" = делает заглавной только первую букву самой строки
                             #"hello world".title() ➞ "Hello World" =  делает заглавной первую букву каждого слова

# 2. Создай список из 5 чисел и выведи первый и последний элемент

# numbers = [1, 2, 3, 4, 5]
#
# del numbers[1:4]
# print(numbers)

# 3. Создай список из 4 имён и добавь ещё одно имя в конец через append()

# names = ["ali", "nurailym", "kawai", "arai"]
#
# names.append("kuffi")
#
# print(names)


# 4. Создай список из 6 чисел и выведи только первые три через срез

# numbers = [1, 2, 3, 4, 5, 6]
#
# new_list_numbers = numbers[0:3]
#
# print(new_list_numbers)



# 5. Создай список из 5 чисел и найди сумму всех элементов через цикл for

numbers = [1, 2, 3, 4, 5]

for number in numbers: # 2
    result = number + 1 # 2 + 1 = 3
    total = result + number  # 2 + 1 = 3
print(total + result)

