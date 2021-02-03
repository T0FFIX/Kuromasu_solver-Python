from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class App(QWidget):

    def __init__(self, cleanBoard, correctBoard, width, height):
        super().__init__()
        self.cleanBoard = cleanBoard
        self.correctBoard = correctBoard
        self.left = 300
        self.top = 200
        self.width = width
        self.height = height
        self.width_of_screen = width*100
        self.height_of_screen = height*100
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Kuromasu")
        self.setGeometry(self.left, self.top, self.width_of_screen, self.height_of_screen)

        for i in range(self.height):
            for j in range(self.width):
                n = self.width * i + j
                if  self.correctBoard[n] == 0:
                    button = QPushButton('', self)
                    button.setStyleSheet("background-color : white")
                elif self.correctBoard[n] == 1:
                    button = QPushButton('', self)
                    button.setStyleSheet("background-color : black")
                else:
                    button = QPushButton(str(self.correctBoard[n]), self)
                    button.setStyleSheet("background-color : white")
                button.setFont(QFont('Times', 20))
                button.resize(100, 100)
                button.move(0+(j*100), 0+(i*100))

        self.show()


def print_visuals(cleanBoard, correctBoard, width, height):
    app = QApplication(sys.argv)
    ex = App(cleanBoard, correctBoard, width, height)
    sys.exit(app.exec_())


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())