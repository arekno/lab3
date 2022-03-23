import sys
import math
import random

# #zad1
# a=[1-x for x in range(1,11,1)]
# b=[4**y for y in range(8)]
# c=[x for x in b if x%2==0]
# print(a)
# print(b)
# print(c)

#zad2
#
# lista1=[]
# for x in range(1,11,1):
#     x=random.randint(1,100000)
#     lista1.append(x)
# print(lista1)
# lista2=[x for x in lista1 if x%2==0]
# print(lista2)


#zad3


# produkty={"mleko":"litry","maslo":"gramy","pomidory":"sztuki","jablka":"sztuki"}
# print(produkty)
# sztuki=[]


#zad4

# def troj_prostokat(a,b,c):
#     if a**2+b**2==c**2:
#         print('to jest trojkat prostokatny')
#     else:
#         print('To nie jest trojkat prostokatny')
#
# print(troj_prostokat(3,4,5))
# print(troj_prostokat(3,8,2))


#zad5

# def pole_trapezu(a=2,b=5,h=8):
#     return pole=1/2*(a+b)*h
#
#
# print(pole_trapezu(2,5,8))


#zad6

# def iloczyn_ciagu(a=1,b=4,c=10):
#     y=[a*b for a in range(a,c)]
#     iloczyn=1
#     for n in y:
#         iloczyn *=n
#     return iloczyn
#
# print(iloczyn_ciagu())


#zad7

# def iloczyn_ciagu(* liczby):
#     if len(liczby)==0:
#         return 0
#     else:
#         iloczyn=1
#     for n in liczby:
#         iloczyn *=n
#     return iloczyn
# print(iloczyn_ciagu(1,4,8,12,16,20,24,28,32,36))

#zad10
a=[]
for x in range(101):
    if x%4==0:
        a.append(x)
print(a)
plik=open("dane.txt","w+")
plik.writelines(str(a))
plik.close()

#zad11
plik=open("dane.txt","r")
ciag=plik.readline()
print(ciag)
plik.close()
