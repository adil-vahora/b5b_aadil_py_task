with open("my_story.txt", "r") as file:
    for line in file:
        line = line.strip()
        print(line, "-", len(line), "characters")