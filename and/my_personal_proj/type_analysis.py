while True:
    print("\nType analysis:")
    print()
    print("1. NG, CT, MG, TV")
    print("2. Candida.albicans")
    print("3. D-Bioflor")
    print("4. HPV-23")
    print("5. HPV-18")
    print("6. Gelmo-screen")
    print("7. Proto-screen")
    print("8. Streptococcus agalactae")
    print("9. Exit")

    choice = input("\nChoose one of the following assay: ")

    if choice == "1":
        print("Type analysis: NG, CT, MG, TV")

        while True:
            print("\nType biomaterials: ")
            print()
            print("1. Swamp")
            print("2. Urine")
            print("3. Sperm")
            print("4. Blood")
            print()
            type_biomaterials = input("Choose one of the following biomaterials: ")

            if (not type_biomaterials == "1"
                    and type_biomaterials == "2"
                    and type_biomaterials == "3"
                    and type_biomaterials == "4"):
                print("Unknown biomaterial, please try again!")

            elif type_biomaterials == "1":
                print("Start assay!")

    elif choice == "9":
        break
    else:
        print("Your choice invalid, please try again!")










