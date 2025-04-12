# Python to EXE Converter

IT WAS ALL GENERATED WITH CLAUDE AI BECAUSE OTHER CHAT MODELS ARE DUMB AND CAN'T DO IT

A simple GUI application that converts Python (.py) files to standalone executable (.exe) files using PyInstaller.

## Features

- User-friendly graphical interface
- One-click conversion from .py to .exe
- Supports both one-file and one-directory packaging options
- Option to show/hide console window
- Custom icon support
- Automatic dependency management
- Progress tracking and detailed logs
- Custom PyInstaller arguments support

## Requirements

- Python 3.6 or higher
- PyInstaller
- tkinter (usually comes with Python)

## Installation

1. Install Python 3.6 or higher if you don't have it already
2. Save the `py_to_exe_converter.py` file to your computer
3. Open a command prompt or terminal and navigate to the folder containing the file
4. Install PyInstaller (if not already installed):
   ```
   pip install pyinstaller
   ```
5. Run the application:
   ```
   python py_to_exe_converter.py
   ```

## Usage Guide

### Converting a Python Script

1. **Launch the Application**
   - Run `python py_to_exe_converter.py` in your terminal/command prompt

2. **Select Your Python Script**
   - Click the "Browse" button next to "Python Script"
   - Navigate to and select your `.py` file

3. **Choose Output Directory**
   - By default, this is set to the same directory as your Python script
   - Click "Browse" to change the output location

4. **Configure Build Options**
   - **One-file package**: Creates a single executable file (recommended for distribution)
   - **Console based application**: Shows console window when running (useful for scripts with terminal output)

5. **Advanced Options (Optional)**
   - Add an icon file (`.ico` format)
   - Specify additional PyInstaller arguments

6. **Check Requirements**
   - Click "Check Requirements" to verify PyInstaller is installed
   - The application will automatically install PyInstaller if needed

7. **Convert to EXE**
   - Click "Convert to EXE" to start the conversion process
   - The progress bar will show activity during conversion
   - Conversion logs will appear in the output area
   - A success message will display when complete

8. **Retrieve Your Executable**
   - Your executable will be available in the specified output directory
   - The file name will be the same as your Python script but with the `.exe` extension

## Common Issues and Solutions

### "PyInstaller not found" Error
- Click the "Check Requirements" button to automatically install PyInstaller
- Alternatively, run `pip install pyinstaller` manually

### Missing Modules in Executable
- Some packages require special handling in PyInstaller
- Use the "Additional PyInstaller Arguments" field to add `--hidden-import=module_name`

### Antivirus Flags Executable
- This is a common false positive with PyInstaller executables
- Add exclusions in your antivirus software or code-sign your application

### Large File Size
- PyInstaller bundles Python and all dependencies into the executable
- Use virtual environments with only necessary packages installed
