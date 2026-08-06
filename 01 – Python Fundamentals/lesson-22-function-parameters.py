student_name = "Tibi"
completed_lessons = 21
total_lessons = 26
current_topic = "Function parameters"

# Your program should:

# 1. Define a function called display_student.

# 2. Give display_student one parameter called name.

# 3. Inside display_student, print "Student: X" using an f-string.

# 4. Define a function called display_progress.

# 5. Give display_progress two parameters called completed and total.

# 6. Inside display_progress, print "Progress: X/Y lessons" using an f-string.

# 7. Define a function called display_topic.

# 8. Give display_topic one parameter called topic.

# 9. Inside display_topic, print "Current topic: X" using an f-string.

# 10. Print "Learning report started." before calling the functions.

# 11. Call display_student using student_name as the argument.

# 12. Call display_progress using completed_lessons and total_lessons as arguments.

# 13. Call display_topic using current_topic as the argument.

# 14. Print "Learning report finished." after the function calls.

# Define every function before calling it.

# Use the supplied variables as arguments.

# Do not manually type "Tibi", 21, 26, or "Function parameters" inside the function calls.

def display_student(name):
    print(f"Student: {name}")

def display_progress(completed, total):
    print(f"Progress: {completed}/{total}")

def display_topic(topic):
    print(f"Current topic: {topic}")

print("Learning report started.")

display_student(student_name)
display_progress(completed_lessons, total_lessons)
display_topic(current_topic)

print("Learning report finished.")