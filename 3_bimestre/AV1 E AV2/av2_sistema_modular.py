# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: Davi Almeida
# Data: 17-09-26
# Link do Repositório: https://github.com/Davizdalm/logica-programacao1.git
# ==============================================================================

# Lista inicial de dados brutos (Exemplo: Sistema de RH / Atendimento)
# Os dados estão no formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
   "  davi almeida silva;tecnico;11991231234  ",
   "  Alexandre de moraes;juiz;99955554444  ",
   "  RoNaldinho Menézes;Banqueiro;35912341234  "
]


# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA (Mínimo de 3 funções)
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
   """
   FUNÇÃO 1:
   - Deve receber uma string.
   - Deve remover espaços extras das pontas (.strip()).
   - Deve converter o texto para letras MAIÚSCULAS (.upper()).
   return
   """
   texto_limpo = texto.strip().upper()
   return texto_limpo


def extrair_codigo_ou_ddd(telefone):
   """
   FUNÇÃO 2:
   - Deve receber um dado em formato de string (ex: telefone ou CPF).
   - Deve remover espaços das pontas.
   - Deve utilizar FATIAMENTO DE STRING [x:y] para extrair os 2 primeiros dígitos (ex: DDD).
   - Retorna apenas os dígitos extraídos.
   """
   telefone_limpo = telefone.strip()
   ddd = telefone_limpo[:2]
   return ddd


def processar_e_exibir_cadastros(lista_dados):
   """
   FUNÇÃO 3:
   - Deve receber a lista de cadastros brutos como parâmetro.
   - Deve utilizar um laço FOR para percorrer cada item da lista.
   - Em cada iteração do for:
       1. Separar as partes usando .split(";")
       2. Chamar a Função 1 para formatar o Nome e o Cargo.
       3. Chamar a Função 2 para extrair o DDD/Código do telefone.
       4. Exibir o resultado final formatado na tela com f-string.
   - Retorna a quantidade total de registros processados.
   """
   total_processado = 0

   for dado in lista_dados:
       nome, cargo, telefone = dado.split(";")
       nome_formatado = limpar_e_formatar_texto(nome)
       cargo_formatado = limpar_e_formatar_texto(cargo)
       ddd = extrair_codigo_ou_ddd(telefone)

       print(f"NOME: {nome_formatado} | CARGO: {cargo_formatado} | DDD: {ddd}")
       total_processado += 1

   return total_processado


# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL (FLUXO DE EXECUÇÃO)
# ------------------------------------------------------------------------------

def main():
   print("==================================================")
   print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
   print("==================================================\n")

   print("Iniciando o processamento dos dados...\n")

   total_processado = processar_e_exibir_cadastros(dados_brutos)
   print(f"\nTotal de registros processados: {total_processado}")

   print("\n==================================================")
   print("             PROCESSAMENTO CONCLUÍDO              ")
   print("==================================================")


# Execução do programa
if __name__ == "__main__":
   main()