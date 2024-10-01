def sumDeret(n):
    if n == 1:
        return 3
    else:
        return sumDeret(n - 1) + (n * 3)


print(sumDeret(2))
