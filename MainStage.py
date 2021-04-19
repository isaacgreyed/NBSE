from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from EffectTree_examples import *

slider_list = []

class MainStage(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainStage, self).__init__(*args, **kwargs)

        self.setGeometry(360, 250, 1550, 915)
        self.grid = QGridLayout()
        w = QHBoxLayout()
        w.addLayout(self.grid)
        self.setLayout(w)
        self.show()

<<<<<<< HEAD
    def setGrid(self, effect_list):
        for i in range(0, len(effect_list)):
            (name, _, _) = effect_list[i]
            n = Node(self, name)
            # label = QLabel(self)
            # label.setText(name)
            self.grid.addWidget(n, 1, i)
=======
    def setGrid(self, node_list):
        for i in range(0, len(node_list)):
            row = 1
            while i > 6:
                row += 1
                i -= 7
            self.grid.addWidget(node_list[i], row, i)
>>>>>>> main

class Node(QWidget):
    def __init__(self, parent, name, position, *args, **kwargs):
        super(Node, self).__init__(parent, *args, **kwargs)
        self.height = 150
        self.width  = 200
        #self.setFixedSize(self.width, self.height)
        self.name = name
        self.position = position
        label = QLabel(self)
        label.setText(name)
        label.setGeometry(0, 100, 80, 80)

        self.param_list = []

        if name == "reverb":
            label.setStyleSheet("border: 3px solid black;\n"
                               "background-image: url(\"images/reverb_node.png\");")
            p1_label = QLabel(self)
            p1_label.setText("Parameter 1")
            p1_label.setGeometry(50, 0, 120,30)
            p1_label.setStyleSheet("background-image: url(\"images/reverblabel.png\");")
            param1 = QSlider(Qt.Horizontal, self)
            param1.setMinimum(1)
            param1.setMaximum(1000)
            param1.setGeometry(0, 30, 200, 30)
            param1.setStyleSheet("background-image: url(\"images/sliderbg.png\");")
            param1.setTickPosition(QSlider.TicksBelow)
            param1.setTickInterval(100)
            param1.sliderReleased.connect(self.slider_changed)
            self.param_list.append((param1, 1))

            p2_label = QLabel(self)
            p2_label.setText("Parameter 2")
            p2_label.setGeometry(50, 80, 120, 30)
            p2_label.setStyleSheet("background-image: url(\"images/reverblabel.png\");")
            param2 = QSlider(Qt.Horizontal, self)
            param2.setGeometry(0, 110, 200, 30)
            param2.setStyleSheet("background-image: url(\"images/sliderbg.png\");")
            param2.setMinimum(1)
            param2.setMaximum(5)
            param2.setTickPosition(QSlider.TicksBelow)
            param2.setTickInterval(1)
            param2.sliderReleased.connect(self.slider_changed)
            self.param_list.append((param2, 1))

            p3_label = QLabel(self)
            p3_label.setText("Parameter 3")
            p3_label.setGeometry(50, 160, 120, 30)
            p3_label.setStyleSheet("background-image: url(\"images/reverblabel.png\");")
            param3 = QSlider(Qt.Horizontal, self)
            param3.setGeometry(0, 190, 200, 30)
            param3.setStyleSheet("background-image: url(\"images/sliderbg.png\");")
            param3.setMinimum(0)
            param3.setMaximum(2)
            param3.setTickPosition(QSlider.TicksBelow)
            param3.sliderReleased.connect(self.slider_changed)
            self.param_list.append((param3, 1))

        elif name == "distortion":
            label.setStyleSheet("border: 3px solid black;\n"
                               "background-image: url(\"images/distort_node.png\");")
            p1_label = QLabel(self)
            p1_label.setText("Drive")
            p1_label.setGeometry(50, 0, 120, 30)
            p1_label.setStyleSheet("background-image: url(\"images/distortlabel.png\");")
            param1 = QSlider(Qt.Horizontal, self)
            param1.setGeometry(0, 30, 200, 30)
            param1.setStyleSheet("background-image: url(\"images/sliderbg.png\");")
            # Must divide by 100 before passed to function
            param1.setMinimum(0)
            param1.setMaximum(100)
            param1.setValue(75)
            param1.setTickPosition(QSlider.TicksBelow)
            param1.sliderReleased.connect(self.slider_changed)
            self.param_list.append((param1, 100))


            p2_label = QLabel(self)
            p2_label.setText("Slope")
            p2_label.setGeometry(50, 80, 120, 30)
            p2_label.setStyleSheet("background-image: url(\"images/distortlabel.png\");")
            param2 = QSlider(Qt.Horizontal, self)
            param2.setGeometry(0, 110, 200, 30)
            param2.setStyleSheet("background-image: url(\"images/sliderbg.png\");")
            # Must divide by 100 before passed to function
            param2.setMinimum(0)
            param2.setMaximum(100)
            param2.setValue(50)
            param2.setTickPosition(QSlider.TicksBelow)
            param2.sliderReleased.connect(self.slider_changed)
            self.param_list.append((param2, 100))

        elif name == "chorus":
            label.setStyleSheet("border: 3px solid black;\n"
                               "background-image: url(\"images/chorus_node.png\");")
            p1_label = QLabel(self)
            p1_label.setText("Depth")
            p1_label.setGeometry(50, 0, 120, 30)
            p1_label.setStyleSheet("background-image: url(\"images/choruslabel.png\");")
            param1 = QSlider(Qt.Horizontal, self)
            param1.setGeometry(0, 30, 200, 30)
            param1.setStyleSheet("background-image: url(\"images/sliderbg.png\");")
            param1.setMinimum(0)
            param1.setMaximum(5)
            param1.setValue(1)
            param1.setTickPosition(QSlider.TicksBelow)
            param1.sliderReleased.connect(self.slider_changed)
            self.param_list.append((param1, 1))


            p2_label = QLabel(self)
            p2_label.setText("Feedback")
            p2_label.setGeometry(50, 80, 120, 30)
            p2_label.setStyleSheet("background-image: url(\"images/choruslabel.png\");")
            param2 = QSlider(Qt.Horizontal, self)
            param2.setGeometry(0, 110, 200, 30)
            param2.setStyleSheet("background-image: url(\"images/sliderbg.png\");")
            # Must divide by 100 before passed to function
            param2.setMinimum(0)
            param2.setMaximum(100)
            param2.setValue(25)
            param2.setTickPosition(QSlider.TicksBelow)
            param2.sliderReleased.connect(self.slider_changed)
            self.param_list.append((param2, 100))

            p3_label = QLabel(self)
            p3_label.setText("Balance")
            p3_label.setGeometry(50, 160, 120, 30)
            p3_label.setStyleSheet("background-image: url(\"images/choruslabel.png\");")
            param3 = QSlider(Qt.Horizontal, self)
            param3.setGeometry(0, 190, 200, 30)
            param3.setStyleSheet("background-image: url(\"images/sliderbg.png\");")
            # Must divide by 100 before passed to function
            param3.setMinimum(0)
            param3.setMaximum(100)
            param3.setValue(50)
            param3.setTickPosition(QSlider.TicksBelow)
            param3.sliderReleased.connect(self.slider_changed)
            self.param_list.append((param3, 100))

        elif name == "delay":
            label.setStyleSheet("border: 3px solid black;\n"
                               "background-image: url(\"images/delay_node.png\");")
            p1_label = QLabel(self)
            p1_label.setText("Delay")
            p1_label.setGeometry(50, 0, 120, 30)
            p1_label.setStyleSheet("background-image: url(\"images/delaylabel.png\");")
            param1 = QSlider(Qt.Horizontal, self)
            param1.setGeometry(0, 30, 200, 30)
            param1.setStyleSheet("background-image: url(\"images/sliderbg.png\");")
            # Must divide by 100 before passed to function
            param1.setMinimum(0)
            param1.setMaximum(100)
            param1.setValue(25)
            param1.setTickPosition(QSlider.TicksBelow)
            param1.sliderReleased.connect(self.slider_changed)
            self.param_list.append((param1, 100))


            p2_label = QLabel(self)
            p2_label.setText("Feedback")
            p2_label.setGeometry(50, 80, 120, 30)
            p2_label.setStyleSheet("background-image: url(\"images/delaylabel.png\");")
            param2 = QSlider(Qt.Horizontal, self)
            param2.setGeometry(0, 110, 200, 30)
            param2.setStyleSheet("background-image: url(\"images/sliderbg.png\");")
            # Must divide by 100 before passed to function
            param2.setMinimum(0)
            param2.setMaximum(100)
            param2.setValue(0)
            param2.setTickPosition(QSlider.TicksBelow)
            param2.sliderReleased.connect(self.slider_changed)
            self.param_list.append((param2, 100))

            p3_label = QLabel(self)
            p3_label.setText("Max Delay")
            p3_label.setGeometry(50, 160, 120, 30)
            p3_label.setStyleSheet("background-image: url(\"images/delaylabel.png\");")
            param3 = QSlider(Qt.Horizontal, self)
            param3.setGeometry(0, 190, 200, 30)
            param3.setStyleSheet("background-image: url(\"images/sliderbg.png\");")
            # Must divide by 100 before passed to function
            param3.setMinimum(0)
            param3.setMaximum(100)
            param3.setValue(1)
            param3.setTickPosition(QSlider.TicksBelow)
            param3.sliderReleased.connect(self.slider_changed)
            self.param_list.append((param3, 100))

        label.setGeometry(0, 250, 100, 30)
        self.slider_changed()

    def slider_changed(self):
        global slider_list
        slider_vals = []
        for (p, m) in self.param_list:
            slider_vals.append(p.value() / m)
        if len(slider_list) > self.position:
            slider_list.remove(slider_list[self.position]) 
        slider_list.insert(self.position, slider_vals)
        print(slider_list)

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
