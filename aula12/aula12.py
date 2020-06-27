#loops
carros=["HRV", "Golf", "Argo", "Focus"]

for x in carros: # inicializa sem parentes e ja criamos uma variavel dentro do for
    print(x)
    if(x=="Golf"):
        print("VW")
    #podemos ja usar 
# for x ( ja cria a variavel)
# for x in (ja mostra qual array percorrer)

#python automaticamente pode criar a lista caso nenhuma seja mencionada

for x in ["1", "2", "3", "4"]:
    print(x)