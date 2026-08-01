# 1. Store " cybersecurity analyst " in a variable.
raw_target_role = "  cybersecurity analyst  "

# 2. Remove the surrounding spaces.
clean_target_role = raw_target_role.strip()

# 3. Convert the cleaned text to title case.
formatted_target_role = clean_target_role.title()

# 4. Create an uppercase version.
uppercase_target_role = clean_target_role.upper()

# 5. Print the original, cleaned, title-case, and uppercase versions with clear labels.
print("Original Version:", raw_target_role)
print("No Spaces Version:", clean_target_role)
print("Formatted Version:", formatted_target_role)
print("Uppercase Version:", uppercase_target_role)

# 6. Print the original variable again at the end to prove it was not automatically changed.
print("Still The Original Version:", raw_target_role)