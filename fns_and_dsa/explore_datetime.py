# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Part 1: Display the current date and time
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted}")

def calculate_future_date():
    try:
        days = int(input("Enter number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        print(f"Future Date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
