# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:13:18 2022

@author: ASUS
"""

print ("===== MENGHITUNG LUAS RUANGAN =====")
p = float(input("Masukkan panjang ruangan = "))
l = float(input("Masukkan lebar ruangan = "))
s = input("Pilih satuan(meter/inci) = ")

if  (s == 'meter') :
    h = p * l
elif (s == 'inci') : 
    h = p * l * 39.37
#else : print("Maaf, hanya bisa meter atau inci") 

print ("\npanjang ruangan = ", p)
print ("Lebar ruangan = ", l)
print ("Luas ruangan = ",h,s)
