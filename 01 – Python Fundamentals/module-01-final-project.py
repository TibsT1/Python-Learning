planned_hours = 24
completed_lessons = 26
has_free_evening = True
review_rounds = 3

module_details = ("Module 1", 26)

study_topics = [
    "variables",
    "conditions",
    "loops",
    "collections",
    "functions",
]

completed_topics = {
    "variables",
    "conditions",
    "loops",
    "loops",
}

required_topic = "functions"


# Functions:

# 1. Define calculate_remaining_hours with planned and completed parameters.

# 2. Calculate planned minus completed inside the function.

# 3. Return the result.


# 4. Define calculate_progress_percentage with completed and planned parameters.

# 5. Calculate completed divided by planned, multiplied by 100.

# 6. Return the percentage.


# 7. Define display_study_topics with one parameter called topics.

# 8. Use a for loop inside it to print "Studied topic: X" for every topic.


# 9. Define display_review_rounds with one parameter called total_rounds.

# 10. Create a counter beginning at 1.

# 11. Use a while loop to print "Review round X" through total_rounds.

# 12. Increase the counter during every repetition.


# Main program:

# 13. Print a heading using "=" repeated 35 times.

# 14. Print the module name and total lesson count by accessing module_details.


# 15. Ask the user to enter their name.

# 16. Clean the name using strip() and title().

# 17. Store the cleaned result in student_name.


# 18. Ask the user to enter their completed study hours.

# 19. Store the original text in raw_completed_hours.


# 20. Use try and except ValueError for the conversion.


# Successful-input path:

# 21. Convert raw_completed_hours into an integer called completed_hours.

# 22. Call calculate_remaining_hours and store its returned value.

# 23. Call calculate_progress_percentage and store its returned value.


# 24. Create a dictionary called student_profile.

# 25. Store student_name, completed_lessons, completed_hours, and the module name in it.


# 26. Add required_topic to completed_topics using add().

# 27. Append "exceptions" to study_topics.


# 28. Print the student's name by accessing student_profile.

# 29. Print the completed lesson count by accessing student_profile.

# 30. Print the completed study hours.

# 31. Print the progress percentage.


# 32. Use if, elif, and else to report progress:

# 33. Print "Weekly target completed." when completed_hours is at least planned_hours.

# 34. Print "Nearly complete." when completed_hours is at least 18 but below the target.

# 35. Otherwise, print "More study is required."


# 36. Print remaining hours only when the target is incomplete.


# 37. Create a Boolean variable called target_completed using a comparison.

# 38. Use and together with not to print "A study session is available tonight."

# 39. It should print only when there is a free evening and the target is incomplete.


# 40. Use in to check whether required_topic exists in completed_topics.

# 41. When present, print "Required topic completed: X" using an f-string.


# 42. Call display_study_topics using study_topics.

# 43. Call display_review_rounds using review_rounds.


# Invalid-input path:

# 44. Use except ValueError to print "Invalid input. Enter a whole number."


# Final output:

# 45. Print the heading again after the try and except blocks.

# 46. Print "Study progress tracker finished." after the heading.


# Requirements:

# Define all functions before the main program.

# Use return in both calculation functions.

# Use both a for loop and a while loop.

# Use a list, tuple, set, and dictionary.

# Use input, int(), try, and except ValueError.

# Do not use a bare except.

# Do not hard-code calculated answers.

# Keep repeated code inside loops.

# Keep one-time summary output outside loops.

def calculate_remaining_hours(planned, completed):
    remaining_hours = planned - completed
    return remaining_hours

def calculate_progress_percentage(completed, planned):
    progress_percentage = completed / planned * 100
    return progress_percentage

def display_study_topics(topics):
    for topics in study_topics:
        print(f"Studied topic: {study_topics}")

def display_review_rounds(total_rounds):
    counter = 1
    while counter <= total_rounds:
        print(f"Review round {counter}")
        counter = counter + 1

heading = "=" * 35
print(heading)
print(f"Module Name: {module_details[0]}")
print(f"Total lessons: {module_details[1]}")

user_name = input("Enter your name: ")
cleaned_user_name = user_name.strip()
student_name = cleaned_user_name.title()

raw_completed_hours = input("Enter completed study hours: ")

try:
    completed_hours = int(raw_completed_hours)

    remaining_hours = calculate_remaining_hours(planned_hours, completed_hours)

    progress_percentage = calculate_progress_percentage(completed_hours, planned_hours)

    student_profile = {
        "name": student_name,
        "completed lessons": completed_lessons,
        "completed hours": completed_hours,
        "module name": module_details[0]
    }

    completed_topics.add(required_topic)

    study_topics.append("exceptions")

    print(f"Student name: {student_profile['name']}")

    print(f"Completed Lessons: {student_profile['completed lessons']}")

    print(f"Completed study hours: {student_profile['completed hours']}")

    print(f"Progress percentage: {progress_percentage}")

    if completed_hours >= planned_hours:
        print("Weekly target completed.")
        target_completed = True
    elif completed_hours >= 18:
        print("Nearly complete.")
        target_completed = False
        print(f"Remaining hours: {remaining_hours}")
    else:
        print("More study is required.")
        target_completed = False
        print(f"Remaining hours: {remaining_hours}")

    if not target_completed and has_free_evening:
        print("A study session is available tonight.")

    if required_topic in completed_topics:
        print(f"Required topic completed: {required_topic}")

    display_study_topics(study_topics)
    display_review_rounds(review_rounds)

except ValueError:
    print("Invalid input. Enter a whole number.")

print(heading)
print("Study progress tracker finished.")