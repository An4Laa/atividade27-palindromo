frase = str(input("Digite sua frase ou palavra: "))
frase = frase.upper().replace(" ", "")
invert = frase.upper() [::-1]
invert = invert.replace(" ", "")

if frase == invert :
    print("Sua frase ou palavra é um palíndromo.")

else :
    print("Sua frase ou palavra não é um palíndromo.")