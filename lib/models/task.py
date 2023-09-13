from models.__init__ import CONN, CURSOR
from models.category import Category
import ipdb
from datetime import datetime

class Task():
    all = {}

    def __init__(self, name, description, due_date, category_id, id = None):
        self.id = id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = False
        self.category_id = category_id

    def __repr__(self):
        return f"(Task: {self.name}, " + \
        f"{self.description}, " + \
        f"Due Date: {self.due_date}, " + \
        "status: " + ("incomplete, " if self.status == False else "Complete, ") + \
        f"Cetegory ID: {self.category_id})"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description):
            self._description = description
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
    
    @property
    def due_date(self):
        return self._due_date
    
    @due_date.setter
    def due_date(self, due_date):
        try: 
            self._due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
            

    @classmethod
    def create_table(cls):
    
        sql = """
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT, 
            description TEXT,
            due_date DATE,
            status BOOLEAN,
            category_id INTEGER, 
            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE);
            """
        
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS tasks;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO tasks (name, description, due_date, status, category_id)
            VALUES (?,?,?,?,?)
        """
        CURSOR.execute(sql, (self.name, self.description, self.due_date, self.status, self.category_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self


    def update(self):
        sql = """
            UPDATE tasks
            SET name = ?, description = ?, due_date = ?, status = ?, category_id = ?
            WHERE id = ?
            """
        
        CURSOR.execute(sql, (self.name, self.description, self.due_date, self.status, self.category_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM tasks
            WHERE id = ?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, description, due_date, category_id):
        task = cls(name, description, due_date, category_id)
        task.save()
        return task
    
    @classmethod
    def instance_from_db(cls, row):
        task = cls.all.get(row[0])
        if task:
            task.name = row[1]
            task.description = row[2]
            task.due_date = row[3]
            task.status = row[4]
            task.category_id = row[5]
            
        else:
            task = cls(row[1], row[2], row[3], row[5])
            task.id = row[0]
            cls.all[task.id] = task

        # ipdb.set_trace()
        return task
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM tasks"""

        rows = CURSOR.execute(sql).fetchall()
        
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def get_by_date(cls, date):
        sql = """
            SELECT * FROM tasks
            WHERE due_date = ?
            """
        
        rows = CURSOR.execute(sql, (date,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM tasks
            WHERE name = ?"""
        
        row = CURSOR.execute(sql, (name,)).fetchone()
        
        return cls.instance_from_db(row) if row else None