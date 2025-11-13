
resultado=[]

print('='*40)
print('/n sistema de boletim de aluno')
print('='*40)

for i in range(5):
    nome=input('nome do aluno:')
    nota1=float(input('primeira nota:'))
    nota2=float(input('segunda nota:'))
media=(nota1+nota2)/2

if media>7:
    status=()