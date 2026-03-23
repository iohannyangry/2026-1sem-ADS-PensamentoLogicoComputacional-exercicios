#exercicio3
>>> numero = int(input("Digite um número para ver a tabuada: "))
Digite um número para ver a tabuada: 22
>>> print(f"\nTabuada do {numero}:")

Tabuada do 22:
>>> for i in range(1, 11):
...         resultado = numero * i
...         print(f"{numero} x {i} = {resultado}")
...
22 x 1 = 22
22 x 2 = 44
22 x 3 = 66
22 x 4 = 88
22 x 5 = 110
22 x 6 = 132
22 x 7 = 154
22 x 8 = 176
22 x 9 = 198
22 x 10 = 220
