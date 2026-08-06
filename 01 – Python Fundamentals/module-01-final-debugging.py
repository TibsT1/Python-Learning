first_day = 1
final_day = 4
hours_per_day = 2

current_review = 1
final_review = 3

study_topics = ["variables", "conditions", "loops", "functions"]

print("Study plan started.")

for day_number in range(first_day, final_day + 1):
    print(f"Study day {day_number}")

total_planned_hours = final_day * hours_per_day
print(f"Total planned hours: {total_planned_hours}")

while current_review <= final_review:
    print(f"Review round {current_review}")
    current_review = current_review + 1

print(study_topics[3])

print("Study plan finished.")


# Debugging instructions:

# 1. Run the original program.

# 2. Record the exception type and failing line.

# 3. Fix the exception without rewriting the program.

# 4. Identify why the for loop does not include day 4.

# 5. Fix the for loop so it prints days 1 through 4.

# 6. Identify why the while loop does not include review round 3.

# 7. Fix the while loop so it prints rounds 1 through 3.

# 8. Replace the total-hours calculation so it does not depend on the final loop-variable value.

# 9. The total must be calculated from the number of days and hours_per_day.

# 10. Run the corrected program and confirm it finishes.


# Debugging notes:

# Exception type: IndexError

# Failing line: Line 22

# Exception cause: there is no item in index value 4

# Exception fix: replace the 4 in "print(study_topics[4])" with a 3


# For-loop problem: It doesn't include day 4 because for loops only run up to the number before the second value in "range()"

# For-loop fix: To fix it, just do "range(Number1, Number2 + 1)"


# While-loop problem: It doesn't include review round 3 because the loop stops once it reaches 3 because it is told to keep running if VariableA is smaller than VariableB (which is 3)

# While-loop fix: To fix it, instead of "VariableA < VariableB", it should be "VariableA <= VariableB"


# Total-hours problem: I think the problem is that the calculation uses the variable inside the loop

# Total-hours fix: Changed it to use the "final_day" variable instead of the variable inside the loop?