#criando um dicionario
def exibir_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

#criamos um dicionario vazio para armazenar entradas

info_usuario = {}

print("Digite as informações (ou 'sair' na chave para encerrar): ")

while True:
    chave = input("Nome do campo (ex: profissão)")
    if chave.lower() == 'sair':
        break
    valor = input(f"Valor para a {chave}: ")
    info_usuario[chave] = valor

# Usamos ** para desempacotar o dicionario como argumentos

exibir_info(**info_usuario)
