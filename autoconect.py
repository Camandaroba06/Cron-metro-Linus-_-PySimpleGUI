# WaveShapePlay
# Find a detailed youtube tutorial for the Arduino Com Connection Code at: https://youtu.be/DJD28uK5qIk
import serial.tools.list_ports
def get_ports():
    ports = serial.tools.list_ports.comports(include_links=False)
    for p in ports:
        print(p.device)
    print(len(ports), 'ports found')
    return ports

def findArduino(portsFound):
    
    commPort = 'None'
    numConnection = len(portsFound)
    print(numConnection)
    for i in range (0, numConnection):
        port = foundPorts[i]
        strPort = str(port)
        print(strPort)
        if 'SERIAL' in strPort: 
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])
    print(commPort)
    return commPort
            
                    
foundPorts = get_ports()        
connectPort = findArduino(foundPorts)

if connectPort != 'None':
    print('Connected to ' + connectPort)

else:
    print('Connection Issue!')

print('DONE')





    
