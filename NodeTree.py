from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys


class Node:

    def __init__(self, x, y, width, height):
        self.down = None
        self.right = None
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.used = False

    def fit(self, blocks):
        for block in blocks:
            node = self.findNode(block.w, block.h)
            if node:
                block.fit = node.splitNode(block.w, block.h)

    def findNode(self, w, h):
        if self.used:
            return self.right.findNode(w, h) or self.down.findNode(w, h)
        elif self.width >= w and self.height >= h:
            return self
        else:
            return 0

    def splitNode(self, w, h):
        self.used = True
        self.right = Node(self.x + w, self.y, self.width - w, h)
        self.down = Node(self.x, self.y + h, self.width, self.height - h)
        return self

    def printNode(self):
        if self.right is not None:
            self.right.printNode()
        print(self.x, self.y, self.width, self.height)
        if self.down is not None:
            self.down.printNode()


class Block:
    def __init__(self, width, height, value):
        self.w = width
        self.h = height
        self.value = value
        self.fit = None

    def __str__(self):
        if self.fit is not None:
            return str(self.w) + "," + str(self.h) + "," + str(self.value)
        return str(self.w) + "," + str(self.h)


def getValueBlocks(block_list, out_list):
    out_list.clear()
    S = 0
    for block in block_list:
        if not block.fit is None:
            out_list.append((block.fit.x, block.fit.y, block.w, block.h))
            S += block.value
    return S
