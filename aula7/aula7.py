#strings parte2
frase="hoje esta frio"

res="hoje" not in frase #é false
print(res)

res2="frio" in frase #é true
print(res2)

#placeholder
cidade="Belo Horizone"
dia=15
mes="Dezembro"
ano=2019
data="{}, {} de {} de {}"

print(data.format(cidade,dia,mes,ano))