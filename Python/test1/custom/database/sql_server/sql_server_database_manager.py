import pyodbc
import json
from custom.utils.common import Common

class SqlServerDatabaseManager:
    def __init__(self):
        try:
            self.statement_type = "select"

            # Usage example
            self.server = "LAPTOP-24V976OB"
            self.database = "trial_db"
            self.username = "sa"
            self.password = "Pas$w0rd5678"

            # driver = 'ODBC DRIVER 18 for SQL Server'
            self.driver = 'SQL Server'
            self.conn_str = f"DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password};TrustServerCertificate=1"
            self.set_cursor()
        except Exception as e:
            print(f"Error connecting to SQL Server: {e}")

    def set_cursor(self):
            self.conn = pyodbc.connect(self.conn_str)
            self.cursor = self.conn.cursor()
            print(self.cursor, self.cursor)
    
    def run_query(self, statement:str, params = None, ifdict = False):
        try:
            Common.determine_statement_type(self, statement)

            self.set_cursor()
            if params in [None, []]:
                self.cursor.execute(statement)
            else:
                self.cursor.execute(statement, params)
                data = True  # Indicate successful

            if self.cursor.rowcount > 0:
                data = True  # Indicate successful
                print(f'{self.statement_type} successful')
            else:
                data = False  # Indicate no rows affected
                print(f'No rows {self.statement_type}')

            self.commit_and_close()

            if ifdict or self.statement_type != 'select':
                return data
            else:
                # Fetch all rows and column names
                rows = self.cursor.fetchall()
                column_names = [column[0] for column in self.cursor.description]

                # Convert to list of dictionaries
                data = [dict(zip(column_names, row)) for row in rows]

                # Convert to JSON
                json_data = json.dumps(data, indent=4)
                return json_data
        except Exception as e:
            print(f"Error connecting to SQL Server run_query : {e}")

    def commit_and_close(self):
        try:
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            print(f"Error connecting to SQL Server commit_and_close : {e}")