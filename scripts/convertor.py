import csv
import json
import sys
from datetime import datetime

def csv_to_json(csv_file_path, json_file_path):
    """
    Convert a CSV file to JSON format.

    Args:
        csv_file_path (str): Path to the input CSV file
        json_file_path (str): Path to the output JSON file
    """
    # List to store all rows
    data = []

    # Read CSV file
    try:
        with open(csv_file_path,encoding="ISO-8859-1", mode='r') as csv_file:

            csv_reader = csv.DictReader(csv_file)

            print(csv_reader)
            for i in csv_reader:

            # Convert each row to a dictionary and add to data list
             for row in csv_reader:
                # Process date fields (convert to standard format if needed)
                for field in ['order date (DateOrders)', 'shipping date (DateOrders)']:
                    if field in row and row[field]:
                        try:
                            # Try to parse the date (adjust format as needed)
                            date_obj = datetime.strptime(row[field], '%Y-%m-%d')
                            row[field] = date_obj.strftime('%Y-%m-%d')
                        except ValueError:
                            # Keep original value if parsing fails
                            pass

                # Convert numeric fields to appropriate types
                for field in row:
                    # Try to convert to integer
                    if row[field] and row[field].isdigit():
                        row[field] = int(row[field])
                    # Try to convert to float for fields that might be decimal numbers
                    elif row[field] and row[field].replace('.', '', 1).isdigit():
                        row[field] = float(row[field])

                data.append(row)

    except FileNotFoundError:
        print(f"Error: File {csv_file_path} not found.")
        return
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    # Write to JSON file
    try:
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Successfully converted {csv_file_path} to {json_file_path}")
    except Exception as e:
        print(f"Error writing JSON file: {e}")

if __name__ == "__main__":

    input_file="./data/DataCoSupplyChainDataset.csv"
    output_file="./data/DataCoSupplyChainDataset.json"
    csv_to_json(input_file, output_file)