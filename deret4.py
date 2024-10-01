"""
Program   : Deret
Deskripsi : Menghitung jumlah bilangan suatu deret
NIM/Nama  : 24060124120013/Muhamad Kemal Faza
Tanggal   : 02/10/2024

**************************************************************
DEFINISI DAN SPESIFIKASI
sumDeret : integer > 0 ---> integer > 0
    sumDeret(n) menghitung jumlah bilangan dari suku pertama ke suku ke-n
    s(1) = 1
    s(2) = 1 + 4
    s(3) = 1 + 4 + 9

**************************************************************

REALISASI
**************************************************************
"""


def sumDeret(n):
    if n == 1:  # basis
        return 1
    else:  # rekurens
        return n**2 + sumDeret(n - 1)


print(sumDeret(4))
