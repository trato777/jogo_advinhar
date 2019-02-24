from random import randint

while True:
    sor = randint(0, 100)
    print(sor)
    num = int(input('Tente acertar o numero entre 0 e 100: '))
    while True:
        if sor == num:
            print(f'Parabéns o numero era {sor}!!!')
            break
        else:
            if num > sor:
                print('O numero é menor!')
            elif num < sor:
                print('O numero é maior!!!')
        num = int(input('Digite novamente o numero: '))
    res = str(input('Voce deseja continuar? '))
    while res not in 'SsNn':
        if res in 'Ss':
            continue
        if res not in 'SsNn':
            res = str(input('Resposta inválida! [S/N]'))
    if res in 'Nn':
        break

