from random import randint
sorteio = (randint(1,10),randint(1,10),randint(1,10),
    randint(1,10),randint(1,10))
print('Os valores sorteados foram:', end=' ')
for n in sorteio:
    print(f'{n} ', end=' ')
print(f'\nO maior valor sorteado foi {max(sorteio)}.')
print(f'O menor valor sorteado foi {min(sorteio)}.')
