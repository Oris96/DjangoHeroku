from re import search

number = int(input())
result = [print(i + 1, end=" ") for i in range(number) if search(r'a.*n.*t.*o.*n', input())]
