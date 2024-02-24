from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QMessageBox

app = QApplication([])
win = QWidget()
win.resize(550, 400)
win.setWindowTitle("Questions")

# Label
lb_q = QLabel("What is 10 + 10.")
rbuton_1 = QRadioButton("40")
rbuton_2 = QRadioButton("30")
rbuton_3 = QRadioButton("20")
rbuton_4 = QRadioButton("10")

#Move around
line_1 = QHBoxLayout()
line_2 = QHBoxLayout()
line_3 = QHBoxLayout()
line_1.addWidget(lb_q, alignment=Qt.AlignCenter)
line_2.addWidget(rbuton_1, alignment=Qt.AlignCenter)
line_2.addWidget(rbuton_3, alignment=Qt.AlignCenter)
line_3.addWidget(rbuton_2, alignment=Qt.AlignCenter)
line_3.addWidget(rbuton_4, alignment=Qt.AlignCenter)
line_4 = QVBoxLayout()
line_4.addLayout(line_1)
line_4.addLayout(line_2)
line_4.addLayout(line_3)
win.setLayout(line_4)

#Clicker
def correct_awnser():
    new_win = QMessageBox()
    new_win.setText("Correct")
    new_win.exec_()

def incorrect_anwser():
    new_win2 = QMessageBox()
    new_win2.setText("Incorrect")
    new_win2.exec_()

rbuton_1.clicked.connect(incorrect_anwser)
rbuton_2.clicked.connect(incorrect_anwser)
rbuton_4.clicked.connect(incorrect_anwser)
rbuton_3.clicked.connect(correct_awnser)

win.show()
app.exec_()