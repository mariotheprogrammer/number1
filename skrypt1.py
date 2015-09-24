#!/usr/bin/python3

def sprawdz_int(x):
	wynik=x.isdigit()
	print('Pozdro z funkcji')
	return wynik

print('hello world')
#zmienna = input('podaj liczbe')
zmienna = '2'
print('Liczba:'+zmienna)
print(sprawdz_int(zmienna))
