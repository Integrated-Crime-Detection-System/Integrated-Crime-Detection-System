from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi('ui/login_window.ui', self)

        self.register_button.clicked.connect(self.go_to_register_page)
        self.login_button.clicked.connect(self.open_settings_window)

        self.show()

    def go_to_register_page(self):
        print("go_to_register_page")

    def open_settings_window(self):
        print("open_settings_window")

