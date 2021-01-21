# coding=utf-8

from chess.chess_piece import ChessPiece
from chess.images import Red_Mandarin, BLACK_Mandarin


class Mandarin(ChessPiece):
    """
    士类
    """
    @property
    def image(self):
        """
        获取棋子图像
        """
        if self._is_red:
            return Red_Mandarin
        else:
            return BLACK_Mandarin

    def get_moves(self, pieces: dict):
        """
        获取所有能移动的位置
        """
        if self.is_north:
            locs = [
                (3, 9),
                (5, 9),
                (3, 7),
                (5, 7),
                (4, 8)
            ]
        else:
            locs = [
                (3, 0),
                (5, 0),
                (3, 2),
                (5, 2),
                (4, 1)
            ]
        moves = []
        for x, y in locs:
            dx, dy = x - self._x, y - self._y
            if abs(dx) == 1 and abs(dy) == 1 and self.can_move(pieces, dx, dy):
                moves.append((x, y))
        return moves
