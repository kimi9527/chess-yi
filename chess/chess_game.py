# coding=utf-8

import pygame

from chess.chess_board import ChessBoard
from chess.chess_view import ChessView


class ChessGame(object):
    """
    chess game
    """

    def __init__(self):
        self._board = None
        self._viewer = None
        self.init()

    def init(self):
        self._board = ChessBoard(True)
        self._viewer = ChessView()

        self.update()

    def update(self):
        """
        更新棋盘
        """
        self._viewer.redraw()
        self._viewer.show_images(self._board.images)
        self._viewer.show_hints(self._board.can_moves)
        self._viewer.update()

    def select(self, x: int, y: int):
        self._board.select(x, y)
