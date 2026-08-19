count = 0

def call_counter():
    global count
    count += 1
    print("Function called")

call_counter()
call_counter()
call_counter()
call_counter()

print("Total calls:", count)