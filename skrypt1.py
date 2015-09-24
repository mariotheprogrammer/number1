#!/usr/bin/python3

def sprawdz_int(x):
	wynik=x.isdigit()
	print('Pozdro z funkcji')
	return wynik

print('hello world')
zmienna = input('podaj liczbe')
print('Liczba:'+zmienna)
print(sprawdz_int(zmienna))
