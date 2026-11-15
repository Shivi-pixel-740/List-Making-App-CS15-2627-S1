my_list = []
completed_list = []
previous_list = my_list.copy()
previous_completed_list = completed_list.copy()
while True:
    print("\n--- TO-DO LIST APP ---")
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display a List")
    print("4. Undo Previous Change")
    print("5. Replace an Item")
    print("6. Check Off an Item")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter an item to add: ")

        previous_list = my_list.copy()
        previous_completed_list = completed_list.copy()

        my_list.append(item)

        print("Item added successfully!")

    elif choice == "2":
        if len(my_list) == 0:
            print("Your list is empty!")
        else:
            for index in range(len(my_list)):
                print(index, "-", my_list[index])


            previous_list = my_list.copy()
            try:
                remove_index = int(input("Enter the index to remove: "))

                if 0 <= remove_index < len(my_list):

                    previous_list = my_list.copy()
                    previous_completed_list = completed_list.copy()

                    my_list.pop(remove_index)
                    print("Item removed successfully!")

                else:
                    print("Invalid index! Please try again.")

            except ValueError:
                print("Please enter a valid number!")


            print("Item removed successfully!")

    elif choice == "3":
        print("\nWhich list would you like to view?")
        print("1. To-do List")
        print("2. Completed List")

        list_choice = input("Enter your choice: ")

        if list_choice == "1":
            print("\n--- TO-DO LIST ---")

            for index in range(len(my_list)):
                print(index, "-", my_list[index])

            if len(my_list) == 0:
                print("Your to-do list is empty!")

        elif list_choice == "2":
            print("\n--- COMPLETED LIST ---")

            for index in range(len(completed_list)):
                print(index, "-", completed_list[index])

            if len(completed_list) == 0:
                print("Your completed list is empty!")

        else:
            print("Invalid choice!")

    elif choice == "4":
        my_list = previous_list.copy()
        completed_list = previous_completed_list.copy()
        print("Previous change undone!")

    elif choice == "5":
        if len(my_list) == 0:
            print("Your to-do list is empty!")
        else:
            for index in range(len(my_list)):
                print(index, "-", my_list[index])

            try:
                replace_index = int(input("Enter the index to replace: "))

                if 0 <= replace_index < len(my_list):

                    new_item = input("Enter the new item: ")

                    previous_list = my_list.copy()
                    previous_completed_list = completed_list.copy()

                    my_list[replace_index] = new_item

                    print("Item replaced successfully!")
                else:
                    print("Invalid index!")

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "6":
        if len(my_list) == 0:
            print("Your to-do list is empty!")
        else:
            for index in range(len(my_list)):
                print(index, "-", my_list[index])

            try:
                complete_index = int(input("Enter the index to complete: "))

                if 0 <= complete_index < len(my_list):

                    previous_list = my_list.copy()
                    previous_completed_list = completed_list.copy()

                    item = my_list.pop(complete_index)
                    completed_list.append(item)

                    print("Item moved to completed list!")

                    print("Item moved to completed list!")
                else:
                    print("Invalid index!")

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "7":
        print("Thank you for using the List Making App!")
        break


    else:
        print("Invalid choice! Please enter a number between 1 and 7.")