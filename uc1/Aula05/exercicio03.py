 
usuario_c='adm'
senha_c='123456'

tentativas=3

while tentativas>0:
    usuario=input('digite seu usuario:')
    senha=input('digite sua senha:')
    if  usuario==usuario_c and senha==senha_c:
        print('acesso permitido')
        break
    else:
        tentativas-=1
        print(f'senha errada, resta {tentativas} tentativas')