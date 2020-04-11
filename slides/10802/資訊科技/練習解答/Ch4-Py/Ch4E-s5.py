def recursive_add(n):
    if n <= 2:
        return 5
    return n + recursive_add(n - 3)
print(recursive_add(15))
