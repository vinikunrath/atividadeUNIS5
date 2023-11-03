def inverter_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    nova_frase = ' '.join(palavras_invertidas)
    return nova_frase

# Exemplo de uso:
frase = "Olá, professor Alberane!"
print(inverter_palavras(frase))
