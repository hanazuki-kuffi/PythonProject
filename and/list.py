# bicycles = ["trek", "cannondale", "redline", "specialized"]
# print(bicycles)
# from reprlib import aRepr
# from threading import main_thread
# from ctypes import c_char_p
# from ssl import socket_error

# bicycles = ["trek", "cannondale", "redline", "specialized"] # Список — упорядочённый набор. каждый элемент содержат свои индексы
# print(bicycles[0:4])   #Когда мы запрашиваем один элемент из списка, Python возвращает только этот элемент без квадратных скобок или кавычек:

# bicycles = ["trek", "cannondale", "redline", "specialized"] #Индексы начинаются с 0, а не с 1
# print(bicycles[0].title())

# bicycles = ["trek", "cannondale", "redline", "specialized"]
# print(bicycles[0].title())
# print(bicycles[3].title())

# bicycles = ["trek", "cannondale", "redline", "specialized"] #Фрагмент вернет значение 'specialized'. Этот синтаксис весьма полезен, потому что при работе со списками часто требуется обратиться к последним элементам, не зная точного количества элементов в списке.
# print(bicycles[-2])

# bicycles = ["trek", "cannondale", "redline", "specialized"]
# print(f"My first bicycle was a {bicycles[0].title()}")

# my_fruits = ["apple", "banana", "lime"]
# print(my_fruits)
#
# nummbers = [141, 245, 762, 123]
# print(nummbers)
#
# user_inputs = [True, 151, "🌸", 10.5]
# print(user_inputs)

# my_fruits = ["apple", "banana", "lime"]
#
# other_fruits = ["banana", "lime", "strawberry"]
#
# print(my_fruits == other_fruits) #False сразу в оутпуте выходит потому что ПОРЯДОК ЭЛЕМЕНТОВ В СПИСКЕ ИМЕЕТ ЗНАЧЕНИЕ

# empty_list = []
# print(len(empty_list)) #  в оутпуте выходит 0
#
# my_fruits = ["apple", "banana", "lime"]
# print(len(my_fruits)) # в оутпуте выходит 3
#
# posts_ids = [151, 141, 161, 171, 181]
# print(len(posts_ids))  # в  оутпуте выходиит 5
#
# user_inputs = [True, "🌸", 141, 10.5, "Hello World!"]
# print(len(user_inputs))  # тоже самое в оутпуте выходит 5
# posts_ids = [141, 151, 161, 171]
# print(posts_ids[0])
# print(posts_ids[1])
#
# print(posts_ids[-1])
# print(posts_ids[-2])


# names = ["mukhamedali", "nurailym", "arai", "zhalgas"]
# print(names[0].title())
# print(names[1].title())
# print(names[2].title())
# print(names[3].title())

# names = ["mukhamedali", "nurailym", "arai", "zhalgas"]
#
# print(f"Hello, {names[0].title()}!")
# print(f"Hello, {names[1].title()}!")
# print(f"Hello, {names[2].title()}!")
# print(f"Hello, {names[3].title()}!")


# transport = ["car", "bicycle", "bus", "bike"]
# print(f"I would like to buy {transport[0]} BYD")


# names = ["mukhamedali", "nurailym", "arai", "zhalgas"]
#
# for name in names:
#     print(name.title())

# motorcycles = ["suzuki", "honda", "yamato"]
# print(motorcycles)
#
# motorcycles[1] = "subaru"
# print(motorcycles)

# posts_ids = [151, 141, 161, 191, 201]
#
# posts_ids[0] = 555
# posts_ids[2] = 333
#
# print(posts_ids)

# user_inputs = [True, "🌸", 10.5, "kuffi"]
# print(user_inputs)
# print(len(user_inputs))
#
# del user_inputs[0]
# print(user_inputs)
# print(len(user_inputs))
#
# del user_inputs[-3]
# print(user_inputs)
# print(len(user_inputs))
#
# users = [
#     {
#         "user_id": 131,
#         "user_name": "Ali"
#     },
#     {
#         "user_id": 151,
#         "user_name": "Gul"
#     }
# ]
#
# print(len(users))
# print(users[0]["user_id"])
#
# my_fruits = "banana"
# other_fruits = "apple"
# new_fruits = "lime"
#
# all_fruits = [my_fruits,other_fruits,new_fruits]
#
# print(all_fruits)
#
# happy_smiles = []
#
# happy_smiles.append("🌸") #append добавление новых элементов
# happy_smiles.append("🌺")
# happy_smiles.append("🌷")
# happy_smiles.append("🌹")
#
# print(happy_smiles)
# print(len(happy_smiles))
#
# inputs = [True, "🌸", "kuffi", 10.5]
#
# inputs.pop()  #Без индекса — удаляет последний элемент:
# print(inputs) # удалит 10.5
#
# inputs.pop(0) #С индексом — удаляет элемент по позиции:
# print(inputs) # удалит первый элемент
#
# removed_element = inputs.pop() #Главная фишка — удалённый элемент можно сохранить:
# print(removed_element)        # удалили И сохранили   # можно использовать дальше

# motorcycles = ["honda", "suzuki", "ducati"]
# print(motorcycles)
#
# motorcycles.append("yamaha")
# print(motorcycles)

# motorcycles = []
#
# motorcycles.append("honda")
# motorcycles.append("suzuki")
# motorcycles.append("yamaha")
# motorcycles.append("ducati")
#
# print(motorcycles)

# motorcycles = ["honda", "ducati", "yamato", "suzuki"]
# print(motorcycles)
#
# motorcycles.insert(1, "subaru") #Вставка элементов в список
# print(motorcycles)

# motorcycles = ["honda", "ducati", "suzuzki", "yamaha"]
# print(motorcycles)
#
# del motorcycles[-3] #Команда del позволяет удалить элемент из любой позиции списка, если вам известен его индекс.
# print(motorcycles)  #В обоих примерах значение, удаленное из списка после использования команды del, становится недоступным.

# posts_ids = [121, 147, 190, 151, 245]
# print(posts_ids)
#
# posts_ids.sort()
# print(posts_ids)
#
# posts_ids.sort(reverse=True) # методика по убыванию элемента
# print(posts_ids)

# greeting = "Hello from Python!" #КОНВЕРТАЦИЯ В СПИСОК НУ ТОЧНЕЕ СЛОВАРЬ КОНВЕНТИРОВАТЬ В СПИСОК
# greeting_letters = list(greeting)
# print(greeting_letters)
# #['H', 'e', 'l', 'l', 'o', ' ', 'f', 'r', 'o', 'm', ' ', 'P', 'y', 't', 'h', 'o', 'n', '!']
#
# my_dict = {"a": 10, "b": True}
# my_dict_keys = list(my_dict)
# print(my_dict_keys)
#['a', 'b']

#
# ratings = [2.5, 5.0, 4.3, 3.7]
#
# print(min(ratings))
# print(max(ratings))
# print(sum(ratings))

# result = sum(ratings) / len(ratings)
# print(result)

# print(sum(ratings) / len(ratings))

# motocycles = ["honda", "suzuki", "yamaha"]
# print(motocycles) #Сначала в точке  определяется и выводится содержимое списка motorcycles.
#
# popped_motocycles = motocycles.pop() #В точке  значение извлекается из списка и сохраняется в переменной с именем popped_motorcycle.
# print(motocycles) # Вывод измененного списка в точкепоказывает, что значе- ние было удалено из списка.
# print(popped_motocycles) #Затем мы выводим извлеченное значение в точке, демонстрируя, что удаленное из списка значение остается доступным в программе.

#Из вывода видно, что значение 'suzuki', удаленное в конце списка, теперь хранится в переменной popped_motorcycle:
# ['honda', 'suzuki', 'yamaha']
# ['honda', 'suzuki']
# yamaha

# motocycles = ["honda", "yamaha", "suzuki"]
#
# last_owned = motocycles.pop()
# print(f"The last motocycle I owned was a {last_owned.title()}! ")

# motocycles = ["suzuki", "honda", "yamaha"]
#
# first_motocycles = motocycles.pop(0)
# print(f"The first motocycle I owned was a {first_motocycles.title()}!")

#Помните, что после каждого вызова pop() элемент, с которым вы работаете, уже
#не находится в списке.

#если вы собираетесь просто удалить элемент из списка, никак не используя его, выбирайте команду del; если же вы намерены использовать элемент после удаления из списка, выбирайте ме- тод pop().

# motocycles = ["honda", "yamaha", "suzuki", "ducatti"]
# print(motocycles)
#
# motocycles.remove("ducatti")
# print(motocycles)


# my_ratings = [2.5, 4.5, 2.8, 6.5] #Обьеденение списков
# other_ratings = [3.5, 5.5]
#
# all_ratings = my_ratings + other_ratings
# print(all_ratings) #При использований оператора + вызывается метод списков ___add___

# ratings = [2.5, 5.0, 4.3, 3.7, 4.5]
#
# first_two_ratings = ratings[:2]
# print(first_two_ratings) #[2.5, 5.0]
#
# middle_ratings = ratings[1:-1]
# print(middle_ratings) #[5.0, 4.3, 3.7]
#
# last_two_ratings = ratings[-2:]
# print(last_two_ratings) #[3.7, 4.5]


# motocycles = ["honda", "yamaha", "suzuki", "ducati"]
# print(motocycles)
#
# motocycles.remove("ducati")
# print(motocycles)


# motocycles = ["honda", "yamaha", "suzuki", "ducati"]
# print(motocycles)
#
# too_expensive = "ducati" # Мы создали переменную для того что бы присваивать ответ " A Ducati is too expensive for me!"
# motocycles.remove(too_expensive) # здесь мы убрали из фильтра якобы такой дукати в рограмме
# print(motocycles)
#
# print(f"\n A {too_expensive.title()} is too expensive for me!") \n функ отвечает начать операцию с нового и отдельного абзаца

# ['honda', 'yamaha', 'suzuki', 'ducati']
# ['honda', 'yamaha', 'suzuki']
#
#  A Ducati is too expensive for me!




#КОПИРОРВАНИЕ СПИСКА
# ВАРИАНТ 1 ТУТ МЫ НАПИСАЛИ И КОПИРОВАЛИ ОРИГИНАЛ И ВЫВЕЛИ В ОУТПУТ
# my_cars = ["BMW", "Mercedes"]
#
# copied_cars = my_cars # этот метод называется копирование по ссылкам
#
# copied_cars.append("BYD")
#
# print(copied_cars) #['BMW', 'Mercedes', 'BYD']
# print(my_cars)     #['BMW', 'Mercedes', 'BYD']
# print(id(my_cars) == id(copied_cars))  #True

#ВАРИАНТ 2 ТУТ МЫ НАПИСАЛИ И ИСПОЛЬЗОВАЛИ ОТРЕЗКА ЧТОБ НЕ ТРОГАТЬ НА ОРИГИНАЛ
# my_cars = ["BMW", "Mercedes"]
#
# copied_cars = my_cars[:] #<---- создание нового списка используя slice [кусочек]
#
# copied_cars.append("BYD")
#
# print(copied_cars) #['BMW', 'Mercedes', 'BYD']
# print(my_cars)     #['BMW', 'Mercedes']
#
# print(id(copied_cars) == id(my_cars)) #False
#
# #ВАРИАНТ 3 ТУТ МЫ БУДЕМ ИСПОЛЬЗОВАТЬ .copy()

# my_cars = ["BMW", "Mercedes"]
#
# copied_cars = my_cars.copy() # Создание нового списка используя метод ".copy()"
#
# copied_cars.append("BYD")
#
# print(copied_cars) # ['BMW', 'Mercedes', 'BYD']
# print(my_cars)     # ['BMW', 'Mercedes']
#
# print(id(copied_cars) == id(my_cars)) #False

#ВАРИАНТ 4 НОВОГО СПИСКА ИСПОЛЬЗУЯ ВСТРОЕННЫЙ ФУНКЦИЮ "list()"

# my_cars = ["BMW", "Mercedes"]
#
# copied_cars = list(my_cars)
#
# copied_cars.append("BYD")
#
# print(copied_cars)
# print(my_cars)
#
# print(id(copied_cars) == id(my_cars))


#VARIANT NUMBER 1 FROM LIST
# invitation = ["Nurai", "Kawai", "Arai"]
#
# print(f"{invitation[0].title()}, I will invite you")
# print(f"{invitation[1].title()}, I will invite you")
# print(f"{invitation[2].title()}, I will invite you")
# print(f"\n {invitation[2]} won't be able to come to visit.")
#
# invitation[2] = "Alima"
# print(invitation)
#
# for person in invitation:
#     print(f"{person}, I will invite you")
#
# print(f"\n !!! EXPANSION COMING SOON!!!")
#
# invitation.insert(0, "Ali")
# invitation.insert(2, "Zhalgas")
# invitation.append("Abdulla")
#
# print(invitation)
#
# for friend in invitation:
#     print(f"{friend}, I will invite you!")
#
#
# print("\n ONLY TWO GUESTS ARE INVITED TO DINNER!!! ")
#
# print(invitation)
# popped_guests1 = invitation.pop()
# print(f"{popped_guests1},I regret canceling the invitation 😅! ")
#
# popped_guests2 = invitation.pop()
# print(f"{popped_guests2},I regret canceling the invitation 😅! ")
#
# popped_guests3 = invitation.pop()
# print(f"{popped_guests3},I regret canceling the invitation 😅! ")
#
# popped_guests4 = invitation.pop()
# print(f"{popped_guests4},I regret canceling the invitation 😅! ")
#
#
# for special_guests in invitation:
#     print(f"\n {special_guests}, your invitation still stands ☺️!")
#
# del invitation[0]
# del invitation[0] # здесь играет роль последовательности каароче После первого удаления список сдвигается, поэтому второй элемент снова становится [0].
# print(invitation)
#
# print(len(invitation))

#
# cars = ["bmw", "toyota", "audi", "subaru"]
#
# cars.sort() # сортирует по алфавитом и вернуться к ис- ходному порядку уже не удастся:
# print(cars) # ['audi', 'bmw', 'subaru', 'toyota']


# cars = ["bmw", "toyota", "audi", "subaru"]
#
# cars.sort(reverse=True) #Список также можно отсортировать в обратном алфавитном порядке; для этого методу sort() следует передать аргумент reverse=True. В следующем примере список сортируется в порядке, обратном алфавитному:
# print(cars)  #['toyota', 'subaru', 'bmw', 'audi']



# cars: list[str] = ["bmw", "subaru", "audi", "toyota"]
#
# print(f"\n Here is the original list: ")
# print(cars) #['bmw', 'subaru', 'audi', 'toyota']
#
# print(f"\n Here is the sorted list: ")  # Функция sorted() позволяет представить список в определенном порядке, но не изменяет фактический порядок элементов в списке.
# print(sorted(cars)) #['audi', 'bmw', 'subaru', 'toyota']
#
# print(f"\n Here is the original cars again: ")
# print(cars) #['bmw', 'subaru', 'audi', 'toyota']

#Сначала список выводится в исходном порядке, а затем в алфавитном порядке.
#После того как список будет выведен в новом порядке, в точкемы убеждаемся
#в том, что список все еще хранится в исходном порядке.


# cars = ["audi", "BMW", "subaru", "toyota"]
# print(cars) #['bmw', 'audi', 'toyota', 'subaru']
#
# cars.reverse() #Обратите внимание: метод reverse() не сортирует элементы в обратном алфавит- ном порядке, а просто переходит к обратному порядку списка:
# print(cars) #['subaru', 'toyota', 'audi', 'bmw']
#
# cars.reverse() #Метод reverse() осуществляет постоянное изменение порядка элементов, но вы можете легко вернуться к исходному порядку, снова применив reverse() к обрат- ному списку.
# print(cars) #['audi', 'BMW', 'subaru', 'toyota']
#
# cars = ["audi", "BMW", "subaru", "toyota"]
# print(len(cars))


#TASKS NUMBER 2

# country_5 = ["Japan",  "Korea", "Iceland", "USA", "Switzerland"]
# print(country_5)
#
# # country_5 = sorted(country_5)
# # print(country_5) #type number 1
#
# print(sorted(country_5)) #type number 2
#
# print(country_5)
#
# print(sorted(country_5, reverse=True))
#
# print(country_5)
#
# country_5.reverse()
# print(country_5)
#
# country_5.reverse()
# print(country_5)
#
# country_5.sort()
# print(country_5)
#
# country_5.sort(reverse=True)
# print(country_5)
# sorted(country_5, reverse=True)
# print(country_5)
#
# country_5.sort()
# print(country_5)
#
# country_5.sort(reverse=True)
# print(country_5)


# my_favorite_place = ["Fudji", "Japan", "Amazon", "Okinawa", "Spanish"]
#
# city = my_favorite_place.pop(1)
# print(f"My favorite city is {city}!")
#
# my_favorite_place.append("Ramen")
# print(my_favorite_place)
#
# my_favorite_place.sort()
# print(my_favorite_place)
#
# my_favorite_place.sort(reverse=True)
# print(my_favorite_place)
#
# print(sorted(my_favorite_place))
#
# print(sorted(my_favorite_place, reverse=True))
#
# print(len(my_favorite_place))
#
# my_favorite_place.insert(1, "Kimano")
# print(my_favorite_place)
#
#
# my_favorite_place.remove("Spanish")
# print(my_favorite_place)
#
# print(my_favorite_place[4])
#
#
# del my_favorite_place[0:6]
# print(my_favorite_place)
# print(my_favorite_place[-1])




# my_nums = [1, 3, 3, 67, 78, 34]

# result = my_nums.count(3) #метод .count() найдет в списке элемент который сколько раз встречался и выводит число сколько раз вышло этот элемент
# print(result)
#
# my_nums.append(35) # метод .append() добавляет элемент в конце списка
# print(my_nums)
#
# my_nums.insert(0, 4) #тоже такая методика для добавления элемента но для этого нужно учитывать такой условия как это
# print(my_nums)                       # сперва перед добавления какого то эдемента нужно написать индекс элемента и после запятой можно написать элемент
#
#
# my_nums.clear()
# print(my_nums)
#
# my_nums.extend("avfd")
# print(my_nums)


# my_nums = [1, 3, 3, 67, 78, 34]
#
# # other_nums = my_nums
# #
# # print(id(my_nums))
# # print(id(other_nums))
#
# # other_nums = my_nums.copy()
# # other_nums = my_nums[:]
# # other_nums = list(my_nums)
#
# my_nums.append(55)
# # other_nums.clear()
#
# # print(id(my_nums))
# # print(id(other_nums))
# #
# # print(my_nums, other_nums)
#
# print(len(my_nums))



#TASKS NUMBER 1

# artefact = [45, 53, "Arigatoo", 65, 76] # создать список содержится 5 элементов
#
# artefact.pop(2)    # удалить 3-й элемент
# print(artefact)
# print(len(artefact)) # выводим длину списка в терминале
#
# # artefact.sort(reverse=True)
# print(artefact)
#
# new_artefact = [-8, -6]
# print(new_artefact)
#
#
# artefact.extend(new_artefact)   # .extend() этот метод помодет обьединит и расширить список например вот так
# print(artefact)


#TASKS NUMBER 2

# list_1 = ["qwerty", "abc", 123]
# list_2 = ["zxcv", "plm", 456]
#
# all_list_1 = list_1 + list_2
# print(all_list_1)
#
# all_list_2 = list_1.__add__(list_2)
# print(all_list_2)
#
# list_1.extend(list_2)
# print(list_1)

#
# magicians = ["germionna", "harry potter", "tom chrismos", "alice", "carolina"]
# # # for magician in magicians:
# # #     print(magician.title())
# #
# # # for magician in magicians:
# # #     print(f"{magician.title()}, that was a great trick!")
# #
# # for magician in magicians:
# #     print(f"{magician.title()}, that was a great trick!")
# #     print(f"I can not wait to see your next trick {magician.title()}. \n")
#
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can not wait to see your next trick {magician.title()} \n")
#
# print("Thank you everyone. That was a great magic show!")

#
# my_favorite_pizza = ["Italian Margarrita", "pepperoni", "chicken pizza"]
#
# for pizza in my_favorite_pizza:
#     print(f"I like {pizza} pizza")
#
# print("\nI really love pizza!")


animals = ["wolf", "fox", "tiger"]

for animal in animals:
    print(f"A {animal} would make a great pet")

print("\nAny of these animals would make a great pet!")





