#!/usr/bin/env python3
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, QRect
from NodeTree import Node
from NodeTree import Block
from ReadFile import FileReader
from NodeTree import getValueBlocks
import sys
import itertools
import time



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
    block_list = []
    for block_list_t in block_list_permutations:
        root = Node(root_cordi[0], root_cordi[1], root_cordi[2], root_cordi[3])
        root.fit(block_list_t)
        out_list_t = []
        value = getValueBlocks(block_list_t, out_list_t)
        if value > value_max:
            out_list = out_list_t
            value_max = value
            block_list = block_list_t
    return value_max, out_list, block_list


class Window(QMainWindow):

    def __init__(self, blocks, root, block_list, parent=None):
        super(Window, self).__init__(parent)
        self.top = 150
        self.left = 150
        self.width = 1800
        self.height = 1500
        self.blocks = blocks
        self.block_list = block_list
        self.root = root
        self.setGeometry(self.top, self.left, self.width, self.height)

    def paintEvent(self, event):
        scale = 5
        painter = QPainter(self)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(p)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.drawRect(self.root[0]*scale, self.root[1]*scale, self.root[2]*scale, self.root[3]*scale)
        PADDING = 20
        ipx = PADDING
        ipy = self.root[3]*scale + PADDING

        for block in self.blocks:
            painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
            painter.drawRect(block[0]*scale, block[1]*scale, block[2]*scale, block[3]*scale)
        for block in self.block_list:
            painter.setPen(QPen(Qt.white, 2, Qt.SolidLine))
            ix = ipx
            iy = ipy
            iw = block.w*scale
            ih = block.h*scale
            ipx += PADDING + iw
            if ipx > 800:
                ipy += self.root[3]*scale + PADDING
                ipx = PADDING
            if block.fit is not None:
                painter.fillRect(
                    ix, iy, iw, ih, Qt.green
                )
            else:
                painter.drawRect(
                    ix, iy, iw, ih,
                )
            painter.drawText(QRect(ix, iy, iw, ih), Qt.AlignCenter, str(block.value))


def result(input_file, benchmark_mode=-1):
    fr = FileReader(input_file)
    block_list_cordi = fr.get_block_cordi_list()
    if benchmark_mode > 0:
        randlist = list(itertools.permutations(block_list_cordi, benchmark_mode))
        block_list_cordi = randlist[randint(0, len(randlist) - 1)]

    blocks_count = len(block_list_cordi)

    start_time = time.time()
    permutations_blocks_cordi = list(itertools.permutations(block_list_cordi))
    block_list_permutations = get_block_list_from_permutations(permutations_blocks_cordi)
    root_cordi = fr.get_node()
    value_max, out_list, block_list = get_max_value_permutation(root_cordi, block_list_permutations)
    time_elapsed = time.time() - start_time

    return out_list, root_cordi, block_list, f'BLOCKS COUNT: {blocks_count}  TIME ELAPSED: {time_elapsed}  SCORE: {str(value_max)}'
