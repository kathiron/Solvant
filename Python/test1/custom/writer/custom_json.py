import json
from custom.utils.common import Common

class CustomJson():

    def __init__(self) -> None:
        # TODO document why this method is empty
        pass

    def read_and_append_file(self, filename, new_record):
        """Reads a JSON file, appends a new record, and writes the updated data back to the file.

        Args:
            filename (str): The name of the JSON file.
            new_record (dict): A dictionary representing the new record.

        Returns:
            None
        """

        try:
            with open(filename, 'r+') as jsonfile:
                data = json.load(jsonfile)
                print(data, new_record)

                # Append the new record to the existing data
                data.append(new_record)

                # Write the updated data back to the file
                jsonfile.seek(0)  # Rewind to the beginning of the file
                json.dump(data, jsonfile, indent=4)  # Indent for better readability

            print("New record added successfully!")
        except FileNotFoundError:
            print("Error: File not found.")

    def save_to_file(self, customers, filename):
        currentid = 0
        try:
            with open(filename, 'r') as jsonfile:
                existing_data = json.load(jsonfile)
                last_record = existing_data[-1]
                currentid = last_record['id']
                print(len(existing_data))
        except FileNotFoundError:
            existing_data = []

        new_data = [customer.to_dict() for customer in customers]
        print(currentid)
        Common.generate_unique_id(new_data, currentid)
        existing_data.extend(new_data)

        with open(filename, 'w') as jsonfile:
            json.dump(existing_data, jsonfile, indent=4)