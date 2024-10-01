def bagi(x, y):
    if x < y:
        return 0
    return bagi(x - y, y) + 1


print(bagi(10, 2))
