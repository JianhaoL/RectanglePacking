import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from test1 import result, Window

class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'I. SAŁUCH, J. LUO'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()
        self.boolval = True

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createHorizontalLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox1)
        windowLayout.addWidget(self.horizontalGroupBox2)
        self.setLayout(windowLayout)

        self.show()

    def createHorizontalLayout(self):
        self.horizontalGroupBox1 = QGroupBox()
        self.horizontalGroupBox2 = QGroupBox()
        layout1 = QHBoxLayout()

        browse_label = QLabel('Select input file')
        layout1.addWidget(browse_label)
        browse_button = QPushButton('Browse', self)
        browse_button.clicked.connect(self.on_click)
        layout1.addWidget(browse_button)

        self.horizontalGroupBox1.setLayout(layout1)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            return fileName

    @pyqtSlot()
    def on_click(self):
        out_list, root_cordi, block_list_cordi, result_string = result(self.openFileNameDialog())
        dialog = Window(out_list, root_cordi, block_list_cordi, self)
        dialog.show()

        if self.boolval:
            layout2 = QHBoxLayout()
            self.results_label = QLabel()
            layout2.addWidget(self.results_label)
            self.horizontalGroupBox2.setLayout(layout2)
            self.boolval = False

        self.results_label.setText(result_string)
        print(result_string)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
