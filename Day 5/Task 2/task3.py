class Account:
    def get_interest_rate(self):
        return 4


class SavingsAccount(Account):
    def get_interest_rate(self):
        return 6


class FixedDeposit(Account):
    def get_interest_rate(self):
        return 8


accounts = [
    Account(),
    SavingsAccount(),
    FixedDeposit()
]

for account in accounts:
    print(account.get_interest_rate())