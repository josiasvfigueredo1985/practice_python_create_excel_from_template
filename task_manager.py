import PySimpleGUI as sg


def criar_janela_inicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''), sg.Input('', key='txt')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar'), sg.Button('Salvar')]
    ]

    return sg.Window('Todo List', layout=layout, finalize=True)


# Criar a janela
janela = criar_janela_inicial()

# Criar as regras dessa janela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[
                             sg.Checkbox(''), sg.Input('')]])
    elif event == 'Salvar':
        print('')
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()
