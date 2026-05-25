# Intelligent File Organizer

A Python-based automation tool that organizes files into categories and detects duplicate files using content-based hashing.

## Overview

Intelligent File Organizer is designed to:

- Automatically organize files into categorized folders
- Detect duplicate files using hash comparison
- Safely remove or move duplicates
- Generate execution reports
- Support CLI options including dry-run mode

This project demonstrates modular architecture, safe file handling, and Python automation practices.

---

## Features

### File Categorization

Automatically organizes files into folders such as:

- Images
- Documents
- Videos
- Audio

File extensions are mapped using configuration from `config.json`.

### Duplicate Detection

- Uses content-based hashing
- Identifies files with identical content
- Supports duplicate movement to a `Duplicates` folder
- Includes optional dry-run mode for safe execution

### Dry Run Mode

Safely preview operations without modifying files.

```bash
python main.py --path test_files --remove-duplicates --dry-run
```

### Execution Reporting

Generates structured reports inside:

```bash
reports/
```

Reports include:

- Total files scanned
- Files moved
- Folders created
- Unknown files
- Total duplicates found
- Duplicates moved

### Logging

Structured logging using Python's logging module:

- INFO
- WARNING
- ERROR

---

## Project Structure

```bash
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
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/pavan123chinta/intelligent_file_organizer.git
cd intelligent_file_organizer
```

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Basic Run

```bash
python main.py --path test_files
```

### Remove Duplicates

```bash
python main.py --path test_files --remove-duplicates
```

### Safe Mode (Dry Run)

```bash
python main.py --path test_files --remove-duplicates --dry-run
```

---

## Technical Concepts Demonstrated

- File handling and OS operations
- Directory traversal
- Hash-based duplicate detection
- CLI argument parsing using argparse
- Logging configuration
- Report generation
- Modular architecture
- Version control using Git

---

## Author

**Pavan Chinta**  
QA Automation Engineer | Python Automation | API & UI Testing
