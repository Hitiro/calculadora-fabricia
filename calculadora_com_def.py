import math

def raiz_quadrada(num):
    return math.sqrt(num)

def potencia(num,num2):
     return math.pow(num,num2)

def soma(num, num2):
     return num+num2

def subtracao(num, num2):
     return num-num2

def multiplicacao(num, num2):
     return num*num2

def divisao(num, num2):
     return num/num2

#Método pra simular valor de um emprestimo By Hitiro Tsugawa
def calcula_taxa_real (taxa):
    return taxa/100

def calacular_valor(valor, taxa_real, intervalo):
    return valor * (1+(taxa_real)) ** intervalo

def calcula_valor_mensal(juros_composto, intervalo):
    try:
        return juros_composto/intervalo
    except:
        print('Não é possível dividir por zero \'0\'')

def simulacao_emprestimo():
    valor = float(input('Digite o Valor: '))
    taxa = float(input('Digite a taxa : '))
    intervalo = int(input('Digite o intervalo em meses: '))

    if valor <= 0: return print('Não é possivel realiar um emprestimo com valor negativo.')

    taxa_real = calcula_taxa_real(taxa)
    juros_composto = calacular_valor(valor, taxa_real, intervalo)
    valor_mensal = calcula_valor_mensal(juros_composto, intervalo)

    try:
        print("Você vai pagar o total de: R$", round(juros_composto, 2))
        print("Você vai pagar por mes: R$", round(valor_mensal, 2))
    except:
        print('Algo deu errado por aqui!')
        

    print('-' * 50)
    print('Que tal um novo emprestimo, amigo?')
    return


while True:
    calcular = input("Olá, bem vindo a nossa calculadora! \n\nInforme a ação desejada:\n\n" \
    "   'C' = continuar e \n" \
    "   'S' = sair: ")  
    
    if calcular.upper() == 'S':
        break
    elif calcular.upper()!= 'S' and calcular.upper() != 'C':
        print("Opção inválida.")
        break
    else:
        try:
            n1 = float(input("Digite N1: "))
            operacao = input("Escolha operação: +, -, *, /, r (raiz quadrada), p (potência)")
            
            if operacao.upper() == 'R':
                resultado = raiz_quadrada(n1)
                print (f"√{n1} = {resultado}.")

            elif operacao.upper() == 'P':
                n2 = int(input("digite expoente: "))
                resultado = potencia(n1,n2)
                print (f"{n1} ^ {n2} = {resultado}")

            else:
                try:
                    n2 = float(input("digite N2: "))
                    if operacao == '+':
                        resultado = soma(n1, n2)
                        print(f"{n1} + {n2} = {resultado}")

                    elif operacao =='-':
                        resultado = subtracao(n1, n2)
                        print(f"{n1} - {n2} = {resultado}")

                    elif operacao == '*':
                        resultado = multiplicacao(n1, n2)
                        print(f"{n1} * {n2} = {resultado}")

                    elif operacao == '/':
                        resultado = divisao(n1, n2)
                        print(f"{n1} / {n2} = {round(resultado,2)}")

                    else:
                        print("Operação inválida!")
                        
                except Exception:
                    print("Erro try operação")
                    break
        except Exception:
                print("Erro Try números!")
                break

    print("\n")