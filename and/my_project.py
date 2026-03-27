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











barcode_patients = [202504, 305463, 202552, 505508, 604125, 505123, 202654, 414506]

ct_channels = ["FAM", "HEX", "ROX", "CY5", "CY5.5"]

ct_results = [
    [28.11, 29.11, 30.67, 29.00, None],
    [None, None, None, 28.11, None],
    [29.91, None, 28.66, 41.00, None],
    [None, None, None, 29.95, None],
    [None, 34.95, None, 29.95, None],
    [36.00, None, None, 25.89, None],
    [None, None, None, 32.95, None],
    [None, None, None, 29.91, None]

]

patient_index = 0

for patient in ct_results:
    print(f"\n Patient: {barcode_patients[patient_index]}")

    index = 0
    for channel in ct_channels:

        cycle_threshold = patient[index]

        if cycle_threshold == None:
            print(f"{channel}: Negative")
        elif 18 <= cycle_threshold <= 35:
            print(f"{channel}: Positive")
        elif 18 > cycle_threshold or cycle_threshold > 35:
            print(f"{channel}: Invalid")

        index += 1
    patient_index += 1


barcode_patients.append(707890)
print(barcode_patients)

ct_results.append([None, 31.5, None, 28.0, None])
print(ct_results)

print("\n New patient 707890 added to the system")

print(f"\n Patient {barcode_patients[-1]} has cancelled their test")

barcode_patients.pop()
print(barcode_patients)

ct_results.pop(-1)
print(ct_results)


print("Results updated for patient 202552")

ct_results[2] = [31.0, 29.5, 28.0, 27.5, None]
print(ct_results)
