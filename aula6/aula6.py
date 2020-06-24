#strings1
palavra="Calendario"

print(palavra[0]) #string é um array de caracteres
#podemos delimitar uma faixa "entre os chars"
print(palavra[0:3])
#imprime Cal

#usamos len para saber a length, usamos o typecast para str

print("tamanho: " + str(len(palavra)))

#strip remove espaços no começo e no fim
# upper deixa tudo em maiusculo e lower em minusculo
texto="flores"
print(texto.upper())
# minusculo
print(texto.lower())

#replace usamos pra substituir
texto2="banana"
print(texto2)
print(texto2.replace("a", "e"))
breno="kazara"
print(breno.replace("a", "o"))