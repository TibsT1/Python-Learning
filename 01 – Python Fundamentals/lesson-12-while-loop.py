current_session = 1
total_sessions = 4

# Your program should:
# 1. Use a while loop that runs once for each study session.
# 2. Print "Starting study session X" during each repetition, where X is the current session number.
# 3. Increase current_session by one during every repetition.
# 4. Print "All study sessions completed." after the loop finishes.
# 5. Print the final value of current_session.
# Do not manually write four separate print() statements.

while current_session <= total_sessions:
    print(f"Starting study session {current_session}")
    current_session = current_session + 1

print("All study sessions completed.")
print(current_session)