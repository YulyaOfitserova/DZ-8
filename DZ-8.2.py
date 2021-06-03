class DivError(Exception):
    def __init__(self, txt):
        self.txt = txt


num1 = input("Введите любое действительное число: ")
num2 = input("Введите число отличное от нуля: ")

try:
    num1 = int(num1)
    num2 = int(num2)

    if num2 == 0:
        raise DivError("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except DivError as err:
    print(err)
else:
    res = round(num1 / num2, 4)
    print(f"Результат деления: {res}")

