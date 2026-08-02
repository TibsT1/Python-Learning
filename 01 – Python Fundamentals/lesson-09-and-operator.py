completed_hours = 18
minimum_hours = 15
target_hours = 20

# Your program should:
# 1. Print all three values using f-strings.
# 2. Use one if statement with and.
# 3. Print "You are within the nearly-complete range." only when completed hours are at least the minimum and below the target.
# 4. Print "Range check finished." regardless of the result.
# Do not use elif or else in this exercise.

print(f"Completed Hours: {completed_hours}")
print(f"Minimum Hours: {minimum_hours}")
print(f"Target Hours: {target_hours}")

if completed_hours >= minimum_hours and completed_hours < target_hours:
    print("You are within the nearly-complete range.")

print("Range check finished.")