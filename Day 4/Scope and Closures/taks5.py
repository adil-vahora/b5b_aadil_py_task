mode = "Global"


def outer():
    mode = "Outer"

    def inner():
        mode = "Inner"
        print("Inner mode:", mode)

    print("Outer mode:", mode)
    inner()


print("Global mode:", mode)
outer()