def kali3(n):
    if n == 1:
        return 3
    return kali3(n - 1) + 3


print(kali3(4))
