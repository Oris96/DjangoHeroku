numbers = input().split(' ')

for i in range(int(len(numbers) / 2)):
    numbers.append(numbers.pop(1))
    numbers.append(numbers.pop(0))

if len(numbers) % 2:
    numbers.append(numbers.pop(0))

print(' '.join(numbers))
