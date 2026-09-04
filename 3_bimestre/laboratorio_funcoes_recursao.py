def calcular_frete(valor_compra, peso_kg):
    frete = peso_kg * 5

    if valor_compra >= 200.00:
        frete = peso_kg * 2.5
    
    total1 = (valor_compra + frete)
    return total1




def aplicar_cupom(valor_item, cupom_desconto):
    cupom_desconto = 0.10
    aplicar_desconto = valor_item * cupom_desconto
    return aplicar_desconto

def exibir_cronograma_regressivo(parcelas_restantes, valor_Parcela):
    if parcelas_restantes == 0:
        return
    else:
        print(f"Parcela {parcelas_restantes}: R$ {valor_Parcela:}")

taxa_processamento = 2.0



valor_compra = float(input("Digite o valor da compra: "))
Peso_kg = float(input("Digite o peso do produto em kg: "))
cupom_desconto = float(input("Caso exista, digite o valor do cupom de desconto: "))
numero_parcelas = int(input("Caso exista, digite o número de parcelas: "))

total = calcular_frete((valor_compra, Peso_kg) + aplicar_cupom(valor_compra, cupom_desconto)) * taxa_processamento
print(f"Valor total da compra: R$ {total}")