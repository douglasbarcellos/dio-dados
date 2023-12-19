def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
 
    cupom_desconto = input()
 
    # Aplicar desconto de acordo com o cupom
    if cupom_desconto == "10%":
        total *= 0.9  # Reduz o total em 10%
    elif cupom_desconto == "20%":
        total *= 0.8  # Reduz o total em 20%
 
    # Imprimir o valor total com desconto
    print(f"Valor total: {total:.2f}")
 
if __name__ == "__main__":
    main()
