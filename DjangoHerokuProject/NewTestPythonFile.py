count = int(input())
dots = [input() for i in range(count)]
first = 0
second = 0
third = 0
fourth = 0

for dot in dots:
    coordinats = dot.split(' ')
    if '0' not in coordinats:
        if eval(coordinats[0]) > 0 and eval(coordinats[-1]) > 0:
            first += 1
        elif eval(coordinats[0]) < 0 and eval(coordinats[-1]) < 0:
            third += 1
        elif eval(coordinats[0]) > 0:
            fourth += 1
        elif eval(coordinats[0]) < 0:
            second += 1

print(f'Первая четверть: {first}\n'
      f'Вторая четверть: {second}\n'
      f'Третья четверть: {third}\n'
      f'Четвертая четверть: {fourth}')