"""
Program   : Pembagian
Deskripsi : Menghitung pembagian dua bilangan integer
NIM/Nama  : 24060124120013/Muhamad Kemal Faza
Tanggal   : 02/10/2024

**************************************************************
DEFINISI DAN SPESIFIKASI
bagi : 2 integer > 0 ---> integer > 0
    bagi(x, y) membagi x dengan y

**************************************************************

REALISASI
**************************************************************
"""


def bagi(x, y):
    if x < y:  # basis
        return 0
    else:  # rekurens
        return bagi(x - y, y) + 1


print(bagi(10, 2))
