# app.py

import datetime
import platform

def greet():
    """Prints a CI greeting message."""
    print("Hello CI ")
    print("Welcome to Continuous Integration Demo!")

def system_info():
    """Displays basic system and environment info."""
    print("\n--- System Information ---")
    print(f"Python Version: {platform.python_version()}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print("---------------------------\n")

def current_time():
    """Shows the current date and time."""
    now = datetime.datetime.now()
    print(f"Current Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

def main():
    greet()
    current_time()
    system_info()
    print("CI Pipeline Test Successful ")

if __name__ == "__main__":
    main()
