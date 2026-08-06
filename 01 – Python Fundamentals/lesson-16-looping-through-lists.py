study_topics = ["variables", "conditions", "while loops", "for loops", "lists"]

# Your program should:
# 1. Print the complete study_topics list.
# 2. Use a for loop to visit every item in study_topics.
# 3. During each repetition, print "Reviewing topic: X".
# 4. Use the current list item for X.
# 5. Print "All topics reviewed." once after the loop.
# 6. Print the total number of topics using len().
# Keep repeated code inside the loop.
# Keep the final messages outside the loop.
# Do not use range() or manually access individual indexes.

print(study_topics)

for topic in study_topics:
    print(f"Reviewing topic: {topic}")

print("All topics reviewed.")
print(f"Total number of topics: {len(study_topics)}")