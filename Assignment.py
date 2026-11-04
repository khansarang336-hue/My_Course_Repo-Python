# Prompt for file name and handle default option
name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except FileNotFoundError:
    print(f"File could not be opened: {name}")
    quit()

# Dictionary to map sender email to message count
sender_counts = dict()

# Read through the file line by line
for line in handle:
    # Look for lines starting with 'From ' (note the space, avoid 'From:')
    if not line.startswith("From "):
        continue

    # Split the line into words and extract the second word (the email address)
    words = line.split()
    email = words[1]

    # Update the count in the dictionary using the get method
    sender_counts[email] = sender_counts.get(email, 0) + 1

# Maximum loop variables to find the most prolific committer
max_sender = None
max_count = None

# Read through the dictionary to find the largest value
for email, count in sender_counts.items():
    if max_count is None or count > max_count:
        max_sender = email
        max_count = count

# Print the final result
print(max_sender, max_count)
