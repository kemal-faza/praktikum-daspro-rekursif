def kali(x, y):
    if y == 0:
        return 0
    return kali(x, y - 1) + x


print(kali(10, 5))
