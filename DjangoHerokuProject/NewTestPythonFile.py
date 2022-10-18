numbers = input().split(' ')
result = [1 for i in range(1, len(numbers)) if eval(numbers[i]) > eval(numbers[i-1])]
print(len(result))