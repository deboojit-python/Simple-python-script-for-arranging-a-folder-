# Auto File Organizer in Python

This is a Python automation script that keeps your messy Downloads folder clean and organized. It automatically scans the folder and moves files into categorized sub-folders (like Photos, Video, Document, etc.) based on their file extensions.

## Features:
* Scans the specified folder automatically.
* Checks file extensions (e.g., .mp4, .png, .pdf).
* Automatically creates new folders if they do not exist and moves the files there.

## How to Use:
1. Before running the code, you **must change** the `download_path` variable in the script to match your computer's Downloads folder location.
   - For Windows, it might look like: `download_path = "C:\\Users\\YourName\\Downloads"`
   - For Linux/Ubuntu, it looks like: `download_path = "/home/yourname/Downloads"`
2. Make sure you have Python installed. The `os` and `shutil` libraries used in this script come pre-installed with Python, so you do not need to install anything else.
