#  Intelligent File Organizer

A professional-grade Python CLI tool that automatically organizes files into categorized folders based on file extensions.  
Includes logging, dry-run mode, execution metrics, and auto-generated reports.

---

##  Features

- Organizes files by extension (Images, Documents, Videos, Audio, etc.)
- Automatic category folder creation
- Dry Run mode (simulate without moving files)
- Execution metrics tracking
- Auto-generated detailed report
- Centralized logging system
- Clean modular architecture
- CLI-based execution

---

##  Project Structure

intelligent_file_organizer/
│
├── organizer/
│ ├── logger_config.py
│ ├── utils.py
│ ├── file_manager.py
│ ├── reporter.py
│ └── duplicate_handler.py
│
├── config.json
├── main.py
├── requirements.txt
├── README.md
└── .gitignore


##  Installation

1️ Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/intelligent_file_organizer.git
cd intelligent_file_organizer

2️ Install dependencies:

pip install -r requirements.txt

Usage
Normal Mode
Organizes files inside the specified folder:

python main.py --path test_files
 Dry Run Mode (Safe Mode)
Simulates file organization without moving files:

python main.py --path test_files --dry-run

Sample Output
INFO | Intelligent File Organizer Application Started
INFO | Loaded categories: ['Images', 'Documents', 'Videos', 'Audio']
INFO | Moved 'photo.jpg' to 'Images' folder.
WARNING | No category found for file: unknown.xyz

----- Execution Summary -----
Total files scanned: 6
Files moved: 3
Folders created: 0
Unknown files: 3

Generated Report
Each run generates a timestamped report inside the reports/ directory:

Example:

reports/report_20260218_173046.txt
Report includes:

Execution Mode

Target Path

Files Scanned

Files Moved

Folders Created

Unknown Files

How It Works

Loads category rules from config.json

Scans the target directory

Matches file extensions to categories

Creates folders if needed

Moves files (or simulates in dry-run mode)

Tracks execution metrics

Generates summary report

Tech Stack

Python 3.13

argparse (CLI handling)

logging (Centralized logging)

os & shutil (File operations)

JSON (Configuration management)

Use Cases

Desktop file cleanup

Automation practice project

Python CLI development learning

SDET / Automation portfolio project

Future Improvements

Duplicate file detection

GUI version

Configurable logging level

Unit test coverage

Cloud storage integration

Author

Pavan Chinta
Automation & Python Enthusiast