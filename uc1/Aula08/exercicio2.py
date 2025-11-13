
def calculo_imc(peso,altura):
    return peso/ (altura*altura)

def classificacao_p(imc):
    if imc<18.5:
        return'abaixo do peso'
    elif imc<25:
        return'peso normal'
    elif imc<30:
        return'sobrepeso'
    else:
        return'obesidade'
    
print('*'*50)
print('calculadora de imc'.center(50))
print('*'*50)

n=int(input('deseja calcular de quantas pessoas?'))

for i in range(n):
    peso=float(input('qual peso?'))
    altura=float(input('qual a altura?'))

    imc= calculo_imc(peso,altura)
    classificacao= classificacao_p(imc)

    print(f'IMC= {imc:.2f} | classificação: {classificacao}')    