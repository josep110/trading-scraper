import interface, sys
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = interface.TS_Interface()
    sys.exit(app.exec_())