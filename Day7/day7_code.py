# Challenge - Count word frequencies in a text file

# Step 1: Read the file
file_path = "wikipedia.txt"  # Make sure the file is in the same directory
with open(file_path, 'r') as file:
    text = file.read()

# Step 2: Convert to lowercase
text = text.lower()

# Step 3: Split into words (splits on spaces)
words = text.split()

# Step 4: Count word frequencies using if-else
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Step 5: Print the word frequencies
for word, count in word_count.items():
    print(f"{word}: {count}")

