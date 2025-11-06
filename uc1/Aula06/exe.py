

lista02_nopets=[ 
    'lavar louça', 
    'ir ao mercado',
    'lavar banheiro',
    'tirar poeira',
    'lavar quintal']

lista02_pets=lista02_nopets.copy()

lista02_pets.append('dar banho no doguinho')
lista02_pets.append('limpar areia dos gatos')
lista02.pop()
print(lista02)
print(lista02[1][6:13])
print(lista02[1][6:])
print(lista02[1][:6])