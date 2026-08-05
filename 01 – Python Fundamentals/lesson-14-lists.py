study_topics = ["variables", "conditions", "while loops", "for loops"]
replacement_topic = "lists"

# Your program should:
# 1. Print the complete study_topics list.
# 2. Print the first topic using its positive index.
# 3. Print the final topic using a negative index.
# 4. Print the number of topics using len().
# 5. Replace "while loops" with the value stored in replacement_topic.
# 6. Print the updated complete list.
# 7. Print the newly replaced item using its index.
# Do not create a second list.
# Do not type "lists" directly when replacing the item; use replacement_topic.

print(study_topics)
print(study_topics[0])
print(study_topics[-1])
print(len(study_topics))
study_topics[2] = replacement_topic
print(study_topics)
print(study_topics[2])
