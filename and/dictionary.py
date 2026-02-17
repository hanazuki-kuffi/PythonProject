# The following simple dictionary stores information about one specific alien
# The alien_0 dictionary stores two attributes: color and points. The following two print commands read this information from the dictionary and display it on the screen:
# alien_0 = {"colour": "Green", "points": 5}
#
# print(alien_0 ["colour"])
# print(alien_0 ["points"])

# alien_0 = {"colour": "green", "points": 5}
#
# new_points = alien_0["points"]
# print(f"You just earned {new_points} points!")

# alien_0 = {"colour": "green", "points": 5}
# print(alien_0)
#
# alien_0["x-position"] = 0
# alien_0["y-position"] = 25
# print(alien_0)

#Иногда удобно сначала создать пустой словарь, а потом постепенно добавлять в него данные.
#Sometimes it is convenient to first create an empty and then gradually add data to it.
# alien_0 = {}
#
# alien_0["colour"] = "green"
# alien_0["points"] = 5
#
# print(alien_0)

#first, the dictionary alien_0 is defined, wich contains only the alien colour: then the value associted with the key "colour" changed to "yellow"
# alien_0 = {"colour": "green"}
# print(f"The alien is {alien_0["colour"]}.")
#
# alien_0["colour"] = "yellow"
# print(f"The alien is now {alien_0["colour"]}.")


#CHANGING DICTIONARY VALUES
# alien_0 = {"x_position": 0, "y_position": 25, "speed": "fast"}
# print(f"Original x-position: {alien_0["x_position"]}")
#
# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# elif alien_0["speed"] == "fast":
#     x_increment = 3
# else:
#     x_increment = 4
#
# alien_0["x_position"] = alien_0["x_position"] + x_increment
# print(f"New x-position: {alien_0["x_position"]}")


# alien_0 = {"colour": "green", "points": 5}
# print(alien_0)
#
# LINE TELLS PYTHON TO REMOVE THE KEY 'POINTS' FROM THE ALIEN_O ALSO DELETE THE VALUE ASSOCIATED WITH THE KEY. THE OUTPUT SHOWS THAT THE KEY POINTS AT ITS VALUE 5 HAVE DISAPPEAREDFROM THE DICTIONARY, BUT THE REST OS THE DATA REMAINS UNCHANGED:
# del alien_0["points"]
# print(alien_0)

#PLEASE NOTE THAT DELETING                           alien_0["points"]
#A KEY-VALUE PAIR CANNOT BE UNDONE    print(alien_0)

# favorite_languages = {
#     "Jen": "python",
#     "Sarah": "c",
#     "Edward": "ruby",
#     "Phil": "python",
# }
#
# language1 = favorite_languages["Sarah"].title()
# print(f"Sarah is favorite language {language1}.")
#
# language2 = favorite_languages["Jen"].title()
# print(f"Jen is favorite language  {language2}.")
#
# language3 = favorite_languages["Edward"].title()
# print(f"Edward is favorite language {language3}.")
#
# language4 = favorite_languages["Phil"].title()
# print(f"Phil is favorite language {language4}.")

#ПЕРЕМЕННАЯ НИКОГДА НЕ НАЧИНАЕТСЯ С ЗАГЛАВНОЙ БУКВ ВСЕХ ЯЗЫКОВ ПРОГРАММИРОВАНИЯ

# alien_0 = {"colour": "green", "speed": "slow"}
# print(alien_0["points"])

# alien_0 = {"colour": "green", "speed": "slow"}
#
# point_value = alien_0.get("points", "No point value assigned!") # Если ключ существует — возвращает его значение, если нет — возвращает None или указанное значение по умолчанию. Это позволяет избежать ошибок при обращении к несуществующим ключам.
# print(point_value)                                              # Пример: user.get('name', 'Неизвестно') вернёт имя пользователя, а если ключа 'name' нет — вернёт 'Неизвестно'.


#human

# sister_07 = {
#     "first_name": "Nurailym",
#     "Last_name": "Dumankyzy",
#     "age": 19,
#     "city": "Satpayev",
# }
#
# print(sister_07["first_name"])
# print(sister_07["Last_name"])
# print(sister_07["age"])
# print(sister_07["city"])


# favorite_number = {
#     "Mother": 7,
#     "Sister": 28,
#     "MoaNoHosuto": 21,
#     "Kuffi": 45,
# }
#
# print(favorite_number["Mother"])
# print(favorite_number["Sister"])
# print(favorite_number["MoaNoHosuto"])
# print(favorite_number["Kuffi"])


user_0 = {
    "username": "kuffi.vv",
    "first": "gulaiym",
    "last": "zharylkassynova",
}

for key, value in user_0.items():
    print(f"\n key: {key}")
    print(f"value {value}")