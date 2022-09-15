import PySimpleGUI as sg
from stopwatch import Stopwatch
# ----------------  Create Form  ----------------
minut = 0
segundos = 0
millis = 0
stopwatch = Stopwatch(2)
stopwatch.reset()
sg.theme('Dark Amber')
tab1_layout =  [[sg.T('This is inside tab 1')],[sg.Text('')],
          [sg.Text('00:00:00', size=(8, 2), font=('Helvetica', 100),
                justification='center', key='text')],
          [sg.Button('Run', key='-RUN-PAUSE-', button_color=('white', '#001480')),
           sg.Button('Reset', button_color=('white', '#007339'), key='-RESET-'),
           sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]

tab2_layout = [[sg.T('This is inside tab 2')]]
layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])]]
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
    

            
    
    
    
# =============== Botões Funcionamento =================================================================================  
    if run:
        event, values = window.read(timeout=10)
    else:
        event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):        # ALWAYS give a way out of program
        break

window.close()