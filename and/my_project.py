# analysis = ["STI_test", "gelmoscrin", "hpv23", "streptococcus agalactae", "d-flor", "candida.albicans"]
#
# print("Available lab tests")
#
# number = 1
# for test in analysis:
#
#     print(f"{number}. {test}")
#     number = number + 1
#
#
# analysis = ["STI_test", "gelmoscrin", "hpv23", "streptococcus agalactae", "d-flor", "candida.albicans"]
#
# print("Available lab tests")
#
# for test, number in enumerate(analysis, 1):
#     print(f"{test}. {number}")
#
#
# PROJECT №1
#
# cycle_threshold1 = input("enter a number: ")
#
# if cycle_threshold1 == " " or cycle_threshold1 == "  ":
#     print("Negative")
# elif 18 <= int(cycle_threshold1) <= 35:
#     print("Positive")
# elif 18 > int(cycle_threshold1) or 35 < int(cycle_threshold1):
#     print("Invalid")
# from wsgiref.validate import check_iterator
#
# barcode_patients = ["202504", "302643", "505678", "343235", "414754", "354890"]
#
# ct_channels = ["FAM", "HEX", "ROX", "CY5", "CY5.5"]
#
# ct_results1 = [None, 22.40, None, 28.5, None]


# FOR 1 PATIENT
# print(f"Patient: {barcode_patients[0]}")
# index = 0
# for channel in ct_channels:
#     cycle_threshold = ct_results1[index]
#
#     if cycle_threshold == None:
#         print(f"{channel}: Negative")
#     elif 18 <= cycle_threshold <= 35:
#         print(f"{channel}: Positive")
#     elif cycle_threshold < 18 or cycle_threshold > 35:
#         print(f"{channel}: Invalid")
#
#     index = index + 1


# FOR SOME PATIENTS

# barcode_patients = ["202504", "302643", "505678", "343235", "414754", "354890"]
#
# ct_channels = ["FAM", "HEX", "ROX", "CY5", "CY5.5"]

# ct_results2 = [
#     [29.51, 28.5, 28.11, 33.0, 28.79],
#     [None, 23.95, None, 28.66, None],
#     [28.18, None, None, 27.00, None],
#     [None, None, None, 27.00, None],
#     [None, None, None, 27.00, 33.9],
#     [None, 24.00, None, 27.00, None]
# ]
#
# patient_index = 0
# for patient in ct_results2:
#     print(f"\n Patient: {barcode_patients[patient_index]}")
#
#     index = 0
#     for channel in ct_channels:
#
#         cycle_threshold = patient[index]
#
#         if cycle_threshold == None:
#             print(f"{channel}: Negative")
#         elif 18 <= cycle_threshold <= 35:
#             print(f"{channel}: Positive")
#         elif cycle_threshold < 18 or cycle_threshold > 35:
#             print(f"{channel}: Invalid")
#
#         index += 1
#     patient_index += 1











# barcode_patients = [202504, 305463, 202552, 505508, 604125, 505123, 202654, 414506]
#
# ct_channels = ["FAM", "HEX", "ROX", "CY5", "CY5.5"]
#
# ct_results = [
#     [28.11, 29.11, 30.67, 29.00, None],
#     [None, None, None, 28.11, None],
#     [29.91, None, 28.66, 41.00, None],
#     [None, None, None, 29.95, None],
#     [None, 34.95, None, 29.95, None],
#     [36.00, None, None, 25.89, None],
#     [None, None, None, 32.95, None],
#     [None, None, None, 29.91, None]
#
# ]
#
#
# patient_index = 0
#
# positive_count = 0
# negative_count = 0
# invalid_count = 0
#
# for patient in ct_results:
#     print(f"\n Patient: {barcode_patients[patient_index]}")
#
#     index = 0
#     for channel in ct_channels:
#
#         cycle_threshold = patient[index]
#
#         if cycle_threshold == None:
#             print(f"{channel}: Negative")
#             negative_count += 1
#         elif 18 <= cycle_threshold <= 35:
#             print(f"{channel}: Positive")
#             positive_count += 1
#         elif 18 > cycle_threshold or cycle_threshold > 35:
#             print(f"{channel}: Invalid")
#             invalid_count += 1
#
#         index += 1
#     patient_index += 1
# #
#
# print("\n === SUMMARY ===")
# print(f"Total patients: {len(barcode_patients)}")
# print(f"Total positive: {positive_count}!")
# print(f"Total Negative: {negative_count}!")
# print(f"Total Invalid: {invalid_count}!")
# #
# barcode_patients.append(707890)
# print(barcode_patients)
#
# ct_results.append([None, 31.5, None, 28.0, None])
# print(ct_results)
#
# print("\n New patient 707890 added to the system")
#
# print(f"\n Patient {barcode_patients[-1]} has cancelled their test")
#
# barcode_patients.pop()
# print(barcode_patients)
#
# ct_results.pop(-1)
# print(ct_results)
#
#
# print("Results updated for patient 202552")
#
# ct_results[2] = [31.0, 29.5, 28.0, 27.5, None]
# print(ct_results)

#
# print("\n Patients sorted by barcode")
# print(sorted(barcode_patients))
#
# print("\n Patients in reverse order")
# print(sorted(barcode_patients, reverse=True))
#
#
# print("\n Patients sorted by barcode")
# barcode_patients.sort()
# print(barcode_patients)
#
# print("\n Patients in reverse order")
# barcode_patients.reverse()
# print(barcode_patients)
#
#
# barcode = int(input("Enter barcode: "))
#
# if barcode in barcode_patients:
#     print(f"Patient {barcode} found in the system")
# else:
#     print(f"Patient {barcode} not found")


#
# patient_order_quantity = [39, 39, 47, 55, 14, 36, 34]
# name_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#
# max_order_quantity = max(patient_order_quantity)
# print(max_order_quantity)
#
# index_order_quantity = patient_order_quantity.index(max_order_quantity)
# print(index_order_quantity)
#
# name_of_day = name_of_days[index_order_quantity]
# print(name_of_day)
#
# print(f"Busiest day: {name_of_day} with {max_order_quantity} ordered patients.")
#
# min_order_quantity = min(patient_order_quantity)
# print(min_order_quantity)
#
# index_order_quantity1 = patient_order_quantity.index(min_order_quantity)
# print(index_order_quantity1)
#
# name_of_day1 = name_of_days[index_order_quantity1]
# print(name_of_day1)
#
#
# print(f"Easiest day: {name_of_day1} with {min_order_quantity} patients!")





# barcode_patients.append(707890)
# print(barcode_patients)
#
# ct_results2.append([None, 31.5, None, 28.0, None])
# print(ct_results2)
#
# print("\n New patient 707890 added to the system")
#
# print(f"\n Patient {barcode_patients[-1]} has cancelled their test")
#
# barcode_patients.pop()
# print(barcode_patients)
#
# ct_results2.pop(-1)
# print(ct_results2)
#
#
# print("Results updated for patient 202552")
#
# ct_results2[2] = [31.0, 29.5, 28.0, 27.5, None]
# print(ct_results2)
# #
# barcode_patients = ["202504", "302643", "505678", "343235", "414754", "354890"] #список пациента
#
# ct_channels = ["FAM", "HEX", "ROX", "CY5", "CY5.5"] #список каналов
#
# ct_results2 = [                                  #cписок результатов
#                                                  #Это список списков. Каждый пациент — это отдельный список из 5 значений внутри большого списка.
#     [29.51, 28.5, 28.11, 33.0, 28.79],
#     [None, 23.95, None, 28.66, None],
#     [28.18, None, None, 27.00, None],
#     [None, None, None, 27.00, None],
#     [None, None, None, 27.00, 33.9],
#     [None, 24.00, None, 27.00, None]
# ]
#
#
# while True:
#     print("--- PCR LAB MENU ---")
#     print("1. Show all patients")
#     print("2. Add new patient")
#     print("3. Delete patient")
#     print("4. Exit")
#     choice = (input("Choose action (1/2/3/4): "))
#
#     if choice == "1":
#         patient_index = 0
#         for result in ct_results2:
#             print(f"\n Patient: {barcode_patients[patient_index]}")
#
#             index = 0
#             for channel in ct_channels:
#
#                 cycle_threshold = result[index]
#
#                 if cycle_threshold == None:
#                     print(f"{channel}: Negative")
#                 elif 18 <= cycle_threshold <= 35:
#                     print(f"{channel}: Positive")
#                 elif cycle_threshold < 18 or cycle_threshold > 35:
#                     print(f"{channel}: Invalid")
#
#                 index += 1
#             patient_index += 1
#     elif choice == "2":
#         new_barcode_patient = input("Enter a barcode patient: ")
#         fam = input("Enter FAM value (or 'none'): ")
#         hex = input("Enter HEX value (or 'none'): ")
#         rox = input("Enter ROX value (or 'none'): ")
#         cy5 = input("Enter CY5 value (or 'none'): ")
#         cy55 = input("Enter CY5.5 value (or 'none'): ")
#
#         # fam = "28.5"  # пользователь ввёл текст "28.5"
#         # fam = float(fam)  # говоришь float: "возьми fam и сделай число"
#         # # теперь fam = 28.5  ← настоящее число, не текст
#
#         if fam == "none":
#             fam = None
#         else:                #float() — это функция которая конвертирует текст в число. Но ей нужно сказать что именно конвертировать.
#             fam = float(fam) #float() без аргумента внутри не знает что конвертировать! Нужно передать переменную:
#         if hex == "none":
#             hex = None
#         else:
#             hex = float(hex) #float() без аргумента внутри не знает что конвертировать! Нужно передать переменную:
#         if rox == "none":
#             rox = None
#         else:
#             rox = float(rox) #float() без аргумента внутри не знает что конвертировать! Нужно передать переменную:
#         if cy5 == "none":
#             cy5 = None
#         else:
#             cy5 = float(cy5) #float() без аргумента внутри не знает что конвертировать! Нужно передать переменную:
#         if cy55 == "none":
#             cy55 = None
#         else:
#             cy55 = float(cy55) #float() без аргумента внутри не знает что конвертировать! Нужно передать переменную:
#         barcode_patients.append(new_barcode_patient)
#         ct_results2.append([fam, hex, rox, cy5, cy55]) #Ты сначала собираешь 5 значений в один список [...], и потом добавляешь этот список как одного пациента. Структура сохраняется.
#                                                        #Каждый пациент — это отдельный список из 5 значений внутри большого списка.
#         print(f"Patient {new_barcode_patient} added successfully!")
#     elif choice == "3":
#         delete_patients = input("Enter the barcode to delete: ")
#         index_1 = 0
#         for patient in barcode_patients:
#             if patient == delete_patients:
#                 barcode_patients.pop(index_1)
#                 ct_results2.pop(index_1)
#                 print(f"Patient {patient} deleted!")
#                 break
#             index_1 = index_1 + 1
#         else:
#             print("The barcode not found")
#     elif choice == "4":
#         break
#     else:
#         print("Invalid choice. Try again!")

