print("Bem vindo, você já pode acessar a calculadora!")
print("Qual operação você deseja realizar?")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação") 
print("4 - Divisão")
opcao = int(input("Digite o número da operação desejada: "))
if opcao == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print(f"O resultado da adição é {resultado}.")
elif opcao == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print(f"O resultado da subtração é {resultado}.")
elif opcao == 3:
    num1 = float(input("Digite o primero número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print(f"O resultado da multiplicação é {resultado}.")
elif opcao == 4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print(f"O resultado da divisão é {resultado}.")
else:print("Opção inválida.")