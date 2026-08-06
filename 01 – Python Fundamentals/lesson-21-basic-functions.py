separator_character = "="
separator_length = 25

# Your program should:

# 1. Define a function called display_separator.

# 2. Inside the function, print separator_character repeated separator_length times.

# 3. Define another function called display_study_message.

# 4. Inside that function, print "Current lesson: Basic functions".

# 5. Print "Program started." before calling either function.

# 6. Call display_separator.

# 7. Call display_study_message.

# 8. Call display_separator again.

# 9. Print "Program finished." after the function calls.

# Each function should be defined before it is called.

# Do not put parameters inside the function parentheses yet.

# Do not manually repeat "=" twenty-five times.

def display_separator():
    print(separator_character * separator_length)

def display_study_message():
    print("Current lesson: Basic functions")

print("Program started.")

display_separator()
display_study_message()
display_separator()

print("Program finished.")