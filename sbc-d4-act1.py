list = []
while len(list) < 5:
    add = str(input(f"Enter Number: "))
    list.append(add)
print(list)
while True:
        choice = input("Enter naa or wala: ")
        if choice == "naa":
            add_delete = input("Enter add or delete: ")
            if add_delete == "add":
                add_number = input("Enter Number: ")
                list.append(add_number)
            elif add_delete == "delete":
                list.pop(0)
        elif choice == "wala":
           list.pop(-1)   
        else:
           print("Invalid")
        print(f"The list is: {list}")