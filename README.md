# Password Complexity Checker

## Purpose
The purpose of this project is to provide a tool for evaluating the strength and complexity of passwords in Python. It assesses passwords based on criteria such as length, character types (uppercase, lowercase, digits, special characters), and sequential patterns to ensure robust security practices.

## Description
This script allows users to input passwords and receive feedback on their strength and compliance with security guidelines. It evaluates passwords against the following criteria:
- Minimum length of 8 characters.
- Inclusion of both uppercase and lowercase letters.
- Presence of digits (0-9) and special characters (e.g., !@#$%^&*()).
- Absence of consecutive sequences of characters or numbers.

## How It Works
1. **Input:**
   - User enters a password to be evaluated for complexity.

2. **Processing:**
   - Checks if the password meets specified requirements using boolean checks for length, character types, and sequential patterns.
   - Utilizes the zxcvbn library to analyze the password strength and provide a numerical score (0 to 4) and feedback.

3. **Output:**
   - Displays whether the password meets all criteria or lists missing requirements.
   - Provides a complexity score and additional suggestions to improve password strength if applicable.

## Example Usage
1. **Password Input:**
   - User enters a password, and the script evaluates its complexity.
   
2. **Output:**
   - Indicates if the password meets all requirements or specifies which criteria are not fulfilled.
   - Displays a complexity score (0 to 4) and offers suggestions to enhance password security.

## Notes
- Ensure Python and the zxcvbn library are installed to run the script.
- Modify the criteria or scoring system as needed for specific security policies or requirements.
