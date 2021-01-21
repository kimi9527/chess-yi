# coding=utf-8

from chess.chess_piece import ChessPiece
from chess.images import Red_ROOK, BLACK_ROOK

MAX_X = 8
MAX_Y = 9


class Rook(ChessPiece):
    """
    車类
    """
    @property
    def image(self):
        """
        获取棋子图像
        """
        if self._is_red:
            return Red_ROOK
        else:
            return BLACK_ROOK

    def get_moves(self, pieces: dict):
        moves = []

        for x in range(MAX_X + 1):
            dx = x - self._x
            if self.can_move(pieces, dx, 0):
                if self.counts(pieces, dx, 0) == 0:
                    moves.append((x, self._y))

        for y in range(MAX_Y + 1):
            dy = y - self._y
            if self.can_move(pieces, 0, dy):
                if self.counts(pieces, 0, dy) == 0:
                    moves.append((self._x, y))
        return moves
