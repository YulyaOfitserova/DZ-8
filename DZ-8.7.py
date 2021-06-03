class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f'Сумма: {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        return f'Произведение: {self.x * other.x - (self.y * other.y)} + {self.y * other.x} * i'


complex1 = ComplexNumber(1, 2)
complex2 = ComplexNumber(1, 2)
print(complex1 + complex2)
print(complex1 * complex2)
