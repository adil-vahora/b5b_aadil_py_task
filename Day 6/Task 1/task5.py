n=input('Enter file name: ')
with open(n, "r") as file:
    content = file.read()

words = content.split()

print("Total number of words:", len(words))