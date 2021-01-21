# coding=utf-8

import pygame
from sys import exit

from chess.images import BACKROUND, SELECTED

MAX_X = 8  # 0-8
MAX_Y = 9  # 0-9


class ChessView(object):
    """
    棋盘显示
    """
    @staticmethod
    def Pixel2XY(pixel_x, pixel_y):
        '''
        界面像素到棋局坐标变化
        '''
        x = (pixel_x - 5) // 40
        y = (pixel_y - 5) // 40
        if x < 0:
            x = 0
        if x > MAX_X:
            x = MAX_X
        if y < 0:
            y = 0
        if y > MAX_Y:
            y = MAX_Y
        return x, MAX_Y - y

    @staticmethod
    def XY2ixel(x, y):
        """
        棋局坐标到像素变化
        """
        x = x * 40 + 5
        y = (MAX_Y - y) * 40 + 5
        return x, y

    def __init__(self):
        # init pygame
        pygame.init()
        # 设置屏幕分辨率 set display
        self._screen = pygame.display.set_mode((377, 417))
        # 设置标题 set caption
        self.set_title("chess yi")
        # pygame.display.set_caption("chess yi")

    def set_title(self, title: str):
        """
        设置标题
        """
        if(title == '' or title is None):
            return
        pygame.display.set_caption(title)

    def redraw(self):
        """
        刷新界面
        """
        # 设置背景图片 set background image
        self._screen.blit(BACKROUND, [0, 0])

    def show_images(self, images: dict):
        if images is None:
            return
        for x, y in images:
            self._screen.blit(images[(x, y)], self.XY2ixel(x, y))

    def show_hints(self, positions: []):
        if positions is None:
            return
        for x, y in positions:
            self._screen.blit(SELECTED, self.XY2ixel(x, y))

    def update(self):
        """
        更新显示
        """
        pygame.display.update()

    def exit(parameter_list):
        """
        quit game view
        """
        exit()
