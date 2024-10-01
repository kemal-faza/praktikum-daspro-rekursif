def sumDeret(n):
    if n == 1:
        return 1
    else:
        return sumDeret(n - 1) + 3 ** (n - 1)


print(sumDeret(4))
