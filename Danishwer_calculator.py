#Welocome to Danishwer Calculator, this is a scientific calculator which I have coded with library PySide6

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QKeySequence
import math

class ScientificCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # window 
        self.setWindowTitle('Danishwer Scientific Calculator')
        self.setGeometry(100, 100, 380, 500)

        # Central 
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layouts
        self.layout = QVBoxLayout(self.central_widget)
        self.buttons_layout = QGridLayout()

        # Display settings
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)
        self.display.setFont(QFont('Arial', 18))
        self.display.setStyleSheet("background-color: #f0f0f0; color: #333; border: 1px solid #ccc; border-radius: 5px;")
        self.layout.addWidget(self.display)

        # Add button layout
        self.layout.addLayout(self.buttons_layout)

        # Create both basic and scientific buttons
        self.create_basic_buttons()
        self.create_scientific_buttons()

        # Keyboard support
        self.setFocusPolicy(Qt.StrongFocus)

    def create_basic_buttons(self):
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('(', 4, 0), (')', 4, 1), ('clear', 4, 2)
        ]

        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.setFixedSize(70, 50)
            button.setFont(QFont('Arial', 14))
            button.setStyleSheet("""
                QPushButton {
                    background-color: #e0e0e0; 
                    border-radius: 5px;
                    border: 1px solid #999;
                }
                QPushButton:hover {
                    background-color: #d6d6d6;
                }
                QPushButton:pressed {
                    background-color: #cccccc;
                }
            """)
            self.buttons_layout.addWidget(button, row, col)
            button.clicked.connect(lambda checked, btn=text: self.on_button_click(btn))

    def create_scientific_buttons(self):
        scientific_buttons = [
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3),
            ('ln', 6, 0), ('^', 6, 1), ('√', 6, 2), ('x²', 6, 3),
            ('π', 7, 0), ('e', 7, 1), ('!', 7, 2), ('%', 7, 3)
        ]

        for (text, row, col) in scientific_buttons:
            button = QPushButton(text)
            button.setFixedSize(70, 50)
            button.setFont(QFont('Arial', 14))
            button.setStyleSheet("""
                QPushButton {
                    background-color: #e0e0e0; 
                    border-radius: 5px;
                    border: 1px solid #999;
                }
                QPushButton:hover {
                    background-color: #d6d6d6;
                }
                QPushButton:pressed {
                    background-color: #cccccc;
                }
            """)
            self.buttons_layout.addWidget(button, row, col)
            button.clicked.connect(lambda checked, btn=text: self.on_button_click(btn))

    def on_button_click(self, button_text):
        if button_text == '=':
            self.evaluate_expression()
        elif button_text == 'clear':
            self.display.clear()
        elif button_text == '√':
            self.calculate_sqrt()
        elif button_text == 'x²':
            self.calculate_square()
        elif button_text == 'sin':
            self.calculate_trig(math.sin)
        elif button_text == 'cos':
            self.calculate_trig(math.cos)
        elif button_text == 'tan':
            self.calculate_trig(math.tan)
        elif button_text == 'log':
            self.calculate_log(math.log10)
        elif button_text == 'ln':
            self.calculate_log(math.log)
        elif button_text == '^':
            self.display.setText(self.display.text() + '**')
        elif button_text == 'π':
            self.display.setText(self.display.text() + str(math.pi))
        elif button_text == 'e':
            self.display.setText(self.display.text() + str(math.e))
        elif button_text == '!':
            self.calculate_factorial()
        elif button_text == '%':
            self.calculate_percentage()
        else:
            self.display.setText(self.display.text() + button_text)

    def evaluate_expression(self):
        try:
            expression = self.display.text()
            result = eval(expression)
            self.display.setText(str(result))
        except Exception:
            self.display.setText('Error')

    def calculate_sqrt(self):
        try:
            value = float(self.display.text())
            result = math.sqrt(value)
            self.display.setText(str(result))
        except Exception:
            self.display.setText('Error')

    def calculate_square(self):
        try:
            value = float(self.display.text())
            result = math.pow(value, 2)
            self.display.setText(str(result))
        except Exception:
            self.display.setText('Error')

    def calculate_trig(self, func):
        try:
            value = float(self.display.text())
            result = func(math.radians(value))  # Converts degrees to radians
            self.display.setText(str(result))
        except Exception:
            self.display.setText('Error')

    def calculate_log(self, func):
        try:
            value = float(self.display.text())
            result = func(value)
            self.display.setText(str(result))
        except Exception:
            self.display.setText('Error')

    def calculate_factorial(self):
        try:
            value = int(self.display.text())
            result = math.factorial(value)
            self.display.setText(str(result))
        except Exception:
            self.display.setText('Error')

    def calculate_percentage(self):
        try:
            value = float(self.display.text())
            result = value / 100
            self.display.setText(str(result))
        except Exception:
            self.display.setText('Error')

    # Keyboard input support
    def keyPressEvent(self, event):
        if event.matches(QKeySequence.InsertParagraphSeparator):
            self.evaluate_expression()
        elif event.key() == Qt.Key_Backspace:
            self.display.setText(self.display.text()[:-1])
        else:
            key_value = event.text()
            if key_value in '0123456789+-*/().':
                self.display.setText(self.display.text() + key_value)
            elif key_value == '=':
                self.evaluate_expression()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = ScientificCalculator()
    calculator.show()
    sys.exit(app.exec())
