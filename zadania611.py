# -*- coding: utf-8 -*-
"""Zadania611.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PTlpqwGLx1nOaR2KEgOzcrP_IISeErLS

ZADANIE 1
"""

def wiadomość (Name, Surname):
    return f'Cześć {Name} {Surname}!'

Name = input("Podaj imię: ")
Surname = input("Podaj nazwisko: ")
wynik = wiadomość(Name, Surname)
print(wynik)

"""ZADANIE 2"""

def mnozenie(a, b):
    return a * b

liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
wynik = mnozenie(liczba1, liczba2)
print("Wynik mnożenia 2 liczb to:", wynik)

"""ZADANIE 3

"""

def rezultat(liczba):
    return liczba % 2 == 0

liczba = int(input("Podaj liczbę całkowitą: "))
rezulatat1 = rezultat(liczba)

if rezultat:
    print("To jest liczba parzysta!")
else:
    print("To jest liczba nieparzysta!")

"""ZADANIE 4"""

def suma(a, b, c):
    return a + b >= c

liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
liczba2 = int(input("Podaj drugą liczbę całkowitą: "))
liczba3 = int(input("Podaj trzecią liczbę całkowitą: "))

wynik = suma(liczba1, liczba2, liczba3)
print("Wynik - Suma dwóch pierwszych liczb jest większa lub równa trzeciej:", wynik)

"""ZADANIE 5


"""

def wartość(input_list, value):
    return value in input_list

lista = [1, 2, 3, 4, 5]

sprawdz = int(input("Podaj wartość do sprawdzenia:"))
wynik = wartość(lista, sprawdz)
print("Czy ten wynik jest w liście? Oczywiscie, że:", wynik)

"""ZADANIE 6"""

def lista(lista1, lista2):
    polaczona_lista = lista1 + lista2
    polaczona_lista = list(set(polaczona_lista))
    polaczona_lista = [x**3 for x in polaczona_lista]
    return polaczona_lista

lista1 = [5, 10, 15, 20]
lista2 = [10, 15, 20, 25]

wynik = lista(lista1, lista2)
print("Wynik:", wynik)