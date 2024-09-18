import sqlite3

from custom.database.model.customer import Customer

class SqlLiteDatabaseManager:  # Use PascalCase for class names

    def __init__(self, db_name="output/trial_db.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        # Create the table (only if it doesn't exist)
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS customer (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                age INTEGER,
                                city TEXT,
                                status SMALLINT DEFAULT 1
                            )''')

    def insert_data(self, obj:Customer):
        self.cursor.execute("INSERT INTO customer (name, age, city) VALUES (?, ?, ?)", (obj.name, obj.age, obj.city))

    def fetch_data(self):
        self.cursor.execute("SELECT * FROM customer")
        return self.cursor.fetchall()

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()