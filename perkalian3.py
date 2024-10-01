"""
Program   : Perkalian 3
Deskripsi : Menghitung perkalian bilangan integer dengan 3
NIM/Nama  : 24060124120013/Muhamad Kemal Faza
Tanggal   : 02/10/2024

**************************************************************
DEFINISI DAN SPESIFIKASI
kali3 : integer > 0 ---> integer
    kali3(n) mengalikan n dengan 3
    f(1) = 3
    f(n) = f(n-1) + 3

**************************************************************

REALISASI
**************************************************************
"""


def kali3(n):
    if n == 1:  # basis
        return 3
    else:  # rekurens
        return kali3(n - 1) + 3


print(kali3(4))
