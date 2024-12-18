from product_componet import *

def main():
    # Criando produtos
    produto1 = ProductLeaf("Produto 1", 100)
    produto2 = ProductLeaf("Produto 2", 200)
    produto3 = ProductLeaf("Produto 3", 300)
    produto4 = ProductLeaf("Produto 4", 400)
    produto5 = ProductLeaf("Produto 5", 500)

    # Criando caixas
    caixa1 = ProductComposed("Caixa 1", 0)
    caixa2 = ProductComposed("Caixa 2", 0)
    caixa3 = ProductComposed("Caixa 3", 0)

    # Adicionando produtos nas caixas
    caixa1.add(produto1)
    caixa1.add(produto2)

    caixa2.add(produto3)
    caixa2.add(produto4)

    caixa3.add(produto5)

    # Adicionando caixas na caixa 1
    caixa1.add(caixa3)

    # Calculando o preço total da caixa 1
    #print(f"Preço total da caixa 1: {caixa1.get_price()}")

main()