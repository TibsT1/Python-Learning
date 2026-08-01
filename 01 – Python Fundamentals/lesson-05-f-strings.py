# 1. Your first name
first_name = "Tibi"

# 2. Your target role
target_role = "Cybersecurity Analyst"

# 3. Your weekly study hours
weekly_study_hours = 21

# 4. The number of hours completed this week
hours_completed_currently = 9


remaining_study_hours = weekly_study_hours - hours_completed_currently

print(f"My name is {first_name} and I want to work as a {target_role}, to achieve that I plan to study {weekly_study_hours} hours per week and this week I have studied {hours_completed_currently}. I still have {remaining_study_hours} hours left to study this week which places my progress at {hours_completed_currently}/{weekly_study_hours} hours.")