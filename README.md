# AWS CloudTrail GZ to JSON Processor

This Python script processes AWS CloudTrail log files that are compressed in `.gz` format. It unzips the `.gz` files, saves them as `.json` files, and then combines all the resulting `.json` files into a single output file. The script is designed to walk through all subdirectories of a given root AWS CloudTrail log directory to find and process `.gz` files.

This is useful for managing large amounts of CloudTrail logs, particularly when you need them in a single JSON file for analysis or processing.

## Features:

- Unzips AWS CloudTrail `.gz` log files.
- Converts them into `.json` format.
- Combines multiple `.json` files into one.
- Walks through all subdirectories of the input directory to find `.gz` files.
- Skips invalid or malformed JSON files and logs errors.

## Requirements:

- Python 3.x
- `gzip`, `json`, `os`, `shutil`, `sys` (standard Python libraries)

## Installation:

1. Ensure Python 3 is installed. Check your Python version with:

```bash
   python3 --version
```

2. Download or clone this script.

3. No external dependencies are required, as the script uses Python's standard libraries.


## Usage:

### Command-line Arguments:

```bash
python3 process_gz_to_json.py /path/to/input/dir /path/to/output/dir
```

Where:

- `/path/to/input/dir`: The root directory where CloudTrail `.gz` log files are stored. The script will walk through all subdirectories to find `.gz` files.
- `/path/to/output/dir`: The directory where the unzipped `.json` files will be saved, and where the final combined JSON output file will be stored.

### Example Usage:

```bash
python3 process_gz_to_json.py /home/user/cloudtrail_logs /home/user/processed_logs
```

### What the Script Does:

1. The script will walk through all subdirectories of the input directory (`/path/to/input/dir`) to find `.gz` CloudTrail log files.
2. It will unzip each `.gz` file and convert it to `.json` format, saving each one in a `Json` folder within the output directory (`/path/to/output/dir`).
3. After all `.gz` files are processed, the script will combine all the individual `.json` files into a single file: `Cloudtrail_Combined_log.json`, inside the output directory.

### Example Output Directory Structure:

```
/home/user/processed_logs
├── Json/
│   ├── cloudtrail_log1.json
│   ├── cloudtrail_log2.json
│   └── cloudtrail_log3.json
└── Cloudtrail_Combined_log.json
```

### Error Handling:

- If a `.gz` file is not valid or cannot be parsed as JSON, it will be skipped, and the script will print a warning message.
- If the input or output directories are missing, the script will exit with an error message.

## Known Issues:

- The script assumes all `.gz` files contain valid CloudTrail JSON data. If any files are corrupted or empty, they will be skipped, but no further information is provided other than a print message.
- For very large numbers of files or extremely large log files, the script's performance may degrade. Performance optimizations can be added if needed.

## How to Contribute:

If you identify a bug, would like to improve the script, or want to add features, feel free to fork the repository, create a branch, and submit a pull request. Some suggestions for contributions include:

- Handling additional CloudTrail log formats (e.g., other compression formats like `.zip`).
- Enhancing error handling and logging.
- Adding tests for various CloudTrail log formats.

---

## Example Contributions:

- **Bug Fix**: If you find an issue where a `.gz` file isn't being properly unzipped or converted to `.json`, please submit a fix.
- **Performance Improvement**: If you know of ways to make the script faster when processing large logs, contributions are welcome!
- **New Features**: Adding support for additional log processing or CloudTrail formats is encouraged.

---

### **Script Walk-through:**

The script is designed to walk through all subdirectories of the specified root AWS CloudTrail log directory. This means that if your `.gz` log files are spread across multiple folders, the script will find and process them all.

- **Input Directory**: The root directory that contains the AWS CloudTrail log files. The script will recursively search for `.gz` files within all subdirectories.
- **Processing Subdirectories**: For example, if your input directory looks like this:

   ```
    /home/user/cloudtrail_logs
    ├── folder1/
    │   ├── log1.gz
    │   └── log2.gz
    ├── folder2/
    │   ├── log3.gz
    └── log4.gz
    ```

	The script will find and process all `.gz` files (`log1.gz`, `log2.gz`, `log3.gz`, `log4.gz`) regardless of their location in subdirectories. The resulting `.json` files will be stored in the `Json` folder of the specified output directory.
