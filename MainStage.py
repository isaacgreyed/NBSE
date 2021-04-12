from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from EffectTree_examples import *


class MainStage(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainStage, self).__init__(*args, **kwargs)

        self.setGeometry(360, 250, 1550, 915)
        self.grid = QGridLayout()
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

        if name == "reverb":
            self.setStyleSheet("border: 3px solid black;\n"
                               "background-image: url(\"images/reverb_node.png\");")

        elif name == "distortion":
            self.setStyleSheet("border: 3px solid black;\n"
                               "background-image: url(\"images/distort_node.png\");")
        elif name == "chorus":
            self.setStyleSheet("border: 3px solid black;\n"
                               "background-image: url(\"images/chorus_node.png\");")
        elif name == "delay":
            self.setStyleSheet("border: 3px solid black;\n"
                               "background-image: url(\"images/delay_node.png\");")


    def paintEvent(self, event) -> None:
        painter = QPainter()
        painter.begin(self)
        rect    = event.rect()
        
        pen = QPen(Qt.blue)
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(0, 15, -250, 15)  # Middle line
        painter.drawLine(65, 15, 150, 15)   # Middle line
        painter.setPen(QPen(Qt.blue, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        painter.drawEllipse(60, 10, 10, 10)
        painter.drawEllipse(150, 10, 10, 10)
        painter.end()
