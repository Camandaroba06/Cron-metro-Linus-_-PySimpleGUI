import PySimpleGUI as sg
from stopwatch import Stopwatch
# ----------------  Create Form  ----------------
minut = 0
segundos = 0
millis = 0
stopwatch = Stopwatch(2)
stopwatch.reset()
sg.theme('Black')


sg.theme('Dark Amber')
layout = [[sg.Text('')],
          [sg.Text('00:00:00', size=(8, 2), font=('Helvetica', 100),
                justification='center', key='text')],
          [sg.Button('Run', key='-RUN-PAUSE-', button_color=('white', '#001480')),
           sg.Button('Reset', button_color=('white', '#007339'), key='-RESET-'),
           sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]

window = sg.Window('Running Timer', layout,
                   resizable=True,
                   no_titlebar=False,
                   auto_size_buttons=False,
                   keep_on_top=True,
                   grab_anywhere=True,
                   element_padding=(0, 0),
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
        run=False
        print('{:02d}:{:02d}:{:03d}'.format(minutos,segundos,millis))
# ===========================================================================================================================
    window['text'].update('{:02d}:{:02d}:{:03d}'.format(minutos,segundos,millis))
    print(run)
    window['-RUN-PAUSE-'].update('Run' if not run else 'Pause')
window.close()