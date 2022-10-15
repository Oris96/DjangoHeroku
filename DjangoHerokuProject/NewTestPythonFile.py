number = input()
reversed_number = number[::-1] if len(number) == 5 else number[0] + number[1:][::-1]
print(int(reversed_number))


