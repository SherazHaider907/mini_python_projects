import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Digital Clock")
        self.setGeometry(100, 100, 300, 150)  # x, y, width, height

        # Layout
        layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 40px; color: blue;")
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Timer
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)  # update every 1 second

        self.update_time()  # initialize the time display

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())