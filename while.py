# name = input("Please enter your name: ")
# print(f"Hello {name}!\n")
# from http.cookiejar import user_domain_match
from itertools import repeat
from math import acosh
from pyexpat.errors import messages

# prompt = "If you tell us who you are, we can personalise the messages you see!"
# prompt += "\nWhat is your first name?: "
#
# name = input(prompt)
# print(f"\nHello {name}!")

# age = input("How old are you?: ")
# print(age)
#
# age = input("How old are you? ")
# age = int(age)
# age >= 18

# height = input("How tall are you, inches? ")
# height = int(height)
#
# if height >= 48:
#     print("\nYou are tall enough to ride")
# else:
#     print("\nYou will be able to the ride when you are a little older.")


# number = input("Enter a number, and I will tell you if it is even or odd: ")
# number = int(number)
#
# if number % 2 == 0:
#     print(f"The number {number} is even.\n")
# else:
#     print(f"The number {number} is odd.\n")

# car = input("What kind of car would he like to rent? ")
# print(f"Let me see if I can find you a {car}.")


# seats = input("How many seats does he/she want to reserve a table for in the restaurant? ")
# seats = int(seats)
#
# if seats > 8:
#     print("You will have to wait 😅!")
# else:
#     print("The table is ready ☺️!")

# user_value = int(input("Enter a number: "))
#
# if user_value % 10 == 0:
#     print("multiple value")
# else:
#     print("not a multiple of 10")


# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

#
# prompt = "\nTell me something and I will repeat it back to you. "
# prompt += "\nEnter 'quit' to end the program: "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)


# prompt = "\nTell me something and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program!: "
#
# message = ""
# while message != 'quit':
#     message = input(prompt)
#
#     if message != 'quit':
#         print(message)

# prompt = "\nTell me something and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program!: "
#
# active = True
#
# while active:
#     message = input(prompt)

# i = 10
#
# while i < 50:
#     print(i)
#     i += 10

# while True:  # В ЛЮБОМ СЛУЧАЕ ЭТО НЕЛЬЗЯ ЗАПУСКАТЬ А ТО БЕЗКОНЕЧНО ЦИКЛ ТОКТАМАЙ ЖУРЕ БЕРЕТ
#     print("Infinite loop")

# while True:
#     answer = input("Enter 'yes' or 'no': ")
#     if answer == 'no':
#         break

import random

# random_num = random.randint(1, 5)
# while True: #while = "принимать пациентов пока рабочий день не закончится" — не знаешь сколько придёт, просто работаешь пока условие (рабочий день) правда. 😊
#     num = int(input("Guess the number from 1 to 5: "))
#     if num != random_num:
#         print("Try again...")
#         continue
#     print("Congratulations", random_num)
#     break #он говорит "выйди из цикла прямо сейчас".


# prompt = "\nTell me something and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program!: "
#
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)


# prompt = "\nPlease, enter the name of a city you have visited"
# prompt += "\n Enter 'quit' when you are finished: "
#
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break #Команда break может использоваться в любых циклах Python . Напри- мер, ее можно включить в цикл for для перебора элементов словаря .
#     else:
#         print(f"I would love to go to {city.title()}!")

# current_number = 0
#
# while current_number < 10:
#     current_number = current_number + 1
#
#     if current_number % 2 == 0:
#         continue
#     print(current_number)


# x = 1
# while x <= 5:
#     print(x)

# x = 1
# while x <= 5:
#      print(x)
#      x += 1

#
# pizza_order = "\nPlease, enter your addition for pizza!"
# pizza_order += "\nEnter 'quit' when you are finished: "
#
# while True:
#     order = input(pizza_order)
#     if order == 'quit':
#         break
#     else:
#         print("This supplement is included in the order!")


#  1) age > 3: -- free
#  2) 3 < age < 12: -- 10 dollars ticket
#  3) age > 12: -- 15 dollars ticket
# напишите цикл который предлагает пользователю ввести возраст и выводит цену билета


# message = "Enter your age for buying tickets. Please, enter the 'quit, when you are finished!: "
#
# active = True
#
# while active:
#     age = input(message)
#
#     if age == 'quit':
#         active = False
#     else:
#         if int(age) < 3:
#             print("Free tickets!")
#         elif 3 <= int(age) <= 12:
#             print("The ticket costs $10")
#         elif int(age) > 12:
#             print("The ticket costs $15")
#
# message = "Enter you age for buying tickets. Please enter the 'quit' when you are finished!: "
#
# active = True
#
# while active:
#     age = input(message)
#
#     if age == 'quit':
#         active = False
#     else:
#         if int(age) < 3:
#             print("Free tickets!")
#         elif 3 < int(age) < 12:
#             print("The ticket costs $10!")
#         elif int(age) > 12:
#             print("The ticket costs $15!")
#             break
#
#
# integer = 1
#
# while integer < 100:
#     print(integer)


# unconfirmed_users = ["Ali", "Nurai", "Arai", "Kawai"]
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f"Veryfuying users: {current_user.title()}")
#     confirmed_users.append(current_user)
#
# print("\nThe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())














#
# unconfirmed_users = ["Ali", "Nurai", "Kawai", "Arai"]
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f"Veryfuying user: {current_user.title()}")
#     confirmed_users.append(current_user)
#
# print("\nThe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# pets = ["cat", "dog", "cat", "goldfish", "lamb", "cat", "rabbit"]
# print(pets)
#
# while "cat" in pets:
#     pets.remove("cat")
#
# print(pets)

# responses = {}
#
# polling_active = True
#
# while polling_active:
#     name = input("\n What is your name? ")
#     response = input("\n Wich mountain would you like to climb someday? ")
#
# responses[name] = response
#
# repeat = input("\n Would you like to let another person respond? (yes/no) ")
#
# if repeat == 'no':
#     polling_active = False
#
# print("\n --- Poll results ---")
#
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")

# name = input("What is your name? ")
#
# while name == "":
#     print("You did not enter your name")
#     name = input("What is your name? ")
#
# print(f"Hello {name}!")
#
# i = 0
#
# while i != 20:
#     i += 2
#     print(i)
# print("end")


# sandwich_orders = ["panini", "tuna sanwich", "grilled cheese sanwich", "tartine"]
# finished_sandwiches = []
#
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#
#     print(f"I made your tuna sandwich: {current_sandwich.title()}")
#     finished_sandwiches.append(current_sandwich.title())
#
# print(finished_sandwiches)

sandwich_orders = ["panini", "pastrami", "pastrami", "tuna sanwich", "pastrami", "grilled cheese sanwich", "pastrami", "tartine"]
finished_sanwiches = []
print("There is no more pastrami!\n")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)
#     current_sandwiches = sandwich_orders.pop()
#
# print(finished_sanwiches.append(current_sandwiches))