available_topics = ["variables", "conditions", "loops", "lists"]
required_topic = "lists"
future_topic = "functions"

# Your program should:
# 1. Print the complete available_topics list.
# 2. Use in to check whether required_topic exists in available_topics.
# 3. When it exists, print "The required topic is available: X".
# 4. Use not in to check whether future_topic is missing from available_topics.
# 5. When it is missing, print "The future topic has not been added: X".
# 6. Print "Topic availability check finished." once at the end.
# Use the variables required_topic and future_topic inside the conditions.
# Use f-strings for the messages containing X.
# Do not manually access any list indexes.

print(available_topics)
if required_topic in available_topics:
    print(f"The required topic is available: {required_topic}")

if future_topic not in available_topics:
    print(f"The future topic has not been added: {future_topic}")

print("Topic availability check finished")