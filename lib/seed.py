from models.__init__ import CONN, CURSOR
from models.category import Category

def seed_dbs():
    Category.drop_table()
    Category.create_table()

    cleaning = Category.create("Cleaning")
    school_work = Category.create("School Work")

    print(cleaning, school_work)
seed_dbs()
print("Seeded Database")