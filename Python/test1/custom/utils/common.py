from datetime import datetime
import enum
import json
import re

statement_types = {
    "select": "SELECT",
    "update": "UPDATE",
    "insert": "INSERT",
    "delete": "DELETE"
}

class Common:
    @staticmethod
    def get_response_type(enum_instance, is_sentence_case: bool = True):
        # Get the enum name and pass it to Common for formatting
        return Common.split_camel_case(enum_instance.name, is_sentence_case)

    @staticmethod
    def get_current_datetime_formatted(format = "%d/%m/%Y %H:%M:%S"):
        # datetime object containing current date and time
        now = datetime.now()

        print("now =", now)

        # dd/mm/YY H:M:S
        dt_string = now.strftime(format)

        return dt_string
    
    @staticmethod
    def split_camel_case(text, is_sentence_case:bool = True):
        # Insert space before each capital letter except the first one
        spaced_text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
        # Convert the entire string to lowercase and then capitalize only the first letter
        return spaced_text if is_sentence_case == False else spaced_text.lower().capitalize()

    @staticmethod
    def generate_unique_id(new_data, currentid):
        for row in new_data:
            row['id'] = int(currentid) + 1
            currentid = int(currentid) + 1
        return currentid
    
    @staticmethod
    def get_data_length(data):
        if isinstance(data, bool):
            return 1 if data == True else 0
        if isinstance(data, str):
            return 1 if str(data).lower().index('error') >= 0 else 0
        if isinstance(data, dict):
            # Return the number of key-value pairs in the dictionary
            return len(data)
        elif isinstance(data, (list, tuple)):
            # Return the length of the list or tuple (number of elements)
            return len(data)
        else:
            # Return 0 for unsupported types or empty data
            return 0
    
    @staticmethod
    def to_data_format(data):
        # Check if data is None or empty
        if isinstance(data, bool) or isinstance(data, str):
            return data
        if data is None or not data:
            print('No data found, returning 404')
            return None

        # Handle if data is a string (likely a JSON string from the database)
        if isinstance(data, str):
            print('Data is a string, attempting to parse JSON')
            try:
                if len(data) > 2:  # Avoid empty or invalid JSON strings
                    data = json.loads(data)
                else:
                    return None
            except json.JSONDecodeError:
                return None

        # Ensure data is a list or convert a single dictionary into a list
        if isinstance(data, dict):
            print('Data is a dictionary, converting to list')
            data = [data]

        if not isinstance(data, list):
            print('Unexpected data format, returning 500')
            return None

        return data

    @staticmethod
    def determine_statement_type(self, statement):
        # Convert the statement to uppercase to ensure case-insensitivity
        statement_upper = statement.upper().strip()
        
        # Extract the command type from the beginning of the statement
        # Split the statement to get the first word
        command_type = statement_upper.split()[0]
        
        # Debug print to check what the statement_upper value is
        print(f"Uppercase statement: '{statement_upper}'")
        
        # Find the statement type based on the value
        for key, value in statement_types.items():
            if command_type == value:
                self.statement_type = key
                break
            else:
                # Handle case where no match is found
                self.statement_type = 'Other'
        
        # Debug print to check the statement_type value
        print(f"Statement type: '{self.statement_type}'")