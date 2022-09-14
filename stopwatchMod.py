from stopwatch import Stopwatch
running = False
minut = 0
segundos = 0
millis = 0
# Argument specifies decimal precision for __str__
# e.g 2 digits = 1.00, 3 digits = 1.000
# Optional, defaults to 2
stopwatch = Stopwatch(2)
stopwatch.reset()
# It's just math with time.perf_counter() so there isn't really a task
# running in background

# stopwatch.stop()  # Stop stopwatch, time freezes
# stopwatch.start()  # Start it again
# stopwatch.reset()  # Reset it back to 0
# stopwatch.restart()  # Reset and start again
# stopwatch.running  # Wether stopwatch is running
# x = stopwatch.duration  # Get the duration (in seconds)
while True:
    stopwatch.start()
    running = True
    if running:
        totalSec = stopwatch.duration
        millisTotal = 1000*totalSec
        segundos = int(millisTotal/1000)
        minutos = int(millisTotal/60000)
        millis = int(millisTotal)
        if(segundos >= 59):
            segundos = segundos % 60
        if(millis >= 999):
            millis = millis % 1000
        print("Min: " + str(minutos) + " " + "Segundos: " +
              str(segundos)+" " + "Milisegundos: " + str(millis))
