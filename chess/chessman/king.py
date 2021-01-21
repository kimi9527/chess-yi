# coding=utf-8

from chess.chess_piece import ChessPiece
from chess.images import Red_King, BLACK_King


class King(ChessPiece):
    """
    将类
    """
    @property
    def image(self):
        """
        获取棋子图像
        """
        if self._is_red:
            return Red_King
        else:
            return BLACK_King

    def get_moves(self, pieces: dict):
        locs = []
        if self.is_north:
            row_min = 7
            row_max = 10
        else:
            row_min = 0
            row_max = 3

        for x in range(3, 6):
            for y in range(row_min, row_max):
                locs.append((x, y))

        res = []
        for (x, y) in locs:
            dx = x - self._x
            dy = y - self._y
            # print(dx, dy)
            if abs(dx) + abs(dy) != 1:
                continue
            if self.can_move(pieces, dx, dy):
                res.append((x, y))

        return res
