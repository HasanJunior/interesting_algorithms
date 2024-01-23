# -*- coding: utf-8 -*-
"""
Kompyuter bilan son topish o'yini

@author: Hasanning
"""

import random

#kompAcholari = 0
#foydalanuvchiAchkolari = 0

print("Kelin o`ylagan sonni topish o`yinini o`ynaymiz \n")

while True:
    
    kompOylaganSon = random.randint(0,10) # 0 va 10 oralig'ida tasodifiy son
    tahminQilinganSon = int(input("0 dan 10 gacha son o`yladim topa olasizmi? \n>>>"))
    foydalanuvchiTahminlariSoni = 0

        
    while True:
        if kompOylaganSon == tahminQilinganSon:
            print("to`g`ri topdingiz! \n")
            foydalanuvchiTahminlariSoni += 1;
            print(f"{foydalanuvchiTahminlariSoni} ta urinishda topdingiz! \n \n")
            break
        elif kompOylaganSon > tahminQilinganSon :
            tahminQilinganSon = int(input("men oylagan son bundan katta, ya`na urinib ko`ring:"))
            foydalanuvchiTahminlariSoni += 1;
            continue
        else:
            tahminQilinganSon = int(input("men oylagan son bundan kichik, ya`na urinib ko`ring:"))
            foydalanuvchiTahminlariSoni += 1;
            continue
        
        
    print("-------------------------- \n")
    
    kompQidirayotganSon = random.randint(0, 10)
    soroqnatijasi = '';
    kompTahminlariSoni = 0;

    rightBorder = 10;
    leftBorder = 0;

    print("Bir son o'ylang (0 va 10  sonlari orasidan) \n")
    print("Men uni nechi ekanligini tahmin qilaman, \nsiz o'ylagandan kichik son aytsam - bosasiz, katta bo`lsa + to`g`ri bo`lsa: t \n")

    while True:
        
        soroqnatijasi = input(f"Siz o`ylagan son {kompQidirayotganSon}mi? (T/+/-)")
        
        if soroqnatijasi.title() == "T":
            print("Ure topdim \n")
            kompTahminlariSoni += 1
            print(f"tahminlar soni {kompTahminlariSoni} \n \n")
            break 
        elif soroqnatijasi.title() == "+":
            leftBorder = kompQidirayotganSon + 1
            kompQidirayotganSon = random.randint(kompQidirayotganSon + 1, rightBorder)
            kompTahminlariSoni += 1
            continue
        else:
            rightBorder = kompQidirayotganSon - 1
            kompQidirayotganSon = random.randint(leftBorder, kompQidirayotganSon - 1)
            kompTahminlariSoni += 1 
            continue
    
    print("-------------------------- \n")
        
        
    if kompTahminlariSoni < foydalanuvchiTahminlariSoni:
        print(f"Sizdan ko'ra \n{foydalanuvchiTahminlariSoni - kompTahminlariSoni}ga kam urinishda topdim \n men yutdim )")
    elif kompTahminlariSoni > foydalanuvchiTahminlariSoni:
        print(f"Siz mendan ko'ra \n{kompTahminlariSoni - foydalanuvchiTahminlariSoni}ga kam urinishda topdingiz \n siz g`olibsiz (")
    else:
        print("Durrang bo'ldi")
        
    a = input('yana o`ynaymizmi (ha / yoq)')
    
    if a == "ha":
         continue
    else:
        break

        
    
    
    