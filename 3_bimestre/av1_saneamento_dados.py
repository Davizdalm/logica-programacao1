# ==============================================================================
# PROVA PRÁTICA AV1 - 3º BIMESTRE
# ARQUIVO: av1_saneamento_dados.py
# Nome do Aluno: Davi Almeida
# Data: 28/08/26
# ==============================================================================

# Lista de cadastros brutos recebidos do sistema
cadastros_brutos = [
   "  joao da silva;11988887777  ",
   "  maria sousa;21977776666  ",
   "  carlos edgardo oliveira;31966665555  ",
   "  ana paula lima;41955554444  "
]

print("==================================================")
print("     SISTEMA DE SANEAMENTO DE DADOS - AV1         ")
print("==================================================\n")

# TODO: Escreva o laco de repeticao usando for e range() para percorrer a lista
for i in range(len(cadastros_brutos)):
        # 1. Remova os espacos extras do inicio e fim do cadastro atual
    cadastro = cadastros_brutos[i].strip()

    # 2. Separe o nome e o telefone (Dica: use o metodo .split(";"))
    partes = cadastro.split(";")
    nome = partes[0].strip().upper()    
    telefone = partes[1].strip()

    # 3. Converta o nome para letras MAIUSCULAS
    nome_padrao = nome

    # 4. Extraia o DDD (2 primeiros digitos do telefone) usando fatiamento [0:2]
    ddd = telefone[0:2]

    # 5. Exiba o resultado padronizado no terminal
    # Exemplo de print formatado desejado:
    print(f"Funcionário: {nome_padrao} | DDD: {ddd} | Telefone: {telefone}")
    # Funcionario: NOME MAIUSCULO | DDD: 11 | Telefone: 11988887777

print("\n==================================================")
print("             PROCESSAMENTO CONCLUÍDO              ")
print("==================================================")

 

 

# Saída Esperada no Terminal
 

# ==================================================
#     SISTEMA DE SANEAMENTO DE DADOS - AV1         
# ==================================================

# Funcionário: JOAO DA SILVA | DDD: 11 | Telefone: 11988887777
# Funcionário: MARIA SOUSA | DDD: 21 | Telefone: 21977776666
# Funcionário: CARLOS EDGARDO OLIVEIRA | DDD: 31 | Telefone: 31966665555
# Funcionário: ANA PAULA LIMA | DDD: 41 | Telefone: 41955554444

# ==================================================
#            PROCESSAMENTO CONCLUÍDO              
# ==================================================