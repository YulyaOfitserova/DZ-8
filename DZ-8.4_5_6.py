class EquipmentWarehouse:
    @staticmethod
    def info():
        print('Склад оргтехники')


class OfficeEquipment:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        try:
            self.num = int(input(f'Введите сколько {self.name} поступило на склад: '))
        except ValueError:
            print('Количество - это целое положительное число!')

    def __str__(self):
        return self.name, self.color, self.price, self.num

    def to_the_warehouse(x):
        return dict((key, getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))


class Printer(OfficeEquipment):
    def __init__(self, name, color, price, print_speed):
        super().__init__(name, color, price)
        self.print_speed = print_speed

    def properties_p(self):
        return f'Свойства {self.name}: {self.color}, {self.price}, {self.print_speed}'

    def to_the_warehouse(x):
        return dict((key, getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))


class Scanner(OfficeEquipment):
    def __init__(self, name, color, price, resolution):
        super().__init__(name, color, price)
        self.resolution = resolution

    def properties_p(self):
        return f'Свойства {self.name}: {self.color}, {self.price}, {self.resolution}'

    def to_the_warehouse(x):
        return dict((key, getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))


class Xerox(OfficeEquipment):
    def __init__(self, name, color, price, dpi):
        super().__init__(name, color, price)
        self.dpi = dpi

    def properties_p(self):
        return f'Свойства {self.name}: {self.color}, {self.price}, {self.dpi}'

    def to_the_warehouse(x):
        return dict((key, getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))


txt = EquipmentWarehouse
txt.info()
printer = Printer('принтер Hp', 'black', '100', '20')
scanner = Scanner('сканер HP', 'white', '50', '20')
xerox = Xerox('ксерокс HP', 'red', '30', '10')
print(printer.properties_p())
print(printer.to_the_warehouse())
print(scanner.properties_p())
print(scanner.to_the_warehouse())
print(xerox.properties_p())
print(xerox.to_the_warehouse())


