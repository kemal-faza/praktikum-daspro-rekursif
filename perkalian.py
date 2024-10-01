"""
Program   : Perkalian
Deskripsi : Menghitung perkalian dua bilangan integer
NIM/Nama  : 24060124120013/Muhamad Kemal Faza
Tanggal   : 02/10/2024

**************************************************************
DEFINISI DAN SPESIFIKASI
kali : 2 integer > 0 ---> integer > 0
    kali(x, y) mengalikan x dengan y

**************************************************************

REALISASI
**************************************************************
"""


def kali(x, y):
    if y == 0:  # basis
        return 0
    else:  # rekurens
        return kali(x, y - 1) + x


print(kali(10, 5))
