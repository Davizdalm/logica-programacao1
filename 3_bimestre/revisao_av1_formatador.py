def formatar_citacao(nome_completo):
    partes = nome_completo.strip().split()

    sobrenome = partes[-1].upper()

    primeiro_nome = " ".join(partes[:-1])

    return sobrenome + ", " + primeiro_nome

resultado1 = formatar_citacao("Carlos Eduardo Andrade")
print(resultado1)

#--------------------------------------------------------#

def gerar_codigo(ano, cpf):
    cpf_limpo = cpf.strip()
    tres_digitos = cpf_limpo[0:3]
    return "ALU-" + str(ano) + "-" +tres_digitos

    




resultado2 = gerar_codigo("2026", "154.607.999-86")
print(resultado2) 