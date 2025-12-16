# num1 = int(input())
# num2 = int(input())
# if num1 < num2:
#     print(num1, 'less than', num2)
# if num1 > num2:
#     print(num1, 'more than', num2)
#
# if num1 == num2: #we use double quality
#     print(num1, 'equals', num2)
# if num1 != num2:
#     print(num1, 'not equal', num2)
# from number import last_digit, first_digit

# answer = input('What programming language are we learning?')
# if answer == 'Python':
#     print('That is right! You are genius c: c:')
#     print('Python - an awesome language!')
# else:
#     print('Not quite like that!')


# age = int(input())
# if 3 <= age <= 6:
#     print('You child!')


# word = input()
# if word =='Python':
#     print('YES')
# else:
#     print('NO')
# a = int(input())
# b = int(input())
# c = int(input())
# if a != b != c:
#     print('numbers are not equal')
# else:
#     print('numbers are equal')

# number = int(input())
# last_digit2 = number % 10    # последняя цифра числа
# first_digit1 = number // 10  # первая цифра числа
# if last_digit2 == first_digit1:
#     print('ДА')
# else:
#     print('НЕТ')

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# counter = 0
# if num1 % 2 == 0:
#     counter = counter + 1
# if num2 % 2 == 0:
#     counter = counter + 1
# if num3 % 2 == 0:
#     counter = counter + 1
# print(counter)


 # Присутствие  двоеточия : в блоке if после условия
# if num % 10 == 0:
#      print('The number is a multiple of 10')
#
# Использование оператора сравнения ==. вместо оператора присвайвание ==.
# if num == 10
#     print('The number is equal to 10')
#
# if и else на одном уровне:
# if num == 777:
#     print('The number is equal to 777')
# else:
#     print('The number not equal to 777')

# Запомните, что операторов =>, =<, =! в Python не существует! Существуют только >=, <=, !=.
# if x >= 10:
#     print('x is greater than or equal to 10')
# if y <= 20:
#     print('y is less than or equal to 20')
# if z != 30:
#     print('z is not equal to 30')


# if do some code only IF some condition is True
#     Else do something else
# age = int(input("Enter your age: "))
#
# if age >= 100:
#     print("You are too old to sign up!")
# elif age >= 18:
#     print('You are now signed up!')
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print('You must be 18+ to sign up!')

responce = input("Would you like food? (Y/N) ")

if responce == "Y":
    print("Have you some food!")
else:
    print("No food for you!")
