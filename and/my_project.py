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


# barcode_patients= ["202504", "302643", "505678", "343235", "414754", "354890"]
#
# ct_channels = ["FAM", "HEX", "ROX", "CY5", "CY5.5"]
#
# ct_results1 = [None, 22.40, None, 28.5, None]
#
#
# # FOR 1 PATIENT
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


#FOR SOME PATIENT

# barcode_patients = ["202504", "302643", "505678", "343235", "414754", "354890"]
# 
# ct_channels = ["FAM", "HEX", "ROX", "CY5", "CY5.5"]
# 
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










#
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



patient_order_quantity = [39, 39, 47, 55, 14, 36, 34]
name_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

max_order_quantity = max(patient_order_quantity)
print(max_order_quantity)

index_order_quantity = patient_order_quantity.index(max_order_quantity)
print(index_order_quantity)

name_of_day = name_of_days[index_order_quantity]
print(name_of_day)

print(f"Busiest day: {name_of_day} with {max_order_quantity} ordered patients.")

min_order_quantity = min(patient_order_quantity)
print(min_order_quantity)

index_order_quantity1 = patient_order_quantity.index(min_order_quantity)
print(index_order_quantity1)

name_of_day1 = name_of_days[index_order_quantity1]
print(name_of_day1)


print(f"Easiest day: {name_of_day1} with {min_order_quantity} patients!")




