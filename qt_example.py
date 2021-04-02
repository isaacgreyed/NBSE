#!/usr/bin/python

import sys
#from PyQt5.QtWidgets import (QWidget, QToolTip,
#    QPushButton, QApplication, QLineEdit, QLabel)

#from PyQt5.QtGui import (QImage, QPalette, QBrush, QFont)
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
<<<<<<< Updated upstream

=======
import effect
>>>>>>> Stashed changes
from PyQt5 import QtCore, QtWidgets

from pyo import *
from scipy.io.wavfile import read
from EffectTree import *

from MainStage import *

file = r"sample.wav"


class NBSEWindow(QMainWindow):

    def __init__(self):
        super(NBSEWindow, self).__init__()

        # Window Visual Design
        # Set to be unscalable 1920x1080
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setFixedSize(1920, 1080)
        self.setStyleSheet("background-image: url(\"images/pgmtexture.png\");\n")
        self.setWindowTitle('Node Based Sound Editor')
        winIcon = QIcon("images/icon.png")
        self.setWindowIcon(winIcon)

        # Initialize user interface
        self.initUI()


    def initUI(self):

        # Filename text box
        # Must modify code to accomodate longer text file names.
        self.textbox_label = QLabel(self)
        self.textbox_label.move(20, 0)
        self.textbox_label.setText("Current filename: " + file)
        self.textbox_label.setGeometry(0, 0, 300, 300)

        # Reverb button
        self.reverb_btn = QPushButton('Reverb', self)
        self.reverb_btn.clicked.connect(reverb)
        self.reverb_btn.clicked.connect(lambda: self.changeEffectText(1))
        self.reverb_btn.move(50, 30)
        self.reverb_btn.setGeometry(30, 350, 125, 125)
        self.reverb_btn.setStyleSheet("border-radius: 25px;\n"
"background: #73AD21;\n"
"padding: 20px;\n"
"width: 200px;\n"
"height: 150px;\n"
"background-image: url(\"images/btntexture.png\");")

        # Distort Button
        self.distort_btn = QPushButton('Distortion', self)
        self.distort_btn.clicked.connect(distortion)
        self.distort_btn.clicked.connect(lambda: self.changeEffectText(2))
        self.distort_btn.move(50, 55)
        self.distort_btn.setGeometry(210, 350, 125, 125)
        self.distort_btn.setStyleSheet("border-radius: 25px;\n"
"background: #73AD21;\n"
"padding: 20px;\n"
"width: 200px;\n"
"height: 150px;\n"
"background-image: url(\"images/btntexture.png\");")

        # Effect text box
        # png for background needs to be improved.
        self.effect_Textbox = QLabel(self, wordWrap=True)
        self.effect_Textbox.setText("This is an example. ")
        self.effect_Textbox.setGeometry(9, 600, 350, 400)
        self.effect_Textbox.setStyleSheet("border: 3px solid black;\n"
"background-image: url(\"images/effectTextbg.png\");")
        self.effect_Textbox.setAlignment(QtCore.Qt.AlignLeft)
        #self.effect_Textbox.move(100, 100)


    # Changes a label to display what an effect does when clicked.
    def changeEffectText(self, func):
        reverb = "Reverb\nThis creates a resounding effect " \
                 "that simulates a resonance of sound off of a surface."

        distortion = "Distortion\nThis creates an effect that simulates" \
                     "a sine-wave of data being modified in a particular" \
                     "direction."
        if func == 1:
            self.effect_Textbox.setText(reverb)
        elif func == 2:
            self.effect_Textbox.setText(distortion)
        else:
            self.effect_Textbox.setText("Error")

        textbox_label = QLabel(self)
        textbox_label.move(20,0)
        textbox_label.setText("Current filename: " + file)

        #textbox = QLineEdit(self)
        #textbox.move(20, 80)
        #textbox.resize(140,20)

        test = Node(self)
        test.move(50, 50)
        
        m = MainStage(self)
        test.move(100,100)
        #test.update()

        test.show()

        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('NBSE')
        self.show()

# Adds a reverberation effect to audio.
def reverb():
    # Apply Audio Effect
    s = Server(audio="offline").boot()
    filedur = sndinfo(file)[1]
    s.recordOptions(dur=filedur, filename=r"sample_reverbed.wav")
    ifile = SfPlayer(file)

    filter = Biquad(ifile, freq=1000, q=5, type=2).out()
    s.start()

    filteredFile = r"sample.wav"
    f = open(filteredFile, 'rb')
    f = f.read()
    return f


def distortion():
    s = Server(audio="offline").boot()
    filedur = sndinfo(file)[1]
    s.recordOptions(dur=filedur, filename=r"sample_distorted.wav")
    ifile = SfPlayer(file)

    lfo = Sine(freq=[.2, .25], mul=.5, add=.5)
    filter = Disto(ifile, drive=lfo, slope=.8, mul=.15).out()
    s.start()
    filteredFile = r"sample.wav"
    f = open(filteredFile, 'rb')
    f = f.read()

    return f


def main():
    

    app = QApplication(sys.argv)
    ex = NBSEWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()