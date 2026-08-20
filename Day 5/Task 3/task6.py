class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies are different")

        return self.amount < other.amount

    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies are different")

        return self.amount > other.amount


money1 = Money(500, "INR")
money2 = Money(1000, "INR")

print(money1 < money2)
print(money1 > money2)