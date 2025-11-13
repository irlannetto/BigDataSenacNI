
def calculo_multa(peso_t):
    limite=100
    multa=4

    if peso_t>limite:
        excesso=peso_t-limite
        return excesso*multa
        
    else:
        return 0


for i in range(2):
calculo_multa=int(input('qual o kg de peixe?'))



