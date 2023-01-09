import random

duzo = 100000000
Lista = []
inf=0
powtorzeniaprocesu = 1

for i in range(powtorzeniaprocesu):
    kolo=0
    inf=inf+1
    for i in range(duzo):
        x=random.random()
        y=random.random()
        zaawansowanamatematykapoziomklasa8 = (x**2 + y**2)**(1/2)
        if zaawansowanamatematykapoziomklasa8<=1:
            kolo=kolo+1
    pi= (kolo/duzo) * 4
    Lista.append(pi)
    print(inf)

wynik = sum(Lista)/len(Lista)
print(wynik)