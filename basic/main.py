my_list =   []
while True:
    print("/n -- List Making App --")
    print("1. Add an item ")
    print("2. Remove an item")
    print("3. Display the list")
    print("4. Undo previous changes")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter an item to add: ")
        previous_list = my_list.copy()
        my_list.append(item)
        print("Item added successfully!")

    elif choice == "2":
        if len(my_list) == 0:
            print("Your list is empty!")
        else:
            for index in range(len(my_list)):
                print(index, "-", my_list[index])

            remove_index = int(input("Enter the index to remove: "))
            previous_list = my_list.copy()
            my_list.pop(remove_index)

            print("Item removed successfully!")

    elif choice == "3":
        if len(my_list) == 0:
            print("Your list is empty!")
        else:
            print("\nYour List:")
            for index in range(len(my_list)):
                print(index, "-", my_list[index])

    elif choice == "4":
        my_list = previous_list.copy()
        print("Previous change undone!")

    elif choice == "5":
        print("Thank you for using the List Making App!")
        break

    else:
        print("Invalid choice. Please try again.")