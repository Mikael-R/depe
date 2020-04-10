from os import system as terminal
from platform import system as sistema_operacional

########## DISTRIBUIÇÃO ELETRÔNICA EM SUBNÍVEIS ##########
'''
1s2
2s2  2p6
3s2  3p6  3d10
4s2  4p6  4d10  4f14
5s2  5p6  5d10  5f14
6s2  6p6  6d10
7s2  7p6
'''

if sistema_operacional() == 'Windows':
    terminal('cls')
else:
    terminal('clear')

s1 = s2 = p2 = s3 = p3 = s4 = d3 = p4 = s5 = d4 = p5 = s6 = f4 = d5 = p6 = s7 = f5 = d6 = p7 = 0

print('''
=========== OPÇÕES ===========
[1] Distribuição em níveis
[2] Distribuição em subníveis
==============================
      ''')

visualizar = input('-> Sua opção: ')
while visualizar != '1' and visualizar != '2':
    print('-> Opção inválida, digite novamente.')
    visualizar = input('\n-> Sua opção: ')

z = input('\n-> Número atômico: ')
while z.isnumeric() == False or int(z) > 118 or int(z) <= 0:
    print('-> Os números atômicos vão de 1 até 118, digite novamente.')
    z = input('\n-> Número atômico: ')
z = int(z)

########## 1S2 ##########
while True:
    if z == 0 or s1 == 2:
        break
    s1 += 1
    z -= 1
########## 2s2 ##########
while True:
    if z == 0 or s2 == 2:
        break
    s2 += 1
    z -= 1
########## 2p6 ##########
while True:
    if z == 0 or p2 == 6:
        break
    p2 += 1
    z -= 1
########## 3s2 ##########
while True:
    if z == 0 or s3 == 2:
        break
    s3 += 1
    z -= 1
########## 3p6 ##########
while True:
    if z == 0 or p3 == 6:
        break
    p3 += 1
    z -= 1
########## 4s2 ##########
while True:
    if z == 0 or s4 == 2:
        break
    s4 += 1
    z -= 1
########## 3d10 ##########
while True:
    if z == 0 or d3 == 10:
        break
    d3 += 1
    z -= 1
########## 4p6 ##########
while True:
    if z == 0 or p4 == 6:
        break
    p4 += 1
    z -= 1
########## 5s2 ##########
while True:
    if z == 0 or s5 == 2:
        break
    s5 += 1
    z -= 1
########## 4d10 ##########
while True:
    if z == 0 or d4 == 10:
        break
    d4 += 1
    z -= 1
########## 5p6 ##########
while True:
    if z == 0 or p5 == 6:
        break
    p5 += 1
    z -= 1
########## 6s2 ##########
while True:
    if z == 0 or s6 == 2:
        break
    s6 += 1
    z -= 1
########## 4f14 ##########
while True:
    if z == 0 or f4 == 14:
        break
    f4 += 1
    z-= 1
########## 5d10 ##########
while True:
    if z == 0 or d5 == 10:
        break
    d5 += 1
    z -= 1
########## 6p6 ##########
while True:
    if z == 0 or p6 == 6:
        break
    p6 += 1
    z -= 1
########## 7s2 ##########
while True:
    if z == 0 or s7 == 2:
        break
    s7 += 1
    z -= 1
########## 5f14 ##########
while True:
    if z == 0 or f5 == 14:
        break
    f5 += 1
    z -= 1
########## 6d10 ##########
while True:
    if z == 0 or d6 == 10:
        break
    d6 += 1
    z -= 1
########## 7p6 ##########
while True:
    if z == 0 or p7 == 6:
        break
    p7 += 1
    z -= 1

if visualizar == '1':
    k = s1
    l = s2 + p2
    m = s3 + p3 + d3
    n = s4 + p4 + d4 + f4
    o = s5 + p5 + d5 + f5
    p = s6 + p6 + d6
    q = s7 + p7
    print(f'''
=======================
        K = {k}
        L = {l}
        M = {m}
        N = {n}
        O = {o}
        P = {p}
        Q = {q}
=======================
          ''')
else:
    print(f'''
==============================
    1s{s1}
    2s{s2}  2p{p2}
    3s{s3}  3p{p3}  3d{d3}
    4s{s4}  4p{p4}  4d{d4}  4f{f4}
    5s{s5}  5p{p5}  5d{d5}  5f{f5}
    6s{s6}  6p{p6}  6d{d6}
    7s{s7}  7p{p7}
==============================
        ''')
