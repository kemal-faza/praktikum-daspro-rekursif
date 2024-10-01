"""
Program   : Deret Aritmatika
Deskripsi : Menghitung jumlah bilangan suatu deret aritmatika
NIM/Nama  : 24060124120013/Muhamad Kemal Faza
Tanggal   : 02/10/2024

**************************************************************
DEFINISI DAN SPESIFIKASI
sumDeret : integer > 0 ---> integer > 0
    sumDeret(n) menghitung jumlah bilangan dari suku pertama hingga suku ke-n
    s(1) = 3
    s(2) = 3 + 6
    s(3) = 3 + 6 + 9

**************************************************************

REALISASI
**************************************************************
"""


def sumDeret(n):
    if n == 1:  # basis
        return 3
    else:  # rekurens
        return sumDeret(n - 1) + (n * 3)


print(sumDeret(2))
