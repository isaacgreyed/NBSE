from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from EffectTree_examples import *


class MainStage(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainStage, self).__init__(*args, **kwargs)

        self.height = 500#canvas_y
        self.width = 500#canvas_x

        self.setFixedSize(QSize(self.height, self.width))

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.setFixedSize(250, 250)

        w = QVBoxLayout()
        w.addLayout(self.grid)

        self.setLayout(w)

        self.import_grid(eff.get_as_2d())
        self.show()

    def import_grid(self, grid):
        for j in range(0, len(grid)):
            for i in range(0, len(grid[j])):
                if grid[j][i]:
                    n = Node()
                    self.grid.addWidget(n, i, j)

    


class Node(QWidget):
    def __init__(self, *args, **kwargs):
        super(Node, self).__init__(*args, **kwargs)

        self.setFixedSize(QSize(5, 5))

    def paintEvent(self, event) -> None:
        painter = QPainter()
        painter.begin(self)
        rect    = event.rect()
        
        painter.fillRect(rect, QBrush(Qt.black))

        #pen = QPen(Qt.red)
        #pen.setWidth(2)
        #painter.setPen(pen)
        #painter.drawRect(rect)
        #painter.end()
        



def render(effect_tree, canvas_x, canvas_y):
    array = effect_tree.get_as_2d
    i = 0
    for x in array:
        j = 0
        for y in x:
            #draw(y, i, j, canvas_x, canvas_y)
            j += 1
        i += 1