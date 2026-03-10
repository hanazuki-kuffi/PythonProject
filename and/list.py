# bicycles = ["trek", "cannondale", "redline", "specialized"]
# print(bicycles)

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
