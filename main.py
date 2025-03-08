import sys
from PyQt5.QtWidgets import QApplication
from app_ui import EncryptionApp

def main():
    app = QApplication(sys.argv)
    window = EncryptionApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()