# Python to EXE Converter

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
- PyInstaller (automatically installed if missing)
- tkinter (usually comes with Python)

## Installation

### Option 1: Install from Source

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/py-to-exe-converter.git
   cd py-to-exe-converter
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python py_to_exe_converter.py
   ```

### Option 2: Download Pre-built Executable

1. Go to the [Releases](https://github.com/yourusername/py-to-exe-converter/releases) page
2. Download the latest version for your operating system
3. Extract the zip file and run the executable

## Usage Guide

### Converting a Python Script

1. **Launch the Application**
   - Double-click the executable or run `python py_to_exe_converter.py`

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

## Creating a requirements.txt File

For GitHub and proper installation, create a `requirements.txt` file in your project root with the following content:

```
pyinstaller>=5.1
```

## Project Structure

```
py-to-exe-converter/
├── py_to_exe_converter.py      # Main application file
├── requirements.txt            # Project dependencies
├── LICENSE                     # License information
├── README.md                   # This readme file
└── assets/                     # Optional folder for icons and images
    └── icon.ico                # Application icon
```

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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [PyInstaller](https://pyinstaller.org/) for the amazing packaging tool
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework

---

**Note**: This project is maintained by [Your Name]. For support, please open an issue on GitHub.
