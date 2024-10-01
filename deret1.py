def sumDeret(n):
    if n == 1:
        return 1
    else:
        return n + sumDeret(n - 1)


print(sumDeret(5))
