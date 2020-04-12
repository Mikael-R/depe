from lib import *

print('''
 _________________________________
|_____________ MENU ______________|
| [ 1 ] Distribuição em níveis    |
| [ 2 ] Distribuição em subníveis |
| [ 3 ] Distribuição em ambas     |
| [ 4 ] Pesquisar elemento        |
|_________________________________|
      ''')

menu = input('❱ Sua opção: ')
while menu != '1' and menu != '2' and menu != '3' and menu != '4':
    print('❱ Opção inválida, digite novamente.')
    menu = input('❱ Sua opção: ')

elemento = pesquisar(input('\n❱ Digite o número atômico, a sigla ou o nome do elemento químico.\n❱ ').strip().title())
while elemento == None:
    print('❱ Este elemento químico não consta na tabela periódica, digite novamente.')
    elemento = pesquisar(input('\n❱ Digite o número atômico, a sigla ou o nome do elemento químico.\n❱ ').strip().title())

diagrama_dicionario = distribuir(elemento[0])

if menu == '1':
    print(f'''
=======================
        K = {diagrama_dicionario["1s"]}
        L = {diagrama_dicionario["2s"] + diagrama_dicionario["2p"]}
        M = {diagrama_dicionario["3s"] + diagrama_dicionario["3p"] + diagrama_dicionario["3d"]}
        N = {diagrama_dicionario["4s"] + diagrama_dicionario["4p"] + diagrama_dicionario["4d"] + diagrama_dicionario["4f"]}
        O = {diagrama_dicionario["5s"] + diagrama_dicionario["5p"] + diagrama_dicionario["5d"] + diagrama_dicionario["5f"]}
        P = {diagrama_dicionario["6s"] + diagrama_dicionario["6p"] + diagrama_dicionario["6d"]}
        Q = {diagrama_dicionario["7s"] + diagrama_dicionario["7p"]}
=======================
          ''')
if menu == '2':
    print(f'''
==============================
    1s{diagrama_dicionario["1s"]}
    2s{diagrama_dicionario["2s"]}  2p{diagrama_dicionario["2p"]}
    3s{diagrama_dicionario["3s"]}  3p{diagrama_dicionario["3p"]}  3d{diagrama_dicionario["3d"]}
    4s{diagrama_dicionario["4s"]}  4p{diagrama_dicionario["4p"]}  4d{diagrama_dicionario["4d"]}  4f{diagrama_dicionario["4f"]}
    5s{diagrama_dicionario["5s"]}  5p{diagrama_dicionario["5p"]}  5d{diagrama_dicionario["5d"]}  5f{diagrama_dicionario["5f"]}
    6s{diagrama_dicionario["6s"]}  6p{diagrama_dicionario["6p"]}  6d{diagrama_dicionario["6d"]}
    7s{diagrama_dicionario["7s"]}  7p{diagrama_dicionario["7p"]}
==============================
        ''')
if menu == '3':
  print(f'''
============================
== Distribuição em níveis ==
        K = {diagrama_dicionario["1s"]}
        L = {diagrama_dicionario["2s"] + diagrama_dicionario["2p"]}
        M = {diagrama_dicionario["3s"] + diagrama_dicionario["3p"] + diagrama_dicionario["3d"]}
        N = {diagrama_dicionario["4s"] + diagrama_dicionario["4p"] + diagrama_dicionario["4d"] + diagrama_dicionario["4f"]}
        O = {diagrama_dicionario["5s"] + diagrama_dicionario["5p"] + diagrama_dicionario["5d"] + diagrama_dicionario["5f"]}
        P = {diagrama_dicionario["6s"] + diagrama_dicionario["6p"] + diagrama_dicionario["6d"]}
        Q = {diagrama_dicionario["7s"] + diagrama_dicionario["7p"]}
=============================
= Distribuição em subníveis =
    1s{diagrama_dicionario["1s"]}
    2s{diagrama_dicionario["2s"]}  2p{diagrama_dicionario["2p"]}
    3s{diagrama_dicionario["3s"]}  3p{diagrama_dicionario["3p"]}  3d{diagrama_dicionario["3d"]}
    4s{diagrama_dicionario["4s"]}  4p{diagrama_dicionario["4p"]}  4d{diagrama_dicionario["4d"]}  4f{diagrama_dicionario["4f"]}
    5s{diagrama_dicionario["5s"]}  5p{diagrama_dicionario["5p"]}  5d{diagrama_dicionario["5d"]}  5f{diagrama_dicionario["5f"]}
    6s{diagrama_dicionario["6s"]}  6p{diagrama_dicionario["6p"]}  6d{diagrama_dicionario["6d"]}
    7s{diagrama_dicionario["7s"]}  7p{diagrama_dicionario["7p"]}
=============================
          ''')
if menu == '4':
    print('\n=======================')
    print(f'• Número atômico: {elemento[0]}\n• Elemento: {elemento[1]}\n• Sigla: {elemento[2]}')
    print('=======================')
