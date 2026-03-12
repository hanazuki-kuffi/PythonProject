# analysis = ["STI_test", "gelmoscrin", "hpv23", "streptococcus agalactae", "d-flor", "candida.albicans"]
#
# print("Available lab tests")

# number = 1
# for test in analysis:
#
#     print(f"{number}. {test}")
#     number = number + 1



analysis = ["STI_test", "gelmoscrin", "hpv23", "streptococcus agalactae", "d-flor", "candida.albicans"]

print("Available lab tests")

for test, number in enumerate(analysis, 1):
    print(f"{test}. {number}")