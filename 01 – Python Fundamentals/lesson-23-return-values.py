planned_hours = 24
completed_hours = 17
number_of_days = 4

# Your program should:

# 1. Define a function called calculate_remaining_hours.

# 2. Give it two parameters called planned and completed.

# 3. Inside the function, calculate planned minus completed.

# 4. Return the calculated remaining hours.

# 5. Define a function called calculate_average_hours.

# 6. Give it two parameters called total_hours and days.

# 7. Inside the function, calculate the average hours per day.

# 8. Return the calculated average.

# 9. Call calculate_remaining_hours using planned_hours and completed_hours.

# 10. Store the returned value in a variable called remaining_hours.

# 11. Call calculate_average_hours using planned_hours and number_of_days.

# 12. Store the returned value in a variable called average_hours_per_day.

# 13. Print "Hours remaining: X" using the returned value.

# 14. Print "Average planned hours per day: X" using the returned value.

# 15. Use an if statement to print "More study is required." when remaining_hours is greater than 0.

# Use return inside both functions.

# Do not print the calculated values from inside the functions.

# Do not manually type 7 or 6.0 in the final output.


def calculate_remaining_hours(planned, completed):
    total = planned - completed
    return total

def calculate_average_hours(total_hours, days):
    total_average = total_hours / days
    return total_average

remaining_hours = calculate_remaining_hours(planned_hours, completed_hours)
average_hours_per_day = calculate_average_hours(planned_hours, number_of_days)

print(f"Hours remaining: {remaining_hours}")
print(f"Average planned hours per day: {average_hours_per_day}")

if remaining_hours > 0:
    print("More study is required.")