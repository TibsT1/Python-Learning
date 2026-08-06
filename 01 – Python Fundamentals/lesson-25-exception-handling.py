planned_hours = 24

# Your program should:

# 1. Print "Study progress checker started."

# 2. Ask the user to enter their completed study hours.

# 3. Store the original input in raw_completed_hours.

# 4. Inside a try block, convert raw_completed_hours into an integer.

# 5. Store the converted value in completed_hours.

# 6. Calculate planned_hours minus completed_hours.

# 7. Store the result in remaining_hours.

# 8. Print the completed hours using an f-string.

# 9. If completed_hours is at least planned_hours, print "Weekly target completed."

# 10. Otherwise, print "Hours remaining: X" using an f-string.

# 11. Use except ValueError to print "Invalid input. Enter a whole number."

# 12. Print "Study progress checker finished." after the try and except blocks.

# Catch only ValueError.

# Do not use a bare except.

# Do not use a loop yet.

print("Study progress checker started.")
raw_completed_hours = input("Enter completed hours: ")

try:
    completed_hours = int(raw_completed_hours)
    remaining_hours = planned_hours - completed_hours
    print(f"Completed hours: {completed_hours}")
    if completed_hours >= planned_hours:
        print("Weekly target completed.")
    else:
        print(f"Hours remaining: {remaining_hours}")
except ValueError:
    print("Invalid input. Enter a whole number.")

print("Study progress checker finished.")