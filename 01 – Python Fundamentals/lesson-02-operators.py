# 1. Store the number of study days in a variable.
study_days = 4

# 2. Store the planned hours per day.
planned_study_hours = 6

# 3. Calculate the total planned study hours.
total_planned_study_hours = planned_study_hours * study_days

# 4. Store the number of completed hours.
completed_hours = 12

# 5. Calculate how many hours remain.
remaining_hours = total_planned_study_hours - completed_hours

# 6. Calculate the average planned hours per day.
average_planned_hours = total_planned_study_hours / study_days

# 7. Calculate how many complete four-hour study blocks fit into the total.
complete_blocks = total_planned_study_hours // 4

# 8. Calculate how many hours remain after forming those four-hour blocks.
remaining_hours_after_blocks = total_planned_study_hours % 4

# 9. Print every calculated result with a clear label.
print("Study Days: ", study_days)
print("Planned Study Hours Per Day: ", planned_study_hours)
print("Total Planned Study Hours: ", total_planned_study_hours)
print("Completed Hours: ", completed_hours)
print("Remaining Hours: ", remaining_hours)
print("Average Planned Hours: ", average_planned_hours)
print("Complete Four-Hour Blocks: ", complete_blocks)
print("Remaining Hours After Four-Hour Blocks: ", remaining_hours_after_blocks)