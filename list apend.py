list1=[]
for i in range(10):
    sayi=int(input(f"{i+1}. ededi daxil edin"))
    list1.append(sayi)
    cut_sayi_sayisi=0
    for i in list1:
        if i %2 ==0:
            cut_sayi_sayisi +=1
 print(cut_sayi_sayisi)