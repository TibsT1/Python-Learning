student_profile = {
    "name": "Tibi",
    "completed_lessons": 18,
    "target_role": "Cybersecurity Analyst",
}

new_lesson_total = 19
current_topic = "dictionaries"

# Your program should:

# 1. Print the complete student_profile dictionary.

# 2. Print the student's name by accessing the "name" key.

# 3. Print the current completed lesson count by accessing its key.

# 4. Replace the completed lesson count with new_lesson_total.

# 5. Add a new key called "current_topic" using the value stored in current_topic.

# 6. Print the updated completed lesson count.

# 7. Print the newly added current topic.

# 8. Print the number of key-value pairs using len().

# 9. Print the complete updated dictionary.

# Use the variables new_lesson_total and current_topic when changing the dictionary.

# Do not create a second dictionary.

# Do not manually type 19 or "dictionaries" when updating the dictionary.

print(student_profile)
print(student_profile["name"])
print(student_profile["completed_lessons"])

student_profile["completed_lessons"] = new_lesson_total

student_profile["current_topic"] = current_topic

print(student_profile["completed_lessons"])
print(student_profile["current_topic"])
print(len(student_profile))
print(student_profile)