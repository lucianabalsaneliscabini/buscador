from time import sleep

# CENTRALIZAÇÃO DO TÍTULO
def titulo(txt):
    """
        :parametro txt: Recebe o texto que devera ser estilizado e centralizado
        :return: Sem retorno
    """
    print('-' * 43)
    print(txt.center(41))
    print('-' * 43)

# ANIMAÇÃO 
def loading(txt):
    """
        :parametro txt: Recebe o texto que deverá receber uma "animação"
    """
    print(f'\n{txt}', end='', flush=True)
    sleep(0.4)
    print('.', end='', flush=True)
    sleep(0.3)
    print('.', end='', flush=True)
    sleep(0.3)
    print('.\033[m', flush=True)
    sleep(0.3)