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
        #self.setFixedSize(self.width, self.height)
        self.name = name

        label = QLabel(self)
        label.setText(name)


        if name == "reverb":
            label.setStyleSheet("border: 3px solid black;\n"
                               "background-image: url(\"images/reverb_node.png\");")
            p1_label = QLabel(self)
            p1_label.setText("Parameter 1")
            p1_label.setGeometry(50, 0, 120,30)
            param1 = QSlider(Qt.Horizontal, self)
            param1.setGeometry(0, 30, 200, 30)

            p2_label = QLabel(self)
            p2_label.setText("Parameter 2")
            p2_label.setGeometry(50, 80, 120, 30)
            param2 = QSlider(Qt.Horizontal, self)
            param2.setGeometry(0, 110, 200, 30)

            p3_label = QLabel(self)
            p3_label.setText("Parameter 3")
            p3_label.setGeometry(50, 160, 120, 30)
            param3 = QSlider(Qt.Horizontal, self)
            param3.setGeometry(0, 190, 200, 30)

        elif name == "distortion":
            label.setStyleSheet("border: 3px solid black;\n"
                               "background-image: url(\"images/distort_node.png\");")
        elif name == "chorus":
            label.setStyleSheet("border: 3px solid black;\n"
                               "background-image: url(\"images/chorus_node.png\");")
        elif name == "delay":
            label.setStyleSheet("border: 3px solid black;\n"
                               "background-image: url(\"images/delay_node.png\");")

        label.setGeometry(0, 250, 100, 30)

    def paintEvent(self, event) -> None:
        painter = QPainter()
        painter.begin(self)
        rect    = event.rect()
        
        pen = QPen(Qt.blue)
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(0, 265, -250, 265)  # Middle line
        painter.drawLine(65, 265, 150, 265)   # Middle line
        painter.setPen(QPen(Qt.blue, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        painter.drawEllipse(60, 260, 10, 10)
        painter.drawEllipse(150, 260, 10, 10)
        painter.end()
