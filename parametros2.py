# def criar_perfil(nome,idade,cidade):
#    print(f"{nome}, {idade} anos,{cidade}")
#criar_perfil(cidade="curitiba", nome="Julia",idade=25)

def somar_tudo(*numeros):
    return sum(numeros)
print(somar_tudo(1, 2))
print(somar_tudo(1, 2, 3, 4))
print(somar_tudo(10, 20, 30))