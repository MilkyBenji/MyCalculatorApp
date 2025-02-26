import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap  # Import for loading the image

class Calculator(QWidget):
  def __init__(self):
        super().__init__()
        self.initUI()
        self.current_expression = ""

  def initUI(self):
        self.setWindowTitle("MyCalculatorApp")
        self.setStyleSheet("background-color: #FFFFFF;")  # White theme

        # Logo Label
        self.logo_label = QLabel(self)
        pixmap = QPixmap("logo.png")  # Load the logo image
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Display Label
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet("""
            font-size: 24px; 
            color: white; 
            background-color: #1E1E1E; 
            padding: 10px; 
            border-radius: 5px;
        """)

        # Create Number Buttons
        self.buttons = {str(i): QPushButton(str(i)) for i in range(10)}
        for button in self.buttons.values():
            button.setStyleSheet("""
                font-size: 20px; 
                background-color: #505050; 
                color: white; 
                border-radius: 5px;
                padding: 10px;
            """)
            button.clicked.connect(self.number_button_clicked)

        # Create Operator Buttons
        self.operators = {"+": "+", "-": "-", "*": "*", "/": "/"}
        self.operator_buttons = {op: QPushButton(op) for op in self.operators}
        for button in self.operator_buttons.values():
            button.setStyleSheet("""
                font-size: 20px; 
                background-color: orange; 
                color: white; 
                border-radius: 5px;
                padding: 10px;
            """)
            button.clicked.connect(self.operator_button_clicked)

        # Create Clear and Equals Button
        self.equals_button = QPushButton("=")
        self.equals_button.setStyleSheet("""
            font-size: 20px; 
            background-color: green; 
            color: white; 
            border-radius: 5px;
            padding: 10px;
        """)
        self.equals_button.clicked.connect(self.calculate)

        self.clear_button = QPushButton("C")
        self.clear_button.setStyleSheet("""
            font-size: 20px; 
            background-color: red; 
            color: white; 
            border-radius: 5px;
            padding: 10px;
        """)
        self.clear_button.clicked.connect(self.clear_display)

        # Layout Setup
        layout = QVBoxLayout()
        layout.addWidget(self.logo_label)  # Add the logo
        layout.addWidget(self.display)

        grid_layout = QGridLayout()
        positions = [(i, j) for i in range(1, 4) for j in range(3)]  # 1-9 buttons
        for pos, num in zip(positions, range(1, 10)):
            grid_layout.addWidget(self.buttons[str(num)], *pos)

        grid_layout.addWidget(self.buttons["0"], 4, 1)  # Place '0' at bottom center

        # Place operator buttons
        for i, (op, btn) in enumerate(self.operator_buttons.items()):
            grid_layout.addWidget(btn, i + 1, 3)

        # Special buttons
        grid_layout.addWidget(self.clear_button, 4, 0)
        grid_layout.addWidget(self.equals_button, 4, 2)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

  def number_button_clicked(self):
    sender = self.sender()
    
    # Change button style for a brief moment
    original_style = sender.styleSheet()
    sender.setStyleSheet(original_style + "background-color: white; color: black;")
    
    QTimer.singleShot(150, lambda: sender.setStyleSheet(original_style))  # Revert after 150ms

    if self.display.text() == "0":
        self.current_expression = sender.text()
    else:
        self.current_expression += sender.text()
    self.display.setText(self.current_expression)

  def operator_button_clicked(self):
    sender = self.sender()

    # Change button style for a brief moment
    original_style = sender.styleSheet()
    sender.setStyleSheet(original_style + "background-color: white; color: black;")
    
    QTimer.singleShot(100, lambda: sender.setStyleSheet(original_style))  # Revert after 150ms

    if self.current_expression and self.current_expression[-1] not in "+-*/":
        self.current_expression += sender.text()
    self.display.setText(self.current_expression)

  def calculate(self):
    sender = self.equals_button
    original_style = sender.styleSheet()
    sender.setStyleSheet(original_style + "background-color: white; color: black;")
    QTimer.singleShot(100, lambda: sender.setStyleSheet(original_style))  # Revert after 150ms

    try:
        result = str(eval(self.current_expression))
        self.display.setText(result)
        self.current_expression = result
    except Exception:
        self.display.setText("Error")
        self.current_expression = ""

  def calculate(self):
    sender = self.equals_button
    original_style = sender.styleSheet()
    sender.setStyleSheet(original_style + "background-color: white; color: black;")
    QTimer.singleShot(100, lambda: sender.setStyleSheet(original_style))  # Revert after 150ms

    try:
        result = str(eval(self.current_expression))
        self.display.setText(result)
        self.current_expression = result
    except Exception:
        self.display.setText("Error")
        self.current_expression = ""

  def clear_display(self):
    sender = self.clear_button
    original_style = sender.styleSheet()
    sender.setStyleSheet(original_style + "background-color: white; color: black;")
    QTimer.singleShot(100, lambda: sender.setStyleSheet(original_style))  # Revert after 150ms

    self.current_expression = ""
    self.display.setText("0")

# Run the Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
