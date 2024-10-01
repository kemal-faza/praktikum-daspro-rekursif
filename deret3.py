"""
Program   : Deret Geometri
Deskripsi : Menghitung jumlah bilangan suatu deret geometri
NIM/Nama  : 24060124120013/Muhamad Kemal Faza
Tanggal   : 02/10/2024

**************************************************************
DEFINISI DAN SPESIFIKASI
sumDeret : integer > 0 ---> integer > 0
    sumDeret(n) menghitung jumlah bilangan dari suku pertama hingga suku ke-n
    s(1) = 1
    s(2) = 1 + 3
    s(3) = 1 + 3 + 9
    s(4) = 1 + 3 + 9 + 27

**************************************************************

REALISASI
**************************************************************
"""


def sumDeret(n):
    if n == 1:  # basis
        return 1
    else:  # rekurens
        return sumDeret(n - 1) + 3 ** (n - 1)


print(sumDeret(4))
