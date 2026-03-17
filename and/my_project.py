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

cycle_threshold1 = input("enter a number: ")

if cycle_threshold1 == " " or cycle_threshold1 == "  ":
    print("Negative")
elif 18 <= int(cycle_threshold1) <= 35:
    print("Positive")
elif 18 > int(cycle_threshold1) or 35 < int(cycle_threshold1):
    print("Invalid")

# barcode_patient = [209399, 209134, 417619, 312910, 417585, 209402, 209364]

barcode_patient1 = ["209399"]
ct_patient = [
    [None, None, 33.1, 28, None] #[NG, CT, MG, IC, TV]
]

for 

