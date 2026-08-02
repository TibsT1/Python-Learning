student_name = "Tibi"
planned_hours = 20
completed_hours = 16
has_free_evening = True
first_day = 1
final_day = 3

# Your program should:
# 1. Print the student's name, planned hours, and completed hours using f-strings.
# 2. Calculate the remaining hours.
# 3. Use if, elif, and else to print:
#    - "Target completed." when completed hours are at least the planned hours.
#    - "Nearly complete." when completed hours are at least 15 but below the target.
#    - "More study is required." otherwise.
# 4. Print the remaining hours only when the target is incomplete.
# 5. Use and together with not to print "A study session is available tonight." when there is a free evening and the target is not complete.
# 6. Use a for loop with range() to print "Planned study day X" for days 1 through 3.
# 7. Use a while loop to count from 1 through 3 and print "Review round X".
# 8. Print "Halfway recap complete." after both loops finish.
# 9. Keep code that should repeat inside its loop.
# 10. Keep code that should run once outside the loops.

target_complete = completed_hours >= planned_hours
review_round = 1

print(f"Student Name: {student_name}")
print(f"Planned Hours: {planned_hours}")
print(f"Completed Hours: {completed_hours}")

remaining_hours = planned_hours - completed_hours

if target_complete:
    print("Target completed.")
elif completed_hours >= 15:
    print("Nearly complete.")
    print(f"Remaining hours: {remaining_hours}")
else:
    print("More study is required.")
    print(f"Remaining Hours: {remaining_hours}")

if has_free_evening and not target_complete:
    print("A study session is available tonight.")

for day_number in range(first_day, final_day + 1):
    print(f"Planned study day {day_number}")

while review_round <= 3:
    print(f"Review round {review_round}")
    review_round = review_round + 1

print("Halfway recap complete.")