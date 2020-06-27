#Nome do programa
print("Calculadora de calorias de um bolo 2020 #Synaxis")
#define ovoInteiro = 0 porque pode dar erro na soma temporaria
print("Vamos tentar calcular quantas calorias existem seu bolo")

manteiga = input("Digite quantos gramas de manteiga está escrito na receita\n")
manteiga = manteiga * 7,17	
#print(Manteiga)
farinha = input("Digite quantos gramas de farinha vai na receita\n")
farinha = farinha * 3,60
#perguntar se gema e clara são separadas
#ovosSeparados = input("Na receita os ovos são separados? digite s ou n")
#if ovosSeparados == "s":
        #perguntar quantas gemas
gemas = input("Quantas gemas vão na receita?")
gemas = gemas * 53,7
        #perguntar quantas claras e multiplicar por kcal
claras = input("Quantas Claras vão na receita ou são usadas para clara em neve")
claras = claras * 53,7
#else:
        #ovoInteiro = input("Quantos ovos inteiros vao na receita?")
        #ovoInteiro = ovoInteiro * 64,35
temporario =  gemas+manteiga+farinha+claras

print("o total temporario de calorias eh: " + temporario)