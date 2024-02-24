from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import randint

app = QApplication([])
win = QWidget()
win.resize(400, 400)
win.setWindowTitle("Check winner")

#Creating widgets
text_1 = QLabel("Click to find out the  winner.")
text_2 = QLabel("?")
click_1 = QPushButton("Generate")

#Move around widgets
y_axis = QVBoxLayout()
y_axis.addWidget(text_1, alignment= Qt.AlignCenter )
y_axis.addWidget(text_2, alignment= Qt.AlignCenter)
y_axis.addWidget(click_1, alignment= Qt.AlignCenter)
win.setLayout(y_axis)

#Main
def clicker():
    text_1.setText("Winner!!!!")
    rand_num = randint(1, 100)
    text_2.setText(str(rand_num))    

click_1.clicked.connect(clicker)

win.show()
app.exec_()