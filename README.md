# User Management Script

This is a Python script for managing user data (name, email, and phone number) in an Excel file. The script provides a simple console interface to add users and display stored user data. It stores data in an Excel file (`user_data.xlsx`) using `pandas` and validates input without using regular expressions.

## Features

- **Add User**: Prompts for user details (Name, Email, Phone Number) with validation and saves them in `user_data.xlsx`.
- **Display Users**: Reads and displays user data from the Excel file in a readable format.
- **Input Validation**: Ensures valid input for each field:
  - **Name**: Alphabetic characters and spaces only.
  - **Email**: Checks for the presence of `@` and `.` in valid positions.
  - **Phone Number**: Must be a 10-digit number.

## Requirements

- Python 3.6 or higher
- `pandas` library

### Installation of Dependencies

To install the required dependencies, run:

```bash
pip install pandas
```

### Usage

- Clone the repository or download the script file to your local machine.
- Run the script using Python:

```bash
python user_management.py
```
- Follow the prompts in the console to add or display users.
