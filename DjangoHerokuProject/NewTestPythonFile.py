timur, ruslan = input(), input()

figure = ['ножницы', 'бумага', 'камень', 'ящерица', 'Спок']
winner = ['ничья', 'Руслан', 'Тимур', 'Руслан', 'Тимур']

print(winner[figure.index(timur) - figure.index(ruslan)])
