from models.__init__ import CONN, CURSOR
from models.category import Category
from models.task import Task

def seed_dbs():
    Category.drop_table()
    Category.create_table()
    Task.drop_table()
    Task.create_table()


    cleaning = Category.create("Cleaning")
    school_work = Category.create("School Work")

    Task.create("Dishes", "Wash dirty dishes", "2023-10-12", cleaning.id)
    Task.create("Mop", "Mop the floors", "2023-12-13", cleaning.id)
    Task.create("Make bed", "Change the sheets on the bed", "2023-09-12", cleaning.id)
    Task.create("Homework", "Do homework for current section", "2023-09-13", school_work.id)
    Task.create("Study", "Study for next quiz", "2024-01-01", school_work.id)

    print(cleaning, school_work)
seed_dbs()
print("Seeded Database")