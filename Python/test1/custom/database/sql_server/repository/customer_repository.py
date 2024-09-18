import json
from custom.database.sql_server.sql_server_database_manager import SqlServerDatabaseManager
from custom.database.model.customer import Customer

class CustomerRepository():
    def __init__(self):
        self.db_mgr = SqlServerDatabaseManager()
        self.table = 'customer'

    def create_table(self):
        query = '''IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'customer')
                BEGIN
                    CREATE TABLE customer (
                        id INT IDENTITY(1,1) PRIMARY KEY,
                        name VARCHAR(50),
                        age INT,
                        city VARCHAR(100),
                        status SMALLINT DEFAULT(1),
                        created_on BIGINT DEFAULT (DATEDIFF(SECOND, '1970-01-01', GETUTCDATE())),
                        modified_on BIGINT NULL
                    );
                END;'''
        sucmsg = self.db_mgr.run_query(query)
        try:
            query = '''CREATE TRIGGER trg_customer_update
                ON  customer
                AFTER UPDATE
            AS 
            BEGIN
                -- SET NOCOUNT ON added to prevent extra result sets from
                -- interfering with SELECT statements.
                SET NOCOUNT ON;

                UPDATE customer
                SET modified_on = DATEDIFF(SECOND, '1970-01-01', GETUTCDATE())
                WHERE id IN (SELECT id FROM INSERTED);

            END'''

            sucmsg = self.db_mgr.run_query(query)
        except Exception as e:
            errmsg = f'Error connecting to SQL Server TRIGGER : {e}'
            print(errmsg)
            sucmsg = errmsg
        return sucmsg

    def insert_data(self, obj:Customer):
        try:
            if isinstance(obj, dict):
                obj = json.loads(json.dumps(obj))
            return self.db_mgr.run_query(f'INSERT INTO {self.table} (name, age, city) VALUES (?, ?, ?)'
                                         , (obj.name, obj.age, obj.city))
        except Exception as e:
            errmsg = f'Error connecting to SQL Server insert_data : {e}'
            print(errmsg)
            return errmsg

    def delete_data(self, id, param = None):
        try:
            raise self.db_mgr.run_query(f'UPDATE {self.table} SET status = 0 WHERE id = {id}', param)
        except Exception as e:
            errmsg = f'Error connecting to SQL Server delete_data : {e}'
            print(errmsg)
            return errmsg

    def fetch_data(self, status:int = 1, param = None):
        try:
            return self.db_mgr.run_query(f"SELECT * FROM {self.table} WHERE status = {status}", param)
        except Exception as e:
            errmsg = f'Error connecting to SQL Server fetch_data : {e}'
            print(errmsg)
            return errmsg

    def get_data(self, id, status:int = 1):
        try:
            return self.db_mgr.run_query(f"SELECT * FROM {self.table} WHERE status = {status} AND id = ?", (id))
        except Exception as e:
            errmsg = f'Error connecting to SQL Server get_data : {e}'
            print(errmsg)

    def get_data_by_name(self, id, name:str):
        try:
            return self.db_mgr.run_query(f"SELECT * FROM {self.table} WHERE status = 1 AND id = ?", (name))
        except Exception as e:
            errmsg = f'Error connecting to SQL Server get_data : {e}'
            print(errmsg)
    
    def update_data(self, obj:Customer):
        try:
            if isinstance(obj, dict):
                obj = json.loads(json.dumps(obj))
            return self.db_mgr.run_query(f'update {self.table} set name = ?, age = ?, city = ? WHERE id = ?'
                , (obj['name'], obj['age'], obj['city'], obj['id']))
        except Exception as e:
            errmsg = f'Error connecting to SQL Server update_data : {e}'
            print(errmsg)
            return errmsg