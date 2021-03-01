from PyQt5 import QtWidgets
from ui import Ui_MainWindow
import os, sys
import serial
import json
import pygame

#############################################################################

class RunGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(RunGUI, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

##############################################################################
# data_test.py
  
# playing audio currently blocks the data receiving
# needs task parallelism

# import pygame and mute awkward stdout message
with open(os.devnull, 'w') as f:
   oldstdout = sys.stdout
   sys.stdout = f
   sys.stdout = oldstdout

# for receiving data from warning subsystem
ser = serial.Serial('/dev/ttyACM0', 115200)

def main():
    
   app = QtWidgets.QApplication(sys.argv)

   window = RunGUI()
   window.show()

   sys.exit(app.exec_())
    
   file = 'test.wav'
   wav = wave.open(file)
   freq = wav.getframerate()

   pygame.mixer.init(frequency=freq)
   pygame.mixer.music.load(file)

   while(1):
      data = ser.readline()

      # json.loads(data) parses the json string stored in the data
      # variable, and stores it back into the data variable as a
      # python dictionary.
      data = json.loads(data)

      # the string is formatted as follows:
      # {"leakDetected":<0 or 1>, "mic0":<value>, "mic1":<value> etc... }
      print('Leak detected = ' + str(data['leakDetected']) + '\n'
            'mic0 = ' + str(data['mic0']) + '\n'
            'mic1 = ' + str(data['mic1']) + '\n'
            'mic2 = ' + str(data['mic2']) + '\n'
            'mic3 = ' + str(data['mic3']) + '\n'
            'mic4 = ' + str(data['mic4']) + '\n'
            'mic5 = ' + str(data['mic5']) + '\n'
            'mic6 = ' + str(data['mic6']) + '\n'
            'mic7 = ' + str(data['mic7']) + '\n'
      )
      if data['leakDetected'] == 1:
         pygame.mixer.music.play()
         while pygame.mixer.music.get_busy() == True:
            continue
            
            
            
#####################################################################################            
        ## audio.py 
        # hides pygame welcome prompt to stdout
        with open(os.devnull, 'w') as f:
            oldstdout = sys.stdout
            sys.stdout = f


            sys.stdout = oldstdout



        file = 'test.wav'
        wav = wave.open(file)
        freq = wav.getframerate()

        pygame.mixer.init(frequency=freq)
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy() == True:
            continue
    

if __name__ == '__main__':
   main()



