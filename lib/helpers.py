# lib/helpers.py
from models.task import Task
from models.category import Category
from datetime import datetime



def addTask():
    name = input("Enter task name: ")
    desc = input("Enter a description: ")
    date = input("Enter a due date: ")
    catId = input("Enter a category id: ")
    Task.create(name, desc, date, catId)
    print("Task added")

def listTasks():
    tasks = Task.get_all()

    print(tasks)


def exit_program():
    print("Goodbye!")
    exit()

def addCat():
    name = input("Enter category name: ")
    Category.create(name)
    print("Category added")

def listCat():
    cat = Category.get_all()
    print(cat)

def completeTask():
    name = input("Enter task name ")
    task = Task.find_by_name(name)
    if task:
        task.status = True
        task.update()
    e

def findByDate():
    date = input("Enter date YYYY-MM-DD: ")
    task = Task.get_by_date(date)
    if task:
        print(task)
    else:
        print("No task due on that date")
 
def dueToday():
    current_date = datetime.now().date()
    tasks = Task.get_by_date(current_date)
    print(tasks)

def deleteCategory():
    id = input("Enter category id: ")
    category = Category.get_by_id(id)
    if category:
        category.delete()
        print("Category deleted")
    else:
        print("Invalid category id")


def categoryTasks():
    id = input("Enter category id: ")
    category = Category.get_by_id(id)
    if category:
        print(category.tasks())
    else:
        print("Invalid category id")

def updateDate():
    name = input("Enter task name: ")
    
    task = Task.find_by_name(name)
    if task:
        new_date = input("Enter new date: ")
        task.due_date = new_date
        task.update()
        print("Task updated")
    else:
        print("Incorrect task name")