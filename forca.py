palavra = "python"
letras_usuario = []
chances = 4
ganhou = False

while True:
    # Imprime a palavra com os acertos e traços
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print() # Linha adicionada para quebrar a linha aqui!

    print(f"Você tem {chances} chances")
    tentativa = input("Escolha uma letra para adivinhar: ").lower()

    # Validação simples para garantir que o usuário digitou apenas uma letra
    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Por favor, digite apenas uma única letra!")
        continue

    letras_usuario.append(tentativa)

    if tentativa not in palavra.lower():
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break
