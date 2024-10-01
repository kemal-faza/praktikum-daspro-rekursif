"""
Program   : Pengurangan
Deskripsi : Menghitung pengurangan dua bilangan integer
NIM/Nama  : 24060124120013/Muhamad Kemal Faza
Tanggal   : 02/10/2024

**************************************************************
DEFINISI DAN SPESIFIKASI
kurang : 2 integer > 0 ---> integer
    kurang(x, y) mengurangi x dengan y

**************************************************************

REALISASI
**************************************************************
"""


def kurang(x, y):
    if y == 0:  # basis
        return x
    else:  # rekurens
        return kurang(x, y - 1) - 1


print(kurang(7, 10))
