liste1=[1,2,3,4,5,6,7,8,9]
liste2=list()
for eleman in liste1:
    liste2.append(eleman)
print(liste1,liste2)

print("***************************")

liste3=[1,2,3,4,5]
liste4=[eleman for eleman in liste3]
print(liste4)

print("***********************")
liste5=[3,4,5,6]
liste6=[z*2 for z in liste5]
print(liste6)


print("***********************")
a="BAYSAN"
denlist=[k*2 for k in a]
print(denlist)




print("*******************************")

denemelistesi=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
for v in denemelistesi:
    print("denemelistesi içindeki v değeri : ", v)

print("*********************")
denemelistesi=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
for v in denemelistesi:
    for m in v:
        print("v içindeki m değeri : ", m)


print("LISTCOMPREHENSION KAYNAK KODLARDA DAHA DETAYLI")

