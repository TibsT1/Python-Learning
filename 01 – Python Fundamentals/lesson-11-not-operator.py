study_target_completed = False
has_free_evening = True

# Your program should:
# 1. Print both Boolean values using f-strings.
# 2. Use not to print "The study target is still incomplete."
# 3. Use and together with not to print "A study session can be completed tonight." when there is a free evening and the target is incomplete.
# 4. Print "Availability check finished." regardless of the result.
# Do not use == False, elif, or else.

print(f"Study Target Complete: {study_target_completed}")
print(f"Has Free Evening: {has_free_evening}")

if not study_target_completed:
    print("The study target is still incomplete.")

if has_free_evening and not study_target_completed:
    print("A study session can be completed tonight.")

print("Availability check finished.")