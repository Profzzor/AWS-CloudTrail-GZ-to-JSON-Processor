# AWS CloudTrail GZ to JSON Processor

This Python script processes AWS CloudTrail log files that are compressed in `.gz` format. It unzips the `.gz` files, saves them as `.json` files, and then combines all the resulting `.json` files into a single output file. The script is designed to walk through all subdirectories of a given root AWS CloudTrail log directory to find and process `.gz` files.

This is useful for managing large amounts of CloudTrail logs, particularly when you need them in a single JSON file for analysis or processing.

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
