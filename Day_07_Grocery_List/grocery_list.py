grocery_list = []
while True:
    print("Press 1 to Add Item")
    print("Press 2 to View List")
    print("Press 3 to Exit")
    option=int(input("Enter your option: "))
    if option == 1:
        add = input("What to add?")
        grocery_list.append(add)
    elif option == 2:
        for i in grocery_list:
            print(i)
    else:
        break

