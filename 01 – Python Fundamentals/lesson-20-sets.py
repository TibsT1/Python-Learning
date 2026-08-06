completed_topics = {"variables", "conditions", "loops", "loops"}
new_topic = "lists"
topic_to_remove = "conditions"
required_topic = "loops"

# Your program should:

# 1. Print the number of unique topics using len().

# 2. Add new_topic to completed_topics using add().

# 3. Add "variables" again using add() to demonstrate that duplicates are ignored.

# 4. Remove topic_to_remove using remove().

# 5. Use in to check whether required_topic exists in completed_topics.

# 6. When it exists, print "Required topic completed: X" using an f-string.

# 7. Use not in to check whether topic_to_remove is now missing.

# 8. When it is missing, print "Topic successfully removed: X" using an f-string.

# 9. Print the final number of unique topics.

# 10. Print the complete final set.

# Do not access the set using an index.

# Do not create a second set.

# Remember that the final set order may vary.

print(len(completed_topics))

completed_topics.add(new_topic)

completed_topics.add("variables")

completed_topics.remove(topic_to_remove)

if required_topic in completed_topics:
    print(f"Required topic completed: {required_topic}")

if topic_to_remove not in completed_topics:
    print(f"Topic successfully removed: {topic_to_remove}")

print(len(completed_topics))

print(completed_topics)