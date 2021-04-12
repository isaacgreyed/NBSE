# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from shutil import copyfile
import os
from EffectTree import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import effectFunctions
import MainStage

class Ui_MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self._buffer = QtCore.QBuffer()
        winIcon = QIcon("images/icon.png")
        MainWindow.setWindowIcon(winIcon)

    def setupUi(self, MainWindow):

        # To hold list of added effects.
        self.effect_list = []

        # To hold list of previously applied effects.
        self.oldeffect_list = []

        # To hold filepath of wav
        self.filepath = ""


        # Media Player Initialized
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        videowidget.setGeometry(QtCore.QRect(200, 10, 871, 141))

        # Display Options for Window
        MainWindow.setObjectName("NBSE")
        MainWindow.setFixedSize(1920, 1080)
        MainWindow.setStyleSheet("background-image: url(\"images/pgmtexture.png\");\n")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # Play Button to play or pause a selected audio file.
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setEnabled(False)
        self.playButton.setGeometry(QtCore.QRect(550, 15, 50, 50))
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.setObjectName("playButton")
        self.playButton.clicked.connect(self.play_video)

        # Slider for playing audio.
        self.playSlider = QtWidgets.QSlider(self.centralwidget)
        self.playSlider.setGeometry(QtCore.QRect(600, 20, 721, 41))
        self.playSlider.setOrientation(QtCore.Qt.Horizontal)
        self.playSlider.setObjectName("playSlider")
        self.playSlider.sliderMoved.connect(self.set_position)

        # Volume Adjuster to modify volume
        self.volumeAdjuster = QtWidgets.QSlider(self.centralwidget)
        self.volumeAdjuster.setEnabled(True)
        self.volumeAdjuster.setRange(0,100)
        self.volumeAdjuster.setGeometry(QtCore.QRect(1350, -60, 31, 201))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.volumeAdjuster.setFont(font)
        self.volumeAdjuster.setSliderPosition(50)
        self.volumeAdjuster.setOrientation(QtCore.Qt.Vertical)
        self.volumeAdjuster.setObjectName("volumeAdjuster")
        self.volumeAdjuster.sliderMoved.connect(self.set_volume)
        
        self.volumeLabel = QtWidgets.QLabel(self.centralwidget)
        self.volumeLabel.setGeometry(QtCore.QRect(1333, 135, 61, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.volumeLabel.setFont(font)
        self.volumeLabel.setObjectName("volumeLabel")

        # Initilizes Effect Stage
        self.mainStage = MainStage.MainStage(self.centralwidget)
        self.mainStage.setGrid(self.effect_list)
        self.mainStage.update()


        # Reverb Button
        self.addReverb = QtWidgets.QPushButton("Reverb", self.centralwidget)
        self.addReverb.clicked.connect(self.add_reverb)
        self.addReverb.clicked.connect(lambda: self.changeEffectText(1))
        self.addReverb.setGeometry(30, 300, 125, 125)
        self.addReverb.setStyleSheet("border-radius: 25px;\n"
                                      "background: #73AD21;\n"
                                      "padding: 20px;\n"
                                      "width: 200px;\n"
                                      "height: 150px;\n"
                                      "background-image: url(\"images/btntexture.png\");")

        # Delay Button
        self.addDelay = QtWidgets.QPushButton("Delay", self.centralwidget)
        self.addDelay.clicked.connect(self.add_delay)
        self.addDelay.clicked.connect(lambda: self.changeEffectText(2))
        self.addDelay.setGeometry(210, 300, 125, 125)
        self.addDelay.setStyleSheet("border-radius: 25px;\n"
                                       "background: #73AD21;\n"
                                       "padding: 20px;\n"
                                       "width: 200px;\n"
                                       "height: 150px;\n"
                                       "background-image: url(\"images/btntexture.png\");")

        # Distortion Button
        self.addDistortion = QtWidgets.QPushButton("Distort", self.centralwidget)
        self.addDistortion.clicked.connect(self.add_distortion)
        self.addDistortion.clicked.connect(lambda: self.changeEffectText(3))
        self.addDistortion.setGeometry(30, 450, 125, 125)
        self.addDistortion.setStyleSheet("border-radius: 25px;\n"
                                     "background: #73AD21;\n"
                                     "padding: 20px;\n"
                                     "width: 200px;\n"
                                     "height: 150px;\n"
                                     "background-image: url(\"images/btntexture.png\");")
        # Chorus Button
        self.addChorus = QtWidgets.QPushButton("Chorus", self.centralwidget)
        self.addChorus.clicked.connect(self.add_chorus)
        self.addChorus.clicked.connect(lambda: self.changeEffectText(4))
        self.addChorus.setGeometry(210, 450, 125, 125)
        self.addChorus.setStyleSheet("border-radius: 25px;\n"
                                         "background: #73AD21;\n"
                                         "padding: 20px;\n"
                                         "width: 200px;\n"
                                         "height: 150px;\n"
                                         "background-image: url(\"images/btntexture.png\");")

        # Apply Button
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.clicked.connect(self.applyEffect)
        self.applyButton.setGeometry(400, 200, 181, 71)
        self.applyButton.setStyleSheet("background-image: url(\"images/apply_btn.png\");")


        # Remove Effect Button
        self.remove_Last = QtWidgets.QPushButton(self.centralwidget)
        self.remove_Last.clicked.connect(self.removeLast)
        self.remove_Last.setGeometry(600, 200, 181, 71)
        self.remove_Last.setStyleSheet("background-image: url(\"images/removelast_btn.png\");")

        # Remove All Effects Button
        self.remove_All = QtWidgets.QPushButton(self.centralwidget)
        self.remove_All.clicked.connect(self.removeAll)
        self.remove_All.setGeometry(QtCore.QRect(800, 200, 181, 71))
        self.remove_All.setStyleSheet("background-image: url(\"images/removeall_btn.png\");")

        # Effect text box
        # png for background needs to be improved.
        self.effect_Textbox = QLabel(self.centralwidget, wordWrap=True)
        self.effect_Textbox.setText("Please check the guide to learn everything you need to know about NBSE. Try "
                                    "uploading a .wav file first!")
        self.effect_Textbox.setGeometry(9, 600, 350, 400)
        self.effect_Textbox.setAlignment(QtCore.Qt.AlignLeft)
        self.effect_Textbox.setStyleSheet("border: 3px solid black;\n"
                                          "background-image: url(\"images/effectTextbg.png\");")

        # File name text box
        self.file_Textbox = QLabel(self.centralwidget, wordWrap=True)
        self.file_Textbox.setText("Upload a .wav file!")
        self.file_Textbox.setGeometry(800, -10, 200, 50)
        self.file_Textbox.setAlignment(QtCore.Qt.AlignCenter)
        self.file_Textbox.setStyleSheet("border: 3px solid black;\n"
                                          "background-image: url(\"images/effectTextbg.png\");")

        # Upload, load, and save files.
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1091, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("background-color: gray;")

        # Save or Load a file.
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        # Upload a file
        self.menuUpload = QtWidgets.QMenu(self.menubar)
        self.menuUpload.setObjectName("menuUpload")


        # Sets menu bar for file access.
        MainWindow.setMenuBar(self.menubar)

        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionUpload_File = QtWidgets.QAction(MainWindow)
        self.actionUpload_File.setObjectName("actionUpload_File")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.triggered.connect(sys.exit)
        self.actionQuit.setText("Quit")
        
        self.actionSave.triggered.connect(self.save_file)

        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
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

        # Media player changes when files are added
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    # When a button is clicked, changes the effect.
    def changeEffectText(self, func):
        reverb = "Reverb\nThis creates a resounding effect " \
                 "that simulates a resonance of sound off of a surface."
        delay = "Delay\nThis delays the output, creating a pausing effect."

        distortion = "Distortion\nThis creates an effect that simulates" \
                         "a sine-wave of data being modified in a particular" \
                         "direction."
        chorus = "Chorus\nThis creates a resounding effect in the background."
        if func == 1:
            self.effect_Textbox.setText(reverb)
        elif func == 2:
            self.effect_Textbox.setText(delay)
        elif func == 3:
            self.effect_Textbox.setText(distortion)
        elif func == 4:
            self.effect_Textbox.setText(chorus)
        else:
            self.effect_Textbox.setText("Error")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NBSE"))
        #self.titleText.setText(_translate("MainWindow", "NBSE"))
        self.volumeLabel.setText(_translate("MainWindow", "Volume"))
        self.addReverb.setText(_translate("MainWindow", "Reverb"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuUpload.setTitle(_translate("MainWindow", "Upload"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionUpload_File.setText(_translate("MainWindow", "Upload File"))


    def open_file(self):
        filename, ok = QtWidgets.QFileDialog.getOpenFileName(
            self, filter='WAV Files (*.wav)')

        # Puts file path in universal variable.
        self.filepath = filename
        self.file_Textbox.setText(self.filepath.rsplit('/', 1)[-1])
        if ok:
            self.effect_list = []
            self.updateGrid()
            os.remove('tmpfile.wav')
            f = open('tmpfile.wav', 'wb')
            k = open(filename, 'rb')
            f.write(k.read())
            k.close()
            f.close()
            
            f = open('original.wav', 'wb')
            k = open(filename, 'rb')
            f.write(k.read())
            k.close()
            f.close()
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playButton.setEnabled(True)


    def save_file(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        
        file = open(name[0]+'.wav','wb')
        file2 = open(r'tmpfile.wav', 'rb')
        file.write(file2.read())
        file.close()
        file2.close()


    def update_player(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('tmpfile.wav')))


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

    def set_volume(self):
        self.mediaPlayer.setVolume(self.volumeAdjuster.value())

    def position_changed(self, position):
        self.playSlider.setValue(position)


    def duration_changed(self, duration):
        self.playSlider.setRange(0, duration)


    def delay_simple(self):
        effectFunctions.add_delay(1.2, 1.6, 0.8, 0.9)
        effectFunctions.remove()


    def add_delay(self):
        self.effect_list.append(("delay", self.delay_simple))
        self.updateGrid()


    def chorus_simple(self):
        effectFunctions.add_chorus(2, 4, 0.25, 0.8)
        effectFunctions.remove()


    def add_chorus(self):
        self.effect_list.append(("chorus", self.chorus_simple))
        self.updateGrid()


    def distortion_simple(self):
        effectFunctions.add_distortion(0.6, 0.7)
        effectFunctions.remove()


    def add_distortion(self):
        self.effect_list.append(("distortion", self.distortion_simple))
        self.updateGrid()


    def reverb_simple(self):
        effectFunctions.add_reverb(1000, 5, 2)
        effectFunctions.remove()


    def add_reverb(self):
        self.effect_list.append(("reverb", self.reverb_simple))
        self.updateGrid()
        

    def applyEffect(self):

        if self.filepath == "":
            self.effect_Textbox.setText("Please upload a file before applying effects.")
        #elif self.effect_list == self.oldeffect_list:
        #    self.effect_Textbox.setText("Effects have not changed since last Apply.")
        else:
            if len(self.effect_list) == 0:
                self.effect_Textbox.setText("No effects applied.")
            elif len(self.effect_list) == 1:
                self.effect_Textbox.setText("Effect applied.")
            else:
                self.effect_Textbox.setText("Effects applied.")

            self.oldeffect_list = self.effect_list

            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('sample_distorted.wav')))
            os.remove('tmpfile.wav')
            copyfile("original.wav", 'tmpfile.wav')
            for (name, effect) in self.effect_list:
                effect()
            self.update_player()


    def removeLast(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('sample_distorted.wav')))

        if self.effect_list != []:
            self.effect_list.pop()[0]
            self.updateGrid()
            self.update_player()
            self.effect_Textbox.setText("Effect has been removed.")
        else:
            self.effect_Textbox.setText("No effects are staged.")


    def removeAll(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('sample_distorted.wav')))
        if len(self.effect_list) == 0:
            self.effect_Textbox.setText("No effects are staged.")
        else:
            reply = QMessageBox.information(
                                            self,
                                            "Remove All Effects",
                                            "This will remove all effects, are you sure?",
                                             QMessageBox.Yes | QMessageBox.Cancel
                                            )
            if reply == QtWidgets.QMessageBox.Yes:
                self.effect_list = []
                self.updateGrid()
                self.update_player()
                self.effect_Textbox.setText("All effects have been removed.")
            else:
                self.effect_Textbox.setText("Effects have been maintained.")



    def updateGrid(self):
        if self.mainStage:
            self.mainStage.setParent(None)
        self.mainStage = MainStage.MainStage(self.centralwidget)
        self.mainStage.setGrid(self.effect_list)
        self.mainStage.update()
        self.mainStage.lower()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
