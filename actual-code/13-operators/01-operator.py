class Quantity:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Quantity):
            return Quantity(self.amount + other.amount)
        elif isinstance(other, int):
            return Quantity(self.amount + other)
        else:
            raise TypeError("Type not supported")

    def __repr__(self):
        return f'Quantity({self.amount})'

    def __lt__(self, other):
        return self.amount < other.amount

    def __eq__(self, other):
        return self.amount == other.amount

q1 = Quantity(10)
q2 = Quantity(5)

q3 = q1 + q2
print(q3)
q4 = q1 + 4
print(q4)

q_list = [q1,q2,q3,q4]
q_list.sort(reverse=True)
print(q_list)

print(q1 < q2)
print(q1 > q2)

print(Quantity(10) < Quantity(10))
print(Quantity(10) > Quantity(10))
print(Quantity(10) == Quantity(10))


