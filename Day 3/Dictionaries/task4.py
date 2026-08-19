words = ["apple", "ant", "banana", "bat", "cat", "carrot"]

grouped = {}

for word in words:
    first_letter = word[0]
    grouped.setdefault(first_letter, []).append(word)

print(grouped)