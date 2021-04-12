from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from EffectTree_examples import *


class MainStage(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainStage, self).__init__(*args, **kwargs)

        self.width  = 1550
        self.height = 915

        self.grid = QGridLayout()
        #self.grid.setSpacing(10)

        self.setFixedSize(800, 400)

        self.move(400,200)

        w = QHBoxLayout()
        w.addLayout(self.grid)

        self.setLayout(w)

        self.show()

    def setGrid(self, effect_list):
        for i in range(0, len(effect_list)):
            (name, effect) = effect_list[i]
            n = Node(self, name)
            # label = QLabel(self)
            # label.setText(name)
            self.grid.addWidget(n, 1, i)

class Node(QWidget):
    def __init__(self, parent, name, *args, **kwargs):
        super(Node, self).__init__(parent, *args, **kwargs)
        self.height = 200
        self.width  = 200
        self.setFixedSize(self.width, self.height)
        self.name = name

        label = QLabel(self)
        label.setText(name)

        self.setStyleSheet("border: 3px solid black;")

    def paintEvent(self, event) -> None:
        painter = QPainter()
        painter.begin(self)
        rect    = event.rect()
        
        pen = QPen(Qt.blue)
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(65, 10, 100, 10)
        painter.drawLine(100, 10, 90, 0)
        painter.drawLine(100, 10, 90, 20)
        painter.end()
