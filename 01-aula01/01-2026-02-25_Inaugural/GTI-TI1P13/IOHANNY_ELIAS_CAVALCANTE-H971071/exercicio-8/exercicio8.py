#exercicio8
 preco_unitario = 100.00
>>>
>>> quantidade = int(input("Quantas unidades você deseja comprar? "))
Quantas unidades você deseja comprar? 57
>>> valor_total = preco_unitario * quantidade
>>> if quantidade >= 10:
...       desconto = valor_total * 0.10
...       valor_final = valor_total - desconto
...       print(f"Você ganhou 10% de desconto! Valor economizado: R$ {desconto:.2f}")
... else:
...       valor_final = valor_total
...       print("Quantidade insuficiente para desconto.")
...
...
Você ganhou 10% de desconto! Valor economizado: R$ 570.00
>>> print(f"O valor final da sua compra é: R$ {valor_final:.2f}")
O valor final da sua compra é: R$ 5130.00
