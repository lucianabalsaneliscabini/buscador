import urllib.request
import webbrowser
from utilities import titulo, loading

titulo('BUSCADOR.br')


while True:
    site = str(input('\nQual site você deseja acessar? '))
    if site == '':
        continue
    else:
        loading('\033[33mBUSCANDO \033[m')
        break



http = ''

if not 'http://' in site and not 'https://' in site:
    http = 'http://'
 
    if not 'www' in site:
        http += 'www.' + site
    else:
        http += site

    if not 'com' in http:
        http += '.com'

    if not 'br' in http:
        http += '.br'
else:
    http = site


try:
    urllib.request.urlopen(http)
except urllib.error.URLError:
    print('\n\033[31mTENTE NOVAMENTE MAIS TARDE :(\033[m')
    print(f'\nERRO: O site {http} não está disponível no momento.\n')
    print('Tente: ')
    print('. Verificar o URL digitado')
    print('. Verificar a conexão com a internet\n')
else:
    print('\n\033[32mO SITE ESTÁ DISPONÍVEL :)\033[m\n')
    print('[ 1 ] ABRIR')
    print('[ 2 ] SAIR DO PROGRAMA\n')
    
    while True:
        resposta = int(input('OPÇÃO: '))
        if resposta == 1:
            webbrowser.open(http)
            break          
        else:
            loading('\033[31mENCERRANDO O PROGRAMA \033[m')
            break
        