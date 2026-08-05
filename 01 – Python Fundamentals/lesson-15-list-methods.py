learning_tools = ["Python", "VS Code", "PowerShell"]
new_tool = "GitHub Desktop"
temporary_tool = "Notepad"

# Your program should:
# 1. Print the original learning_tools list.
# 2. Add new_tool to the end using append().
# 3. Insert temporary_tool at index 1 using insert().
# 4. Print the updated list.
# 5. Remove temporary_tool using remove().
# 6. Remove the first item using pop() and store it in removed_tool.
# 7. Print the final list.
# 8. Print the value stored in removed_tool.
# 9. Print the number of remaining tools using len().
# Do not create a second list.
# Do not type "GitHub Desktop" or "Notepad" directly inside the list methods.

print(learning_tools)
learning_tools.append(new_tool)
learning_tools.insert(1, temporary_tool)
print(learning_tools)
learning_tools.remove(temporary_tool)
removed_tool = learning_tools.pop(0)
print(learning_tools)
print(removed_tool)
print(len(learning_tools))