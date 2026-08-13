telefone = input("Digite o telefone no formato (xx)xxxx-xxxx:" )

ddd = telefone[1:3]
numero = telefone[4:]

print(f"ddd: {ddd}")
print(f"numero: {numero}")




data = input("Digite sua data de nascimento (DD/MM/AAAA): ")

dia = data[0:2]
mes = data[3:5]
ano = data[6:]

print(f"Dia: {dia}")
print(f"Mês: {mes}")
print(f"Ano: {ano}")

email = input("Digite seu e-mail (nome.sobrenome@escola.com): ")

primeiro_nome = email[0:5] 
dominio = email[13:]

print(f"Primeiro nome extraído: {primeiro_nome}")
print(f"Domínio extraído: {dominio}")
