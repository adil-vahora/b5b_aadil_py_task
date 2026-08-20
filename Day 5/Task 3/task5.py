class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.__items:
            return self.__items.pop()
        return "Stack is empty"

    def __str__(self):
        return str(self.__items)


stack = Stack()

stack.push("Adil")
stack.push("Rahim")
stack.push("Alex")

print(stack)

print(stack.pop())

print(stack)