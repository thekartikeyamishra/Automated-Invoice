import json
import os


def save_extracted_data(data, output_path):
    try:
        os.makedirs(os.path.dirname(output_path), exit_ok=True)
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data : {e}")
