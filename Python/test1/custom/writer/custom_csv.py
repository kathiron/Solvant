import csv
from custom.utils.common import *

class CustomCsv():

    def __init__(self) -> None:
        # TODO document why this method is empty
        pass

    def read_and_append_file(self, filename, new_record):
        """Reads a CSV file, appends a new record, and writes the updated data back to the file.

        Args:
            filename (str): The name of the CSV file.
            new_record (list): A list containing the new record data in the same order as the existing headers.

        Returns:
            None
        """

        try:
            with open(filename, 'r+', newline='') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)  # Read the header row
                existing_data = list(reader)

                # Append the new record to the existing data
                existing_data.append(new_record)

                # Write the updated data back to the file
                csvfile.seek(0)  # Rewind to the beginning of the file
                writer = csv.writer(csvfile)
                writer.writerow(header)
                writer.writerows(existing_data)

            print("New record added successfully!")
        except FileNotFoundError:
            print("Error: File not found.")

    def save_to_file(self, customers, filename):
        currentid = 0
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                existing_data = list(reader)
                last_record = existing_data[-1]
                currentid = last_record['id']
                print(len(existing_data))
        except FileNotFoundError:
            print("errrrrrooooor")
            existing_data = []

        new_data = [customer.to_dict() for customer in customers]
        print(currentid)
        Common.generate_unique_id(new_data, currentid)
        existing_data.extend(new_data)

        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ["id", "name", "age", "city"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(existing_data)