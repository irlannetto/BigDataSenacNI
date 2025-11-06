
#dicionario#

filme={
    'nome':'v for vendetta',
    'ano' : 2005,
    'genero': 'açao' , #triller/drama
    'faixa etaria': 16
}

print(filme)
print(type(filme))
print()
print(filme['ano'])
print()
print(filme.keys())
print()
print(filme.values())
print()
print(len(filme))
print()
filme['duraçao']='130min'
filme['genero']="triller/drama"
print(filme)