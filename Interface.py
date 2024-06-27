import PySimpleGUI as sg

# All the stuff inside your window.
layout = [
            [sg.Text("Data"), sg.InputText(key='data')],
            [sg.Text("Nome"), sg.InputText(key='nome')],
            [sg.Text("Vendedor"), sg.InputText(key='vendedor')],
            [sg.Text("Quantidade Creatina"), sg.InputText(key='creatina')],
            [sg.Text("Scoop"), sg.InputText(key='scoop')],
            [sg.Text("Sexo"), sg.InputText(key='sexo')],
            [sg.Text("Idade"), sg.InputText(key='idade')],
            [sg.Text("Regiao"), sg.InputText(key='regiao')],
            [sg.Text("Status"), sg.InputText(key='status')],
            [sg.Button("Cadastrar"), sg.Button("Cancelar")]
        ]

# Create the Window
window = sg.Window('Hello Example', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    if event == 'Cadastrar':
        data = values['data']
        nome = values['nome']
        vendedor = values['vendedor']
        creatina = values['creatina']
        scoop = values['scoop']
        sexo = values['sexo']
        idade = values['idade']
        regiao = values['regiao']
        status = values['status']
        sg.popup(f'Data: {data}\nNome: {nome}\nVendedor: {vendedor}\nCreatina: {creatina}\nScoop: {scoop}\nSexo: {sexo}\nRegiao: {regiao}\nIdade: {idade}\nStatus: {status}')

window.close()
