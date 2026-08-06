planned_hours = 24

# Your program should:

# 1. Ask the user to enter their name.

# 2. Store the entered name in a variable called student_name.

# 3. Ask the user to enter their completed study hours.

# 4. Store the original text input in a variable called raw_completed_hours.

# 5. Convert raw_completed_hours into an integer.

# 6. Store the converted value in completed_hours.

# 7. Calculate the remaining hours.

# 8. Print the student's name using an f-string.

# 9. Print the completed hours using an f-string.

# 10. Print the remaining hours using an f-string.

# 11. Use an if statement to print "Weekly target completed." when completed_hours is at least planned_hours.

# 12. Otherwise, print "More study is required."

# 13. Print the type of raw_completed_hours.

# 14. Print the type of completed_hours.

# Keep the input and conversion steps separate.

# Assume the user enters a valid whole number.

# Do not use try or except yet.


student_name = input("Enter your name: ")
raw_completed_hours = input("Enter studied hours: ")
completed_hours = int(raw_completed_hours)
remaining_hours = planned_hours - completed_hours
print(f"Student name: {student_name}")
print(f"Completed hours: {completed_hours}")
print(f"Remaining horus: {remaining_hours}")

if completed_hours >= planned_hours:
    print("Weekly target completed.")
else:
    print("More study is required.")

print(type(raw_completed_hours))
print(type(completed_hours))