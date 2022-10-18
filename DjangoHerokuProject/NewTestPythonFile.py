rows = int(input())
numbers = [int(input()) for i in range(rows)]
composition = int(input())
result = 'НЕТ'

while len(numbers) > 1:
    comps = [numbers[0] * i for i in numbers[1:]]
    if composition in comps:
        result = 'ДА'
        break
    else:
        numbers.pop(0)

print(result)