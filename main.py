import math


wejscie = input()
liczby = wejscie.split()

def obliczanie_newtona(n, k):
    licznik = math.factorial(n)
    mianownik = math.factorial(k)*math.factorial(n-k)
    return int(licznik/mianownik)

for i in range(len(liczby)):
    liczby[i] = int(liczby[i])
print(obliczanie_newtona(liczby[0],liczby[1]))