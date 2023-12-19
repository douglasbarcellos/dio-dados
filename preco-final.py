valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

# Cálculo do preço total do pedido
precoHamburgueres = valorHamburguer * quantidadeHamburguer
precoBebidas = valorBebida * quantidadeBebida
precoTotal = precoHamburgueres + precoBebidas

# Cálculo do troco
troco = valorPago - precoTotal

# Imprimir a saída formatada
mensagem = f"O preço final do pedido é R$ {precoTotal:.2f}. Seu troco é R$ {troco:.2f}."
print(mensagem)
