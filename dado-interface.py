import PySimpleGUI as sg, random

sg.theme('Reddit')

layout = [
    [sg.Text('Qual o tamanho do dado que você deseja? (0-1000)', key='tamanho')],
    [sg.InputText('', key='respostaTamanho')],
    [sg.Text('Você deseja girar o dado?', key='girar')],
    [sg.Button('Sim', key='sim'), sg.Button('Não', key='nao')],
    [sg.Text('', key='resposta', text_color='red', font=16)],
    [sg.Button('Sair do Programa', key='sair')]
]

janela = sg.Window('Simulador de Dado', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == 'sair' or evento == 'nao':
        break
    if evento == 'sim':
        tamDado = int(valores['respostaTamanho'])
        if tamDado == 0:
            janela['resposta'].update('Por favor, digite um número diferente de 0.'.format())
        elif tamDado > 1000:
            janela['resposta'].update('Por favor, digite um número menor que 1000.'.format())
        elif tamDado == '':
            janela['resposta'].update('Por favor, digite um valor.'.format())
        else:
            randomizar = random.randint(1, tamDado)
            janela['resposta'].update('D{}'.format(randomizar))
    