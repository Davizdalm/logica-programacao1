nome = input("Insira seu nome: ")   #-------- EXERCÍCIO 1 -------#
email = input("Insira seu E-mail: ")

nome_limpo = nome.strip().upper()
email_limpo = email.strip().lower()

print(f"Nome higienizado: {nome_limpo}")
print(f"E-mail higienizado: {email_limpo}")

#------------EXERCICIO 2------------#

cpf = input("Digite seu cpf: ")
telefone = input("Digite seu telefone: ")

cpf_limpo = cpf.strip().replace(".", "").replace("-", "")
telefone_limpo = (telefone.strip().replace("(", "").replace(")", "").replace("-", ""))

print(f"CPF higienizado: {cpf_limpo}")
print(f"Telefone higienizado: {telefone_limpo}")


#------------ EXERCÍCIO 3 ------------#

codigo = input("Digite o código: ")

codigo_limpo = codigo.strip().upper().replace("-", "_")

print(f"Código higienizado = {codigo_limpo}")
