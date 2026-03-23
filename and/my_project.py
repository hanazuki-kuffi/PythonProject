# analysis = ["STI_test", "gelmoscrin", "hpv23", "streptococcus agalactae", "d-flor", "candida.albicans"]
#
# print("Available lab tests")

# number = 1
# for test in analysis:
#
#     print(f"{number}. {test}")
#     number = number + 1


# analysis = ["STI_test", "gelmoscrin", "hpv23", "streptococcus agalactae", "d-flor", "candida.albicans"]
#
# print("Available lab tests")
#
# for test, number in enumerate(analysis, 1):
#     print(f"{test}. {number}")


# PROJECT №1

# cycle_threshold1 = input("enter a number: ")

# if cycle_threshold1 == " " or cycle_threshold1 == "  ":
#     print("Negative")
# elif 18 <= int(cycle_threshold1) <= 35:
#     print("Positive")
# elif 18 > int(cycle_threshold1) or 35 < int(cycle_threshold1):
#     print("Invalid")


barcode_patients= ["202504", "302643", "505678", "343235", "414754", "354890"]

ct_channels = ["FAM", "HEX", "ROX", "CY5", "CY5.5"]

ct_results1 = [None, 22.40, None, 28.5, None]


# FOR 1 PATIENT
# print(f"Patient: {barcode_patients[0]}")
# index = 0
# for channel in ct_channels:
#     cycle_threshold = ct_results[index]
#
#     if cycle_threshold == None:
#         print(f"{channel}: Negative")
#     elif 18 <= cycle_threshold <= 35:
#         print(f"{channel}: Positive")
#     elif cycle_threshold < 18 or cycle_threshold > 35:
#         print(f"{channel}: Invalid")

    # index = index + 1


#FOR SOME PATIENT

# barcode_patients= ["202504", "302643", "505678", "343235", "414754", "354890"]
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
#     print(f"Patient: {barcode_patients[patient_index]}")
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
