# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from EffectTree import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl
import effectFunctions

class Ui_MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self._buffer = QtCore.QBuffer()

    def setupUi(self, MainWindow):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videowidget = QVideoWidget()

        self.tree = EffectTree(None) #makes default empty tree
        self.last_node = None

        videowidget.setGeometry(QtCore.QRect(200, 10, 871, 141))


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1091, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleText = QtWidgets.QLabel(self.centralwidget)
        self.titleText.setGeometry(QtCore.QRect(30, 10, 151, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.titleText.setFont(font)
        self.titleText.setTextFormat(QtCore.Qt.AutoText)
        self.titleText.setObjectName("titleText")

        self.playSlider = QtWidgets.QSlider(self.centralwidget)
        self.playSlider.setGeometry(QtCore.QRect(310, 20, 721, 41))
        self.playSlider.setOrientation(QtCore.Qt.Horizontal)
        self.playSlider.setObjectName("playSlider")
        self.playSlider.sliderMoved.connect(self.set_position)

        self.volumeAdjuster = QtWidgets.QSlider(self.centralwidget)
        self.volumeAdjuster.setEnabled(True)
        self.volumeAdjuster.setGeometry(QtCore.QRect(990, 340, 31, 201))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.volumeAdjuster.setFont(font)
        self.volumeAdjuster.setSliderPosition(50)
        self.volumeAdjuster.setOrientation(QtCore.Qt.Vertical)
        self.volumeAdjuster.setObjectName("volumeAdjuster")
        self.volumeLabel = QtWidgets.QLabel(self.centralwidget)
        self.volumeLabel.setGeometry(QtCore.QRect(970, 550, 61, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.volumeLabel.setFont(font)
        self.volumeLabel.setObjectName("volumeLabel")


        self.addReverb = QtWidgets.QPushButton(self.centralwidget)
        self.addReverb.setGeometry(QtCore.QRect(30, 200, 181, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.addReverb.setFont(font)
        self.addReverb.setObjectName("addReverb")
        self.addReverb.clicked.connect(self.add_reverb)

        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setGeometry(QtCore.QRect(400, 200, 181, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.applyButton.setFont(font)
        self.applyButton.setObjectName("applyEffect")
        self.applyButton.clicked.connect(self.applyEffect)

        self.addDistortion = QtWidgets.QPushButton(self.centralwidget)
        self.addDistortion.setGeometry(QtCore.QRect(30, 320, 191, 81))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.addDistortion.setFont(font)
        self.addDistortion.setObjectName("addDistortion")

        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setEnabled(False)
        self.playButton.setGeometry(QtCore.QRect(210, 30, 75, 23))
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.setObjectName("playButton")
        self.playButton.clicked.connect(self.play_video)
        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1091, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")


        self.menuUpload = QtWidgets.QMenu(self.menubar)
        self.menuUpload.setObjectName("menuUpload")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionUpload_File = QtWidgets.QAction(MainWindow)
        self.actionUpload_File.setObjectName("actionUpload_File")


        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuUpload.addAction(self.actionUpload_File)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuUpload.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionUpload_File.triggered.connect(self.open_file)


        # create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0, 0, 0, 0)

        # set widgets to the hbox layout

        hboxLayout.addWidget(self.playButton)
        hboxLayout.addWidget(self.playSlider)

        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)

        # self.setLayout(vboxLayout)
        #
        # self.mediaPlayer.setVideoOutput(videowidget)

        # media player signals

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

        # self._buffer = QtCore.QBuffer()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleText.setText(_translate("MainWindow", "NBSE"))
        self.volumeLabel.setText(_translate("MainWindow", "Volume"))
        self.addReverb.setText(_translate("MainWindow", "Add Reverb"))
        self.addDistortion.setText(_translate("MainWindow", "Add Distortion"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuUpload.setTitle(_translate("MainWindow", "Upload"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionUpload_File.setText(_translate("MainWindow", "Upload File"))


    def open_file(self):
        filename, ok = QtWidgets.QFileDialog.getOpenFileName(
            self, filter='WAV Files (*.wav)')

        if ok:
            f = open('tmpfile.wav', 'wb')
            k = open(filename, 'rb')
            f.write(k.read())
            k.close()
            f.close()
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playButton.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()


    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)

            )

        else:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)

            )

    def position_changed(self, position):
        self.playSlider.setValue(position)

    def duration_changed(self, duration):
        self.playSlider.setRange(0, duration)

    def reverb_simple(self):
        return effectFunctions.add_reverb(1000, 5, 2)

    def add_reverb(self):
        reverb_node = EffectNode(self.reverb_simple, 1, 1)
        connect(self.last_node, reverb_node, 0, 0)
        self.last_node = reverb_node
        #global 
        # global array
        # reverbAdded = effectFunctions.add_reverb(array, 1000, 5, 2)[0]
        # self._buffer.close()

        # self._buffer.setData(reverbAdded)


        # if self._buffer.open(QtCore.QIODevice.ReadOnly):
        #     self.mediaPlayer.setMedia(QMediaContent(), self._buffer)
        #     self.playButton.setEnabled(True)
    def applyEffect(self):
        mediaPlayerNode = EffectNode(self.setMediaPlayer, 1, 0)
        connect(self.last_node, mediaPlayerNode, 0, 0)
        mediaPlayerNode.apply()
    
    def setMediaPlayer(self, byteArray):
        self._buffer.close()
        self._buffer.setData(byteArray)
        if self._buffer.open(QtCore.QIODevice.ReadOnly):
            self.mediaPlayer.setMedia(QMediaContent(), self._buffer)
            self.playButton.setEnabled(True)
    def get_byte_array():
        global array
        return array




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

