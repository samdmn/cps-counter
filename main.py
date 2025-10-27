import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QCursor, QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self):

        # CONSTRUCTOR
        super().__init__()
        
        # VARIABLES
        self.times_clicked = 0
        self.seconds = 0
        self.cps = 0
        self.seconds_limit = 5

        # MAIN WINDOW
        self.setGeometry(0, 0, 500, 500)
        self.setFixedSize(500, 500)
        self.setWindowTitle("CPS Counter")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setCursor(QCursor(Qt.ArrowCursor))
        self.setStyleSheet("color: #000000; background-color: #ffffff;")

        # CLICK IMAGE
        self.title_image = QLabel(self)
        self.title_image.setGeometry(0, 0, 100, 100)
        self.title_image.setStyleSheet("background-color: #f5f5f5;")
        self.title_image.setPixmap(QPixmap("icon.ico"))
        self.title_image.setScaledContents(True)

        # TITLE
        self.titre = QLabel("CPS Counter", self)
        self.titre.setFont(QFont("Arial", 40))
        self.titre.setGeometry(100, 0, 400, 100)
        self.titre.setStyleSheet("color: #1f1f1f; background-color: #f5f5f5;")
        self.titre.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # BUTTON
        self.button = QPushButton("Start and click fast !", self)
        self.button.setGeometry(0, 100, 500, 100)
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button.setStyleSheet("""
            QPushButton {
                color: #e6304a;
                background-color: #ffffff;
                border: 2px solid #e6304a;
                border-radius: 10px;
                font-size: 20px;
                
            }
            QPushButton:pressed {
                color: #ffffff;
                background-color: #e6304a;
                border-radius: 10px;
                border: 2px solid #e6304a;
            }
        """)
        self.button.clicked.connect(self.on_click)

        # TIMER LABEL
        self.timer_label = QLabel("Timer : 0 s", self)
        self.timer_label.setFont(QFont("Arial", 20))
        self.timer_label.setGeometry(0, 220, 500, 50)
        self.timer_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # TIMER
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer_and_cps)
        self.cps_label = QLabel("0 CPS", self)
        self.cps_label.setFont(QFont("Arial", 20))
        self.cps_label.setGeometry(0, 280, 500, 50)
        self.cps_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # RETRY
        self.retry_button = QPushButton("Retry", self)
        self.retry_button.setGeometry(0, 400, 500, 100)
        self.retry_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.retry_button.setStyleSheet("""
            QPushButton {
                color: #e6304a;
                background-color: #ffffff;
                border: 2px solid #e6304a;
                border-radius: 10px;
                font-size: 20px;
                
            }
            QPushButton:pressed {
                color: #ffffff;
                background-color: #e6304a;
                border-radius: 10px;
                border: 2px solid #e6304a;
            }
        """)
        self.retry_button.clicked.connect(self.retry)

    def on_click(self):
        if self.times_clicked == 0:
            self.timer.start(1000)
        self.times_clicked += 1

    def update_timer_and_cps(self):
        self.seconds += 1
        self.cps = self.times_clicked/self.seconds
        self.timer_label.setText(f"Timer : {self.seconds} s")
        self.cps_label.setText(f"{round(self.cps, 4)} CPS")
        if self.seconds == self.seconds_limit:
            self.timer.stop()
            self.show_results()
            return

    def show_results(self):
        self.results = QLabel(f"You are {round(self.cps, 2)} CPS fast ! {self.commentary()}", self)
        self.results.setFont(QFont("Arial", 20))
        self.results.setGeometry(0, 220, 500, 100)
        self.results.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.results.setWordWrap(True)
        self.results.show()
        self.cps_label.hide()
        self.timer_label.hide()

    def retry(self):
        self.timer.stop()
        self.times_clicked = 0
        self.seconds = 0
        self.cps = 0
        if hasattr(self, "results") and self.results is not None:
            self.results.hide()
        self.timer_label.setText("Timer : 0 s")
        self.cps_label.setText("0 CPS")
        self.timer_label.show()
        self.cps_label.show()

    def commentary(self):
        if self.cps < 7:
            return "It's very bad, to be honest..."
        elif self.cps >= 7 and self.cps < 10 :
            return "It's good, but I'm sure you can do better !"
        else :
            return "Great job !"
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
