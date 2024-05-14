print("="*20)
print("Conversor de medidas")
print("="*20)

def calculo(valor):
    if escolha_usuario == "1" or escolha_usuario == "centimetros":
        medida_retorno = valor / 100
        unidade = "m"
        unidade_escolhida = "metros"
    elif escolha_usuario == "2" or escolha_usuario == "metros":
        medida_retorno = valor * 100
        unidade = "cm"
        unidade_escolhida = "centimetros"
    elif escolha_usuario == "3" or escolha_usuario == "graus celsius":
        medida_retorno = (valor * 1.8) + 32
        unidade = "°F"
        unidade_escolhida = "graus fahrenheit"
    elif escolha_usuario == "4" or escolha_usuario == "graus fahrenheit":
        medida_retorno = (valor - 32) / 1.8
        unidade = "°C"
        unidade_escolhida = "graus celsius"
    elif escolha_usuario == "5" or escolha_usuario == "quilos":
        medida_retorno = valor * 1000
        unidade = "g"
        unidade_escolhida = "gramas"
    else:
        medida_retorno = valor / 1000
        unidade = "K"
        unidade_escolhida = "quilos"
    return f"Essa medida em {unidade_escolhida} é de {medida_retorno}{unidade}."

while True:
    while True:
        escolha_usuario = input("Escolha a unidade de medida que você quer utilizar:\n"
                                "1. centimetros -> metros\n"
                                "2. metros -> centimetros\n"
                                "3. graus celsius -> graus fahrenheit\n"
                                "4. graus fahrenheit -> graus celsius\n"
                                "5. quilos -> gramas\n"
                                "6. gramas -> quilos\n-> ")
        if escolha_usuario in ["1", "2", "3", "4", "5", "6"] or escolha_usuario in ["centimetros", "metros", "graus celsius", "graus fahrenheit", "quilos", "gramas"]:
            break
        print("Escolha inválida! Tente novamente\n")
    while True:
        medida_usuario = input("Qual a medida gostaria de converter?\n->")
        if medida_usuario.isnumeric():
            medida_usuario = float(medida_usuario)
            break
        else:
            print("Escolha inválida! Tente um número válido\n")
    print(calculo(medida_usuario))
    print("")
    while True:
        lista_confirmacao = ["Sim", "sim", "S", "ss", "s", "SS", "SIM"]
        lista_negacao = ["Não", "Nao", "não", "nao", "n", "NN", "nn", "NÃO", "NAO"]
        variavel_continuar = input("Você deseja realizar outra conversão?\n->")
        if variavel_continuar in lista_confirmacao or variavel_continuar in lista_negacao:
            break
        else:
            print("Valor inválido, Tente novamente!")

    if variavel_continuar in lista_confirmacao:
        print("Reiniciando...\n")
    else:
        break
print("Obrigado por utilizar nosso sistema!")