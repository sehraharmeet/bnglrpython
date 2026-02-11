class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, otr):
        print(self.amount , "---", otr.amount)
        return Money(self.amount + otr.amount)

m1 = Money(500)
m2 = Money(700)
m3 = Money(300)

print((m1 + (m2 + m3)).amount)

