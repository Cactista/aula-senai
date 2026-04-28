def formatar_real_replace(valor):
    texto = f"R$ {valor:,.2f}" # padrao do eua R$ 1,234.56
    texto = texto.replace(",","X")
    texto = texto.replace(".",",")
    texto = texto.replace("X",".")
    return texto

#uso
preco = 1234.5
print(formatar_real_replace(preco))  # R$ 1.234,50
