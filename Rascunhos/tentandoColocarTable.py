import PySimpleGUI as sg
from stopwatch import Stopwatch
# ----------------  Create Form  ----------------
minut = 0
segundos = 0
millis = 0
stopwatch = Stopwatch(2)
stopwatch.reset()
headings = ['Tempo da Equipe']
collectInfo_Array_Equipe1 = []
collectInfo_Array_Equipe2 = []
collectInfo_Array_Equipe3 = []
collectInfo_Array_Equipe4 = []
sg.theme('Dark Amber')
frame_layout = [
                [sg.T('')],
                [sg.T('')],
                [sg.Combo(['Equipe 1','Equipe 2','Equipe 3','Equipe 4'], key='combo')],
                [sg.T('')],
                [sg.T('')],
                [sg.Button('Run', key='-RUN-PAUSE-', button_color=('white', '#001480')),
                sg.Button('Reset', button_color=('white', '#007339'), key='-RESET-'),
                sg.Button('CLK', button_color=('white', '#3e3e3e'), key='-CLK-'),
                sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]


tab1_layout =  [[sg.T('Cronometro')],[sg.Text('')],
          [sg.Text('00:00:000', size=(8, 2), font=('Helvetica', 100),
                justification='center', key='text')],[sg.Frame('My Frame Title', frame_layout, font='Any 12', title_color='blue', element_justification='c')]]


tabelaEquipe1_layout = [sg.Table(values=collectInfo_Array_Equipe1,
                                 headings = headings,
                                 max_col_width=35,
                                 num_rows=10,
                                 auto_size_columns=True,
                                 display_row_numbers=False,
                                 justification='c',
                                 key='-myTable1-')]
tabelaEquipe2_layout = [sg.Table(values=collectInfo_Array_Equipe2,
                                 headings = headings,
                                 max_col_width=35,
                                 num_rows=10,
                                 auto_size_columns=True,
                                 display_row_numbers=False,
                                 justification='c',
                                 key='-myTable2-')]
tabelaEquipe3_layout = [sg.Table(values=collectInfo_Array_Equipe3,
                                 headings = headings,
                                 max_col_width=35,
                                 num_rows=10,
                                 auto_size_columns=True,
                                 display_row_numbers=False,
                                 justification='c',
                                 key='-myTable3-')]
tabelaEquipe4_layout = [sg.Table(values=collectInfo_Array_Equipe4,
                                 headings = headings,
                                 max_col_width=35,
                                 num_rows=10,
                                 auto_size_columns=True,
                                 display_row_numbers=False,
                                 justification='c',
                                 key='-myTable4-')]



equipeTab1_layout = [[sg.T('Aqui ficaria a tabela da equipe 1')], tabelaEquipe1_layout]
equipeTab2_layout = [[sg.T('Aqui ficaria a tabela da equipe 2')], tabelaEquipe2_layout]
equipeTab3_layout = [[sg.T('Aqui ficaria a tabela da equipe 3')], tabelaEquipe3_layout]
equipeTab4_layout = [[sg.T('Aqui ficaria a tabela da equipe 4')], tabelaEquipe4_layout]



tab2_layout = [[sg.T('Tabela com os tempos e Nome da Equipe')],
               [sg.TabGroup([[sg.Tab('Equipe 1 Table', equipeTab1_layout, element_justification='c'),
                              sg.Tab('Equipe 2 Table', equipeTab2_layout, element_justification='c'),
                              sg.Tab('Equipe 3 Table', equipeTab3_layout, element_justification='c'),
                              sg.Tab('Equipe 4 Table', equipeTab4_layout, element_justification='c')]])]
               ]

layout = [[sg.TabGroup([[sg.Tab('Cronometro', tab1_layout, element_justification='c'), sg.Tab('Tabela com os tempos e Nome da Equipe', tab2_layout, element_justification='c')]])]]
window = sg.Window('Linus Cronometro', layout,
                   resizable=True,
                   no_titlebar=False,
                   auto_size_buttons=False,
                   keep_on_top=True,
                   grab_anywhere=True,
                   element_padding=(100, 10),
                   finalize=True,
                   element_justification='c',
                   right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT)
run = False
while True:
    if run:
        stopwatch.start()
    
# ========================== Conversão e Leitura =================================================================================
    if True:
        totalSec = stopwatch.duration
        millisTotal = 1000*totalSec
        segundos = int(millisTotal/1000)
        minutos = int(millisTotal/60000)
        millis = int(millisTotal)
        if(segundos >= 59):
            segundos = segundos % 60
        if(millis >= 999):
            millis = millis % 1000
            
# ======================================================================================================================
    
    
    
# =============== Botões Funcionamento =================================================================================  
    if run:
        event, values = window.read(timeout=10)
    else:
        event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):        # ALWAYS give a way out of program
        break
    if event == '-RUN-PAUSE-':
        if run == False:
            stopwatch.start()
            run = True
        elif run == True:
            stopwatch.stop()
            run = False
    #Tendo apertar 2 vezes o botão reset(só usar caso o carro saia da pista - da para contornar o bug)        
    if event == '-RESET-':
        stopwatch.reset()
        minutos = 0
        segundos = 0
        millis = 0
        run=False
        print('{:02d}:{:02d}:{:03d}'.format(minutos,segundos,millis))
#============================================================================================================
#==================== Evento da Seleção de Equipes ==========================================================
    if event == '-CLK-' and values['combo']=='Equipe 1':
        collected = '{:02d}:{:02d}:{:03d}'.format(minutos,segundos,millis)
        collectedArray = [collected]
        collectInfo_Array_Equipe1.append(collectedArray)
        window['-myTable1-'].update(values=collectInfo_Array_Equipe1)        

    if event == '-CLK-' and values['combo']=='Equipe 2':
        collected = '{:02d}:{:02d}:{:03d}'.format(minutos,segundos,millis)
        collectedArray = [collected]
        collectInfo_Array_Equipe2.append(collectedArray)
        window['-myTable2-'].update(values=collectInfo_Array_Equipe2)        

    if event == '-CLK-' and values['combo']=='Equipe 3':
        collected = '{:02d}:{:02d}:{:03d}'.format(minutos,segundos,millis)
        collectedArray = [collected]
        collectInfo_Array_Equipe3.append(collectedArray)
        window['-myTable3-'].update(values=collectInfo_Array_Equipe3)        

    if event == '-CLK-' and values['combo']=='Equipe 4':
        collected = '{:02d}:{:02d}:{:03d}'.format(minutos,segundos,millis)
        collectedArray = [collected]
        collectInfo_Array_Equipe4.append(collectedArray)
        window['-myTable4-'].update(values=collectInfo_Array_Equipe4)        
#=======================================================================================================



# ===========================================================================================================================
    window['text'].update('{:02d}:{:02d}:{:03d}'.format(minutos,segundos,millis))
    print(run)
    window['-RUN-PAUSE-'].update('Run' if not run else 'Pause')
window.close()