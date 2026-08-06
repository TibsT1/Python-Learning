planned_hours = 24
raw_completed_hours = "18"

def calculate_remaining_hours(planned, completed):
    remaining = planned - completed
    return remaining

print("Progress report started.")

completed_hours = int(raw_completed_hours)

remaining_hours = calculate_remaining_hours(planned_hours, completed_hours)

print(f"Completed hours: {completed_hours}")
print(f"Remaining hours: {remaining_hours}")

if remaining_hours > 0:
    print("The target is incomplete.")
else:
    print("The target is complete.")

print("Progress report finished.")


# Debugging instructions:

# 1. Run the program without changing anything.

# 2. Read the final line of the first traceback.

# 3. Record the first exception type in the debugging notes below.

# 4. Record the line that failed and the value that caused it.

# 5. Fix only the first problem.

# 6. Run the program again.

# 7. Read the new traceback.

# 8. Record the second exception type and its cause.

# 9. Fix only the second problem.

# 10. Run the program again and confirm that it completes successfully.

# 11. Do not rewrite the entire program.

# 12. Change one issue at a time.


# Debugging notes:

# First exception type: ValueError

# First failing line: line 10

# First cause: the value given is a string 'eighteen' instead of an integer on line 2

# First fix: changed it from 'eighteen' to '18' on line 2


# Second exception type: NameError

# Second failing line: line 12

# Second cause: wrong variable name given

# Second fix: changed the variable name on line 12 from "planned_hour" to "planned_hours"


# Problem breakdown:

# Step 1: Convert variable values if needed.

# Step 2: Calculate the remaining hours.

# Step 3: Decide if target has been met or not.

# Step 4: Display appropriate statement based on decision made.