"""
Program   : Tipe Garis
Deskripsi : Menentukan tipe garis yang terdiri dari dua titik yaitu titik awal dan titik akhir
NIM/Nama  : 24060124120013/Muhamad Kemal Faza
Tanggal   : 29/09/2024

**************************************************************
DEFINISI DAN SPESIFIKASI
type garis : < p1 : point, p2 : point >
    <p1, p2> adalah sebuah garis yang terdiri dari dua titik yaitu titik awal (p1) dan titik akhir (p2)

**************************************************************

REALISASI
**************************************************************
"""


def kurang(x, y):
    if y == 0:
        return x
    return kurang(x, y - 1) - 1


print(kurang(7, 5))
