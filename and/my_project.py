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
#
# if cycle_threshold1 == " " or cycle_threshold1 == "  ":
#     print("Negative")
# elif 18 <= int(cycle_threshold1) <= 35:
#     print("Positive")
# elif 18 > int(cycle_threshold1) or 35 < int(cycle_threshold1):
#     print("Invalid")


barcode_patients= ["202504", "302643", "505678", "343235", "414754", "354890"]

ct_channels = ["FAM", "HEX", "ROX", "CY5", "CY5.5"]

ct_results = [None, 22.40, None, 28.5, None]

index = 0
for channel in ct_channels:
    print(channel, ct_results[index])
    index = index + 1