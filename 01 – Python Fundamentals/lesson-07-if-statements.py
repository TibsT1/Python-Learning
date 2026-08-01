# 1. Store the planned weekly study hours.
planned_weekly_study_hours = 21

# 2. Store the completed study hours.
completed_study_hours = 15

# 3. Calculate the remaining hours.
remaining_study_hours = planned_weekly_study_hours - completed_study_hours

# 4. Print the planned and completed hours using f-strings.
print(f"Planned Weekly Study Hours: {planned_weekly_study_hours}")
print(f"Completed Study Hours This Week: {completed_study_hours}")

# 5. Use an if statement to print "Weekly target completed!" when completed hours are greater than or equal to planned hours.
if completed_study_hours >= planned_weekly_study_hours:
    print("Weekly target completed!")

# 6. Use another if statement to print the remaining hours when completed hours are less than planned hours.
if planned_weekly_study_hours > completed_study_hours:
    print(f"Remaining Weekly Study Hours: {remaining_study_hours}")

# 7. Print "Progress check finished." regardless of the result.
print("Progress check finished.")