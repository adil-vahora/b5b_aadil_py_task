admin = {"read", "write", "delete"}
editor = {"read", "write"}

action = "delete"

if action in editor:
    print("Allowed")
else:
    print("Not Allowed")