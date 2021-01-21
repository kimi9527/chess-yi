# coding=utf-8

from chess.chess_piece import ChessPiece
from chess.images import Red_Knight, BLACK_Knight


class Knight(ChessPiece):
    """
    马类
    """
    @property
    def image(self):
        """
        获取棋子图像
        """
        if self._is_red:
            return Red_Knight
        else:
            return BLACK_Knight

    def get_moves(self, pieces: dict):
        """
        获取能移动的位置
        """
        # 不考虑卡马腿，马只能蹦跶八个位置
        pre_moves = [
            (+1, +2),
            (+1, -2),
            (-1, +2),
            (-1, -2),
            (+2, +1),
            (+2, -1),
            (-2, +1),
            (-2, -1)
            ]
        # 卡马腿位置
        blocks = [
            (self._x, self._y+1),
            (self._x, self._y-1),
            (self._x, self._y+1),
            (self._x, self._y+1),
            (self._x+1, self._y),
            (self._x+1, self._y),
            (self._x-1, self._y),
            (self._x-1, self._y)
        ]

        moves = []
        for i in range(len(blocks)):
            dx = pre_moves[i][0]
            dy = pre_moves[i][1]
            if blocks[i] not in pieces and self.can_move(pieces, dx, dy):
                moves.append((self._x + dx, self._y + dy))
        return moves
