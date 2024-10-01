"""
Program   : Perpangkatan
Deskripsi : Menghitung perpangkatan dua bilangan integer
NIM/Nama  : 24060124120013/Muhamad Kemal Faza
Tanggal   : 02/10/2024

**************************************************************
DEFINISI DAN SPESIFIKASI
pangkat : 2 integer > 0 ---> integer > 0
    pangkat(x, y) memangkatkan x dengan y

**************************************************************

REALISASI
**************************************************************
"""


def pangkat(x, y):
    if y == 0:  # basis
        return 1
    else:  # rekurens
        return pangkat(x, y - 1) * x


print(pangkat(2, 6))
