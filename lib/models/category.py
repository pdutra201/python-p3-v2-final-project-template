from models.__init__ import CONN, CURSOR


class Category:
    all = {}

    def __init__(self, name, id = None):
        self.name = name
        self.id = id
    
    def __repr__(self):
        return f"Category {self.id}: {self.name}"
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IS NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT,
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS categories;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO categories (name)
            VALUES (?)
            """
        
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name):
        category = cls(name)
        category.save
        return category

