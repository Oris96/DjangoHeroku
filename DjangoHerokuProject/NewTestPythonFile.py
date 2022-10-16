def joseph(n, k):
    return (joseph(n - 1, k) + k - 1) % n + 1 if n > 1 else 1


n = int(input())
k = int(input())
print(joseph(n, k))
