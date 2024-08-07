# Keylogger Project

## Overview

This Python-based keylogger captures and logs keystrokes from the keyboard. It uses the `pynput` library to listen to key presses and writes the captured keystrokes to a log file. The project also includes basic log management to handle file size and rotation.

## Features

- **Keystroke Capture**: Logs all keystrokes, including special keys.
- **File Management**: Automatically rotates log files when they exceed a specified size (5 MB in this case).
- **Logging**: Detailed logs of key events and system activities.

## Requirements

- Pycharm
- Python 3.10.0
- `pynput` library

You can install the required library using pip:

`pip install pynput`

## Usage

**1. Run the Keylogger**

- To start the keylogger, execute the script from the command line:

- `python keylogger.py`

**2. Log Files**

- Keyfile.txt: The primary log file where keystrokes are recorded.

- Keyfile.log: These log messages provide information about the status and actions of a keylogger program at a specific time.

**3. Stopping the Keylogger**

- The keylogger will continue running until interrupted. You can stop it using Ctrl + C in the terminal or by stop the program. The keylogger will log this event and exit gracefully.

## Code Breakdown

- **Logging Configuration**: Configures logging to Keyfile.log with a debug level and specified format.

- **Key Press Handling**: Logs each key press and handles special keys.

- **File Management**: Checks the size of Keyfile.txt and rotates the file if necessary.

- **Listener Setup**: Initializes the key listener and starts capturing keystrokes.

## Example Log

2022-07-29 11:13:13,963 - INFO - Keylogger started.

2022-07-29 11:13:14,123 - INFO - Logged character: a

2022-07-29 11:13:15,456 - INFO - Logged special key: [Key.shift]

2022-07-29 11:13:16,789 - INFO - Log file rotated: Keyfile_20240729081316.txt

## Important Notes

- **Ethical Use**: This keylogger is for educational purposes only. Ensure you have explicit permission before using it on any system.

- **Security**: Be cautious when handling sensitive information. The keylogger logs all keystrokes, which may include personal or confidential data.

## Note

"Don’t forget to add the Python path to your environment variables."