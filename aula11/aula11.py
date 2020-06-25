#if e elif e else

dia=1+1

if dia==1:
    print("hoje é dia 1")

elif dia!=1: # else if vira elif em python
    print("hoje não é dia 1")

else:
    print("tudo falso fodase")


option = input("Como está o clima hoje?,digite 1 para sol e 2 para chuva")
lugar=""
if option == 1:
    lugar="parque"
elif option == 2:
    lugar="cinema"
print("hoje vamos ao: ",str(lugar))


