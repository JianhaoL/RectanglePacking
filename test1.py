from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from NodeTree import Node
from NodeTree import Block
from ReadFile import FileReader
from NodeTree import getValueBlocks
import sys
import itertools


def get_block_list_from_permutations(permutations):
    block_list_permutations = []
    for permutation in permutations:
        block_list = []
        for rec in permutation:
            b = Block(rec[0], rec[1], rec[2])
            block_list.append(b)
        block_list_permutations.append(block_list)
    return block_list_permutations


def get_max_value_permutation(root_cordi, block_list_permutations):
    value_max = 0
    out_list = []
    for block_list_t in block_list_permutations:
        root = Node(root_cordi[0], root_cordi[1], root_cordi[2], root_cordi[3])
        root.fit(block_list_t)
        out_list_t = []
        value = getValueBlocks(block_list_t, out_list_t)
        if value > value_max:
            out_list = out_list_t
            value_max = value
    return value_max, out_list


class Window(QMainWindow):

    def __init__(self, blocks, root):
        super().__init__()
        self.title = "Jianhao Luo, Igor Saluch"
        self.top = 150
        self.left = 150
        self.width = 1800
        self.height = 1500
        self.blocks = blocks
        self.root = root
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(p)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.drawRect(root_cordi[0], root_cordi[1], root_cordi[2], root_cordi[3])
        PADDING = 40
        i = 0
        for block in self.blocks:
            painter.setPen(QPen(Qt.green, 5, Qt.SolidLine))
            painter.drawRect(block[0], block[1], block[2], block[3])
            print(block)
            painter.setPen(QPen(Qt.white, 5, Qt.SolidLine))
            i += PADDING
            painter.drawRect(
                block[0] + i,
                block[1] + root_cordi[0] + root_cordi[3] + i,
                block[2],
                block[3],
            )


App = QApplication(sys.argv)
fr = FileReader("Samples.txt")
block_list_cordi = fr.get_block_cordi_list()
permutations_blocks_cordi = list(itertools.permutations(block_list_cordi))
block_list_permutations = get_block_list_from_permutations(permutations_blocks_cordi)
root_cordi = fr.get_node()
value_max, out_list = get_max_value_permutation(root_cordi, block_list_permutations)
window = Window(out_list, root_cordi)
print(value_max)
sys.exit(App.exec())
