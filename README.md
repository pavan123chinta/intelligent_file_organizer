Intelligent File Organizer

A CLI-based Python automation tool that organizes files into categories and detects duplicate files using content-based hashing.

Overview

Intelligent File Organizer is a modular Python automation project designed to:

Automatically organize files into categorized folders

Detect duplicate files using hash comparison

Safely remove or move duplicates

Generate execution reports

Provide CLI options including dry-run mode

This project demonstrates clean architecture, modular design, and safe file automation practices.

Features
File Categorization

Automatically organizes files into folders:

Images

Documents

Videos

Audio

File types are mapped using configuration from config.json.

Duplicate Detection

Uses content-based hashing

Identifies files with identical content

Supports duplicate movement to a Duplicates folder

Optional dry-run mode for safe testing

Dry Run Mode

Run safely without modifying files:

python main.py --path test_files --remove-duplicates --dry-run


This shows what would happen without actually moving files.

Execution Reporting

Generates structured reports inside:

reports/


Report includes:

Total files scanned

Files moved

Folders created

Unknown files

Total duplicates found

Duplicates moved

Logging

Structured logging system using Python logging module:

INFO

WARNING

ERROR

Project Structure
intelligent_file_organizer/
│
├── organizer/
│   ├── file_manager.py
│   ├── duplicate_handler.py
│   ├── reporter.py
│   ├── logger_config.py
│   └── utils.py
│
├── test_files/
├── reports/
├── logs/
│
├── config.json
├── main.py
├── requirements.txt
└── README.md

Installation
1. Clone the repository
git clone https://github.com/pavan123chinta/intelligent_file_organizer.git
cd intelligent_file_organizer

2. Create virtual environment (Recommended)
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

Usage
Basic Run
python main.py --path test_files

Remove Duplicates
python main.py --path test_files --remove-duplicates

Safe Mode (Dry Run)
python main.py --path test_files --remove-duplicates --dry-run

Technical Concepts Demonstrated

File handling and OS operations

Directory traversal

Hash-based duplicate detection

CLI argument parsing using argparse

Logging configuration

Report generation

Modular architecture

Version control using Git

Author

Pavan Chinta
Automation Engineer | Python Enthusiast