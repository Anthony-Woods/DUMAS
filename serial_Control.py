from PyQt5 import QtWidgets
from ui import Ui_MainWindow
import sys

class RunGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(RunGUI, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)

    window = RunGUI()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
