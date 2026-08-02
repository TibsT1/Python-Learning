first_day = 1
final_day = 5
hours_per_day = 2

# Your program should:
# 1. Use a for loop with range() to repeat once for days 1 through 5.
# 2. Print "Day X: Study for 2 hours." during each repetition.
# 3. Use the loop variable for X instead of manually writing each day.
# 4. Calculate the total planned study hours after the loop.
# 5. Print "Total planned hours: X" using an f-string.
# 6. Print "Study plan created." after everything else.
# Do not write five separate print() statements.

for day_number in range(first_day, final_day + 1):
    print(f"Day {day_number}: Study for 2 hours.")
    total_planned_hours = day_number * hours_per_day

print(f"Total Planned Study Hours: {total_planned_hours}")
print("Study plan created.")