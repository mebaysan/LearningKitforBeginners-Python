print("for döngü denemeleri")

liste=[1,2,3,4,5,6]

for denelem in liste:
    print(denelem)
    
print("**********************")

liste1=[2,123,132,432,123,543,753,123,76,986,10980,123,6,7,8,88,12,43,54]
toplam = 0
print(liste1,"\nBu liste için:")
for eleman in liste1:
    toplam = toplam + eleman
    print("Toplam: {} Eleman: {}".format(toplam,eleman))


print("****************************")
liste2=[123,231,531,123,513,647,8975,123321,4452,124123,2,4,12,24,34,45,56,67,78]
for cift in liste2:
    if(cift%2==0):
        print(cift)


print("*************************************")


x="Sanane Lan Mal"
for harf in x:
    print(harf)

print("*********************************")

x="Sanane Lan Mal"
for harf in x:
    print(harf*3)


print("*****************************")

