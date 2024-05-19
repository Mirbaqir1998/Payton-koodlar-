# 2 eded daxil ediler,  bu edelerden birincisi axtarlaan   eded  2 ncisi saydi bu say qeder eded daxil edib axtralan ededen bu ededler icersinde nece dedene olan kodu yazin

a=int(input("axdaranacaxiniz  eded "))
b=int(input("say"))
count=0
for i in range(b):
    num=int(input(f"{i+1}-ci ededi daxil edin:"))
    if num==a:
        count+=1
print(f"axtarilan ededden{count}- dene  tapildi")
 
