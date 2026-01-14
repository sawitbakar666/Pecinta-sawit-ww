#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program Kalkulator Sederhana
Mendukung operasi: tambah, kurang, kali, bagi, pangkat, akar
"""

import math

def tambah(a, b):
    """Menjumlahkan dua angka"""
    return a + b

def kurang(a, b):
    """Mengurangkan dua angka"""
    return a - b

def kali(a, b):
    """Mengalikan dua angka"""
    return a * b

def bagi(a, b):
    """Membagi dua angka"""
    if b == 0:
        return "Error: Tidak bisa dibagi dengan 0!"
    return a / b

def pangkat(a, b):
    """Memangkatkan angka"""
    return a ** b

def akar(a):
    """Menghitung akar kuadrat"""
    if a < 0:
        return "Error: Tidak bisa menghitung akar dari angka negatif!"
    return math.sqrt(a)

def tampilkan_menu():
    """Menampilkan menu operasi"""
    print("\n" + "="*40)
    print("       PROGRAM KALKULATOR PYTHON")
    print("="*40)
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pangkat (^)")
    print("6. Akar Kuadrat (√)")
    print("7. Keluar")
    print("="*40)

def main():
    """Fungsi utama program"""
    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi (1-7): ").strip()
        
        if pilihan == '7':
            print("\nTerima kasih telah menggunakan kalkulator. Selamat tinggal!")
            break
        
        if pilihan == '6':
            try:
                angka = float(input("Masukkan angka: "))
                hasil = akar(angka)
                print(f"\n√{angka} = {hasil}")
            except ValueError:
                print("\nError: Masukkan angka yang valid!")
            except TypeError:
                print(f"\nHasil: {hasil}")
            continue
        
        if pilihan in ['1', '2', '3', '4', '5']:
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
                
                if pilihan == '1':
                    hasil = tambah(angka1, angka2)
                    operator = "+"
                elif pilihan == '2':
                    hasil = kurang(angka1, angka2)
                    operator = "-"
                elif pilihan == '3':
                    hasil = kali(angka1, angka2)
                    operator = "*"
                elif pilihan == '4':
                    hasil = bagi(angka1, angka2)
                    operator = "/"
                elif pilihan == '5':
                    hasil = pangkat(angka1, angka2)
                    operator = "^"
                
                if isinstance(hasil, str):
                    print(f"\n{hasil}")
                else:
                    print(f"\n{angka1} {operator} {angka2} = {hasil}")
                    
            except ValueError:
                print("\nError: Masukkan angka yang valid!")
        else:
            print("\nError: Pilihan tidak valid! Silakan pilih 1-7.")

if __name__ == "__main__":
    main()
