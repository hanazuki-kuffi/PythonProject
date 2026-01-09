# num_seven = 7
# num_ten = 10
# num_seventeen = 17
# print(num_seventeen)
from calendar import firstweekday
from urllib.parse import non_hierarchical

# a = 5
# b = 4
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# g = '2004'  # естб какие нибудь разница между кавычкой или просто написав число
# year = int(g)
# print(year)

# num1 = input()
# num2 = input()
# print(num1+num2)

# num1 = int(input())
# num2 = int(input())
# print(num1+num2)

# s = 0
# k = 30
# d = k - 5
# k = 2 * d
# s = k - 100
#
# print(s)

# x = 3
# y = 4
# z = x + y
# z = z + 1
# x = y
# y = 5
# x = z + y + 7
#
# print(x)

# a = int(input())
# b = a + 1
# c = a + 2
#
# print(a)
# print(b)
# print(c)

# a =  int(input())
# b = a + 1
# c = a + 2
#
# print(a)
# print(b)
# print(c)

# a = int(input())
# b = a + 1
# c = a + 2
# print(a)
# print(b)
# print(c)

# a = int(input())
# b = a + 1
# c = a + 2
# print(a)
# print(b)
# print(c)

# a =  int(input())
# b = a + 1
# c = a + 2
# print(a)
# print(b)
# print(c)


# a = int(input())
# b = int(input())
# c = int(input())
# x = a + b + c
# print(x)

# monitor = int(input())
# system_unit = int(input())
# keyboard = int(input())
# mouse = int(input())
# x = (monitor + system_unit + keyboard + mouse) * 3
# print(x)

# a = int(input())
# b = int(input())
# x = 3 * (a + b) * (a + b) * (a + b) + 275 * b * b - 127 * a - 41
# print(x)

# лучге всего будет если ты берешь эти чисел на скобках так будет в программе понятнее потоу что программа читат в одном направлний
# то есть слева и на право
# a = int(input())
# b = int(input())
# x = (3 * (a + b) * (a + b) * (a + b)) + (275 * b * b) - (127 * a) - 41
# print(x)

# twenty = int(input())
# next = "Следующее за числом 20 число: 21"
# previous = "Для числа 20 предыдущее число: 19"
# print(twenty)
# print(next)
#
# print(previous)


# number = int(input())
# next_to = 'Следующее за числом  number, 'число:', number + 1
# previous = 'Для числа', number, 'предыдущее число:', number - 1
#
# print(next_to)
# print(previous)


# SHOULD BE A LOT OF PRACTICE
# number = int(input())
# next_to = number + 1
# previous = number - 1
# print('Следующее за числом', number, 'число:', next_to)
# print('Для числа', number, 'предыдущее число:', previous)


# SHOULD BE A LOT OF PRACTICE
# rib_length = int(input())
# V = rib_length * rib_length * rib_length
# S = 6 * (rib_length * rib_length)
# print('Объем =', V)
# print('Площадь полной поверхности =', S)


# SHOULD BE A LOT OF PRACTICE
# a = int(input())
# b = int (input())
# print(a, '+', b, '=', a + b)
# print(a, '-', b, '=', a - b)
# print(a, '*', b, '=', a * b)


# SHOULD BE A LOT OF PRACTICE
# a1 = int(input())
# d = int(input())
# n = int(input())
# aN = a1 + (d * (n - 1))
# print(aN)


# SHOULD BE A LOT OF PRACTICE
# x = int(input())
# print(x, 2 * x,3 * x,4 * x,5 * x, sep='---')


# SHOULD BE A LOT OF PRACTICE
# b1 = int(input())
# q = int(input())
# n = int(input())
# bn = b1 * q**(n - 1)
# print(bn)



# SHOULD BE A LOT OF PRACTICE
# cm = int(input())
# meter = cm // 100
# print(meter)



# n_stud = int(input())
# k_orange = int(input())       n = 100%   /2 четные и нечетные числа
#                               survivors = 50%
# print(k_orange // n_stud)
# print(k_orange % n_stud)

# SHOULD BE A LOT OF PRACTICE
# n = int(input())
# print((n + 1) // 2)

# SHOULD BE A LOT OF PRACTICE
# inomin = int(input())
# tonohours = (inomin//60)
# remnominutes = (inomin % 60)
# print(inomin,'min - the', tonohours, 'hour', remnominutes, 'minutes')

# number_seat = int(input())
# seat = 36 - number_seat
# coupe = seat // 4
# print(9 - coupe)

# number = int(input())
# last_digit = (number % 10)
# average_digit = (number % 100) // 10
# first_digit = number // 100
# adding_numbers = (last_digit + average_digit + first_digit)
# equation_numbers = (last_digit * average_digit * first_digit)
# print('Сумма цифр =', adding_numbers)
# print('Произведение цифр =', equation_numbers)

# numbers = int(input())
# last_digit = (numbers % 10)
# average_digit = (numbers % 100) // 10
# first_digit = (numbers // 100)
# print(first_digit,average_digit,last_digit, sep='')
# print(first_digit,last_digit,average_digit, sep='')
# print(average_digit,first_digit,last_digit, sep='')
# print(average_digit,last_digit,first_digit, sep='')
# print(last_digit,first_digit,average_digit, sep='')
# print(last_digit,average_digit,first_digit, sep='')
#
# four_digit_integer = int(input())
# first_digit = (four_digit_integer // 1000 )
# second_digit = ((four_digit_integer % 1000) // 100)
# third_digit = ((four_digit_integer % 100) // 10)
# four_digit = (four_digit_integer % 10)
# print('Цифра в позиции тысяч равна', first_digit)
# print('Цифра в позиции сотен равна', second_digit)
# print('Цифра в позиции десятков равна', third_digit)
# print('Цифра в позиции единиц равна', four_digit)

# print("степиктан новый задания истедим")

# s = 13
# k = -5
# d = s + 2  13 +2 = 15
# s = d 13= 15
# k = 2 * s 15 * 2 = 30
# print(s + k + d) 15 + 30 + 15

# a = 17 // (23 % 7)
# b = 34 % a * 5 - 29 % 4 * 3 10-3
# print(a * b)

# говнокод
# print('*****************')
# print('*               *')
# print('*               *')
# print('*****************')

# замудренный код
# a = "*"
# print(a * 17 + "\n" + a + " " * 15 + a + "\n" + a + " " * 15 + a + "\n" + a * 17)

# a = int(input())
# b = int(input())
# square_of_the_sum = (a + b)**2
# sum_of_squares = a**2 + b**2
# print('Квадрат суммы', a, 'и', b, 'равен',square_of_the_sum )
# print('Сумма квадратов', a, 'и', b, 'равна', sum_of_squares)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(a**b + c**d)

# n = input()
# nn = n + n
# nnn = n + n + n
# print(int(n) + int(nn) + int(nnn))