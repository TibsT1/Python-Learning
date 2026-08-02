completed_hours = 8
planned_hours = 20
deadline_is_today = True

#Your program should:
# 1. Print all three values using f-strings.
# 2. Use one if statement with or.
# 3. Print "Study reminder activated." when completed hours are below the planned hours or the deadline is today.
# 4. Print "Reminder check finished." regardless of the condition.
#Do not use elif or else.

print(f"Completed Hours: {completed_hours}")
print(f"Planned Hours: {planned_hours}")
print(f"Is deadline today? {deadline_is_today}")

if completed_hours < planned_hours or deadline_is_today == True:
    print("Study reminder activated.")

print("Reminder check finished.")