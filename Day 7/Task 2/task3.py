import sys

if len(sys.argv) != 4:
    print("Error: Please provide a number, operator, and another number.")
    sys.exit()

num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
else:
    print("Error: Operator must be + or -.")