#!/usr/bin/env python3

import os
import gzip
import json
import shutil
import sys

def unzip_gz_to_json(gz_file_path, output_dir):
    """Unzips a .gz file and saves its content as a .json file."""
    try:
        with gzip.open(gz_file_path, 'rt', encoding='utf-8') as gz_file:
            # Read the content of the gzipped file
            json_data = json.load(gz_file)
            
            # Create output JSON file path
            json_file_name = os.path.splitext(os.path.basename(gz_file_path))[0] + '.json'
            json_file_path = os.path.join(output_dir, json_file_name)
            
            # Write the JSON data to the new .json file
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, indent=4)
    except json.JSONDecodeError:
        print(f"Skipping invalid JSON file: {gz_file_path}")
    except Exception as e:
        print(f"Error processing {gz_file_path}: {e}")

def combine_json_files(input_dir, output_json_file):
    """Combines all JSON files from the input directory into one."""
    combined_data = []

    # Traverse all subdirectories and files in the input directory
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.json'):
                json_file_path = os.path.join(root, file)
                # Load the JSON data from each file
                try:
                    with open(json_file_path, 'r', encoding='utf-8') as json_file:
                        data = json.load(json_file)
                        combined_data.append(data)
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON file: {json_file_path}")

    # Write the combined data into a single JSON file
    with open(output_json_file, 'w', encoding='utf-8') as output_file:
        json.dump(combined_data, output_file, indent=4)

def process_gz_files(input_dir, output_dir):
    """Unzips .gz files and combines all .json files into one."""
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    unzipped_json_folder = os.path.join(output_dir, "Json")
    os.makedirs(unzipped_json_folder, exist_ok=True)

    # Unzip all .gz files into .json files
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.gz'):
                gz_file_path = os.path.join(root, file)
                unzip_gz_to_json(gz_file_path, unzipped_json_folder)
    
    # Combine all resulting JSON files into one
    output_json_file = os.path.join(output_dir, "Cloudtrail_Combined_log.json")
    combine_json_files(unzipped_json_folder, output_json_file)
    print(f"All JSON files have been combined into {output_json_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Example Usage: python3 {sys.argv[0]} /path/to/input/dir /path/to/output/dir")
        exit(1)
    else:
        input_directory = sys.argv[1]
        output_directory = sys.argv[2]

        # Ensure the input directory exists
        if not os.path.exists(input_directory):
            print(f"Error: Input directory {input_directory} does not exist.")
            exit(1)
        if not os.path.exists(output_directory):
            print(f"Error: Output directory {output_directory} does not exist.")
            exit(1)

        process_gz_files(input_directory, output_directory)