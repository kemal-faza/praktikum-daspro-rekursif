def pangkat(x, y):
    if y == 0:
        return 1
    return pangkat(x, y - 1) * x


print(pangkat(2, 6))
