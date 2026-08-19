class OutOfRangeError(Exception):
    pass


while True:
    try:
        number = int(input("Enter a number between 1 and 10: "))

        if number < 1 or number > 10:
            raise OutOfRangeError("Number must be between 1 and 10.")

        print("Valid number:", number)
        break

    except ValueError:
        print("Error: Please enter a number.")

    except OutOfRangeError as error:
        print(error)