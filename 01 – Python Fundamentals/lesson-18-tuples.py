server_address = ("192.168.1.50", 8080)
allowed_statuses = ("pending", "approved", "rejected")
required_status = "approved"

# Your program should:
# 1. Print the complete server_address tuple.
# 2. Print the IP address using its positive index.
# 3. Print the port number using its positive index.
# 4. Print the final item in allowed_statuses using a negative index.
# 5. Print the number of items in allowed_statuses using len().
# 6. Use in to check whether required_status exists in allowed_statuses.
# 7. When it exists, print "Required status is allowed: X" using an f-string.
# 8. Print the type of server_address.
# Do not attempt to modify either tuple.
# Do not manually type "approved" inside the membership condition.

print(server_address)
print(server_address[0])
print(server_address[1])
print(len(allowed_statuses))

if required_status in allowed_statuses:
    print(f"Required status is allowed: {required_status}")

print(type(server_address))