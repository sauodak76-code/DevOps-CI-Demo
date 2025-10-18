# app.py

import datetime
import platform
import argparse


def greet(name="CI"):
    """Prints a customizable CI greeting message."""
    print(f"Hello, {name}!")
    print("Welcome to the Continuous Integration Demo 🚀")


def system_info():
    """Displays basic system and environment info."""
    print("\n🔧 --- System Information ---")
    print(f"Python Version : {platform.python_version()}")
    print(f"Platform       : {platform.system()} {platform.release()}")
    print(f"Processor      : {platform.processor() or 'Unknown'}")
    print("-----------------------------\n")


def current_time():
    """Shows the current date and time."""
    now = datetime.datetime.now()
    print(f"🕒 Current Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")


def main():
    parser = argparse.ArgumentParser(description="A simple CI demo application.")
    parser.add_argument(
        "-n", "--name", type=str, default="CI", help="Name to include in the greeting"
    )
    args = parser.parse_args()

    greet(args.name)
    current_time()
    system_info()
    print(" CI Pipeline Test Successful!")


if __name__ == "__main__":
    main()
