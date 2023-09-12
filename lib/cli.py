# lib/cli.py

from helpers import (
    exit_program,
    listTasks,
    listCat,
    addTask,
    addCat,
    completeTask,
    findByDate,
    dueToday,
    deleteCategory,
    categoryTasks,
    updateDate
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            addTask()    
        elif choice == "2":
            listTasks()
        elif choice == "3":
            addCat()
        elif choice == "4":
            listCat()
        elif choice == "5":
            completeTask()
        elif choice == "6":
            findByDate()
        elif choice == "7":
            categoryTasks()
        elif choice == "8":
            dueToday()
        elif choice == "9":
            deleteCategory()
        elif choice == "10":
            updateDate()    
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a new Task")
    print("2. List Tasks")
    print("3. Add Categories")
    print("4. List Categories")
    print("5. Mark Task Completed")
    print("6. Filter by Due Date")
    print("7. Show tasks by category id")
    print("8. Display Tasks due today")
    print("9. Delete Category")
    print("10, Update Due Date")


if __name__ == "__main__":
    main()
