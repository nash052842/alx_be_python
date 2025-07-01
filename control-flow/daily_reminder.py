# daily_reminder.py

def main():
    # Prompt for task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Match case to respond based on priority
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Make sure to complete it soon.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be done today.")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Try to get to it this week.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task, but it's time-bound—try not to miss it.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority level entered. Please use high, medium, or low.")

if __name__ == "__main__":
    main()
