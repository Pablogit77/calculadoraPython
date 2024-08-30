while True:
    print()  # Adiciona uma linha em branco
    print("Escolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Divisão Inteira")
    print("6 - Módulo")
    print("7 - Potenciação")
    print("0 - Sair")

    operacao = int(input("Informe o número da operação: "))

    while operacao < 0 or operacao > 7:
        oper = int(input("Operação inválida. Escolha uma operação entre 0 e 7: "))
        
    if operacao == 0:
        print("Saindo...")
        break   
     
    a = float(input("Informe o primeiro número: "))
    b = float(input("Informe o segundo número: "))
    
    match operacao:
        case 1:
            result = a + b
        case 2:
            result = a - b
        case 3:
            result = a * b
        case 4:
            while b == 0:
                b = float(input("Divisão por zero não é permitida. Informe o segundo número novamente: "))
            result = a / b
        case 5:
            result = a // b
        case 6:
            result = a % b
        case 7:
            result = a ** b
    
    print("O resultado é: " + str(result))
