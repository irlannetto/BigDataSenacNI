
for i in range(10):
    nota1=float(input('digite a primeira nota:'))
    nota2=float(input('digite a segunda nota:'))

    media= (nota1+nota2)/2

    if media>7:
        print(f'a media do aluno é {media}, o aluno está aprovado')

    elif media>=5:
        print(f'a media do aluno é {media}, o aluno está em recuperação')

    else:
        print(f'a media do aluno é {media}, o aluno está reprovado')
    