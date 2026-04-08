# name = input("Please enter your name: ")
# print(f"Hello {name}!\n")
# from http.cookiejar import user_domain_match
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

current_number = 0

while current_number < 10:
    current_number = current_number + 1

    if current_number % 2 == 0:
        continue
    print(current_number)
