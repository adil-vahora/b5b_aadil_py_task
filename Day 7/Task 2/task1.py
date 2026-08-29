import os

if "USER_KEY" in os.environ:
    print(os.environ["USER_KEY"])
else:
    print("Key not found")