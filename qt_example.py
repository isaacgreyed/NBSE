#!/usr/bin/python

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QLineEdit, QLabel)
from PyQt5.QtGui import QFont
from pyo import *
from scipy.io.wavfile import read
from EffectTree import *

from MainStage import *

file = r"sample.wav"


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        
        reverb_btn = QPushButton('Apply Reverb', self)
        reverb_btn.clicked.connect(reverb)
        reverb_btn.resize(reverb_btn.sizeHint())
        reverb_btn.move(50, 30)

        distort_btn = QPushButton('Apply Distortion', self)
        distort_btn.clicked.connect(distortion)
        distort_btn.resize(distort_btn.sizeHint())
        distort_btn.move(50, 55)

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

def reverb():

    # Change text box
    reverbDesc = "Reverb creates a resounding echo effect."
    textbox_label.setText(reverbDesc)
    textbox_label.adjustSize()

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
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()