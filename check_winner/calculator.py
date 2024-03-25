from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
import math

style = """
    QWidget {
        background-color: rgb(9, 4, 106);
    }
    QLabel {
        background-color: rgb(0, 38, 121);
        color: rgb(215, 227, 234);
        font: bold 75px;
        border: 20px solid rgb(0, 0, 0);
        border-radius: 35px;
    }
    QPushButton {
        background-color: rgb(9, 4, 106);
        color: rgb(215, 227, 234);
        font: bold 25px;
        border: 5px solid black;
        border-radius: 10px;
    }
    QPushButton:hover {
        background-color : rgb(0, 71, 171);
    }
    QPushButton#AC {
        background-color : rgb(5, 213, 255);
    }
    QPushButton#AC:hover {
        background-color : rgb(0, 71, 171);
    }
    QPushButton#EQUAL {
        background-color : rgb(5, 213, 255);
    }
    QPushButton#EQUAL:hover {
        background-color : rgb(0, 71, 171);
    }
    .QPushButton[level="buttons"] {
        background-color : rgb(0, 150, 95);
    }
    .QPushButton[level="buttons"]:hover {
        background-color : rgb(0, 58, 41);
    }
"""

app = QApplication([])
win = QWidget()
win.setWindowTitle("CALCULATOR")
win.resize(700, 600)
win.setStyleSheet(style)

#Creating widgets
label = QLabel("")
label.setAlignment(Qt.AlignCenter)
btn_1 = QPushButton("1")
btn_2 = QPushButton("2")
btn_3 = QPushButton("3")
btn_4 = QPushButton("4")
btn_5 = QPushButton("5")
btn_6 = QPushButton("6")
btn_7 = QPushButton("7")
btn_8 = QPushButton("8")
btn_9 = QPushButton("9")
btn_0 = QPushButton("0")
btn_point = QPushButton(".")
btn_ac = QPushButton("AC")
btn_ac.setObjectName("AC")
btn_delete = QPushButton("◄")
btn_sqrt = QPushButton("√")
btn_x = QPushButton("x")
btn_divide = QPushButton("/")
btn_plus = QPushButton("+")
btn_minus = QPushButton("-")
btn_equal = QPushButton("=")
btn_equal.setObjectName("EQUAL")
btn_squared = QPushButton("^")

btn_delete.setProperty("level", "buttons")
btn_plus.setProperty("level", "buttons")
btn_minus.setProperty("level", "buttons")
btn_divide.setProperty("level", "buttons")
btn_x.setProperty("level", "buttons")
btn_squared.setProperty("level", "buttons")
btn_sqrt.setProperty("level", "buttons")

#Move around widgets

l1 = QHBoxLayout()
l1.addWidget(btn_ac)
l1.addWidget(btn_delete)
l1.addWidget(btn_sqrt)
l1.addWidget(btn_x)

l2 = QHBoxLayout()
l2.addWidget(btn_7)
l2.addWidget(btn_8)
l2.addWidget(btn_9)
l2.addWidget(btn_divide)

l3 = QHBoxLayout()
l3.addWidget(btn_4)
l3.addWidget(btn_5)
l3.addWidget(btn_6)
l3.addWidget(btn_plus)

l4 = QHBoxLayout()
l4.addWidget(btn_1)
l4.addWidget(btn_2)
l4.addWidget(btn_3)
l4.addWidget(btn_minus)

l5 = QHBoxLayout()
l5.addWidget(btn_point)
l5.addWidget(btn_0)
l5.addWidget(btn_squared)
l5.addWidget(btn_equal)


l6 = QVBoxLayout()
l6.addWidget(label)
l6.addLayout(l1)
l6.addLayout(l2)
l6.addLayout(l3)
l6.addLayout(l4)
l6.addLayout(l5)

win.setLayout(l6)

#clicking

def clicker1():
    label.setText(label.text()+"1")


def clicker2():
    label.setText(label.text()+"2")

def clicker3():
    label.setText(label.text()+"3")

def clicker4():
    label.setText(label.text()+"4")

def clicker5():
    label.setText(label.text()+"5")

def clicker6():
    label.setText(label.text()+"6")
   
def clicker7():
    label.setText(label.text()+"7")

def clicker8():
    label.setText(label.text()+"8")

def clicker9():
    label.setText(label.text()+"9")

def clicker0():
    label.setText(label.text()+"0")

def clicker_point():
    label.setText(label.text()+".")

def clicker_plus():
    label.setText(label.text()+" + ")

def clicker_minus():
    label.setText(label.text()+" - ")

def clicker_x():
    label.setText(label.text()+" x ")

def clicker_divide():
    label.setText(label.text()+" / ")

def clicker_sqrt():
    label.setText(label.text()+" √ ")

def clicker_squared():
    label.setText(label.text()+" ^ ")

def clear_all():
    label.setText("0")

def label_minus_add_divide_multiply_sqrt_squared():
    expression = label.text()
    # Check for addition
    if ' + ' in expression:
        numbers = expression.split(' + ')
        total = 0
        for num in numbers:
            total += float(num) 
    # Check for subtraction
    elif ' - ' in expression:
        numbers = expression.split(' - ')
        total = float(numbers[0])
        for num in numbers[1:]:
            total -= float(num)
    # Check for multiplication
    elif ' x ' in expression:
        numbers = expression.split(' x ')
        total = 1
        for num in numbers:
            total *= float(num)
    # Check for division
    elif ' / ' in expression:
        numbers = expression.split(' / ')
        total = float(numbers[0])
        for num in numbers[1:]:
            total /= float(num)
    
    elif ' ^ ' in expression:
        numbers = expression.split(" ^ ")
        total = float(numbers[0])
        for num in numbers[1:]:
            total = total ** float(num)

    elif ' √ ' in expression:
        if len(numbers) > 0:
            numbers = expression.split(' √ ')
            total = float(numbers[0])
            for num in numbers[1:]:
                total = math.sqrt(float(num))
    

    label.setText(str(total))

def delete():
    current_text = label.text()
    if current_text:
        label.setText(current_text[:-1])



    
        
btn_1.clicked.connect(clicker1)
btn_2.clicked.connect(clicker2)
btn_3.clicked.connect(clicker3)
btn_4.clicked.connect(clicker4)
btn_5.clicked.connect(clicker5)
btn_6.clicked.connect(clicker6)
btn_7.clicked.connect(clicker7)
btn_8.clicked.connect(clicker8)
btn_9.clicked.connect(clicker9)
btn_0.clicked.connect(clicker0)
btn_point.clicked.connect(clicker_point)
btn_plus.clicked.connect(clicker_plus)
btn_divide.clicked.connect(clicker_divide)
btn_x.clicked.connect(clicker_x)
btn_minus.clicked.connect(clicker_minus)
btn_sqrt.clicked.connect(clicker_sqrt)
btn_squared.clicked.connect(clicker_squared)
btn_ac.clicked.connect(clear_all)
btn_equal.clicked.connect(label_minus_add_divide_multiply_sqrt_squared)
btn_delete.clicked.connect(delete)

win.show()
app.exec_()
