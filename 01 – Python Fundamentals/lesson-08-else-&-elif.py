planned_hours = 20
completed_hours = 17

# 1. Calculate the remaining hours.
remaining_hours = planned_hours - completed_hours

# 2. Print the planned and completed hours using f-strings.
print(f"Planned Hours: {planned_hours}")
print(f"Completed Hours: {completed_hours}")

# 3. Print "Target completed." when completed hours are at least 20.
if completed_hours >= 20:
    print("Target completed.")

# 4. Print "Nearly complete." when completed hours are at least 15 but below 20.
elif completed_hours >= 15:
    print("Nearly complete.")
    print(f"Remaining Hours: {remaining_hours}")

# 5. Otherwise, print "More study is required."
else:
    print("More study is required.")

# 6. Print the remaining hours only when the target is not complete.
    print(f"Remaining Hours: {remaining_hours}")

# 7. Print "Progress check finished." at the end.
print("Progress check finished.")