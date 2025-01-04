# AWS-CloudTrail-GZ-to-JSON-Processor
This Python script processes AWS CloudTrail log files that are compressed in .gz format. It unzips the .gz files, saves them as .json files, and then combines all the resulting .json files into a single output file. The script is designed to walk through all subdirectories of a given root AWS CloudTrail log directory to find and process .gz files.
