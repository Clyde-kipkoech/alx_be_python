

# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Loop to ensure reminder is printed once (can be useful for future repetition logic)
reminder_given = False

while not reminder_given:
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
            reminder_given = True

        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires attention today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Plan it into your schedule.")
            reminder_given = True

        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that still requires attention today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
            reminder_given = True

        case _:
            print("Invalid priority entered. Please enter high, medium, or low.")
            priority = input("Priority (high/medium/low): ").lower()
