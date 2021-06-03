class List(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    el = input('Введите целое положительное число или stop для выхода: ')

    try:
        if el == 'stop':
            break
        if not el.isdigit():
            raise List('Введите целое положительное число! ')
        else:
            my_list.append(el)
        print(f'Текущий список: {my_list}')
    except List as err:
        print(err)
print(f'Итоговый список: {my_list}')

