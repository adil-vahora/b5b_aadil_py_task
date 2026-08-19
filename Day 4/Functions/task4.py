usernames = ["Adil", "Rahim", "Razzak", "Afroz123", "Hasnain"]

long_usernames = list(
    filter(lambda name: len(name) >= 6, usernames)
)

print(long_usernames)