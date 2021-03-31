#!/usr/bin/python

import sys
#from PyQt5.QtWidgets import (QWidget, QToolTip,
#    QPushButton, QApplication, QLineEdit, QLabel)

#from PyQt5.QtGui import (QImage, QPalette, QBrush, QFont)
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtWidgets

from pyo import *
from scipy.io.wavfile import read

file = r"sample.wav"


class NBSEWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Node Based Sound Editor v1")
        QWidget.__init__(self)  #What does this do?

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setFixedSize(1920, 1080)
        self.setStyleSheet("background-image: url(\"images/pgmtexture.png\");\n")
        self.setWindowTitle('Node Based Sound Editor')
        winIcon = QIcon("images/icon.png")
        self.setWindowIcon(winIcon)

        reverb_btn = QPushButton('Reverb', self)
        reverb_btn.clicked.connect(reverb)
        reverb_btn.resize(reverb_btn.sizeHint())
        reverb_btn.move(50, 30)
        reverb_btn.setGeometry(30, 350, 125, 125)
        reverb_btn.setStyleSheet("border-radius: 25px;\n"
"background: #73AD21;\n"
"padding: 20px;\n"
"width: 200px;\n"
"height: 150px;\n"
"background-image: url(\"images/btntexture.png\");")

        distort_btn = QPushButton('Distortion', self)
        distort_btn.clicked.connect(distortion)
        distort_btn.resize(distort_btn.sizeHint())
        distort_btn.move(50, 55)
        distort_btn.setGeometry(210, 350, 125, 125)
        distort_btn.setStyleSheet("border-radius: 25px;\n"
"background: #73AD21;\n"
"padding: 20px;\n"
"width: 200px;\n"
"height: 150px;\n"
"background-image: url(\"images/btntexture.png\");")


        textbox_label = QLabel(self)
        textbox_label.move(20,0)
        textbox_label.setText("Current filename: " + file)

        textbox = QLineEdit(self)
        textbox.move(20, 80)
        textbox.resize(140,20)


        self.show()

def changeTextBox(text):
    textbox_label.setText(reverbDesc)
    textbox_label.adjustSize()

def reverb():

    # Change text box
    reverbDesc = "Reverb creates a resounding echo effect."
    changeTextBox(reverbDesc)

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
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
