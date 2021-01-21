# coding=utf-8

from chess.chess_piece import ChessPiece
from chess.images import Red_Pawn, BLACK_Pawn


class Pawn(ChessPiece):
    """
    兵类
    """
    @property
    def image(self):
        """
        获取棋子图像
        """
        if self._is_red:
            return Red_Pawn
        else:
            return BLACK_Pawn

    def get_moves(self, pieces: dict):
        """
        获取所有能移动的位置
        """
        # 北方棋子只能南下, 南方兵只能北上

        can_trun_right = False
        dy = 1

        if self.is_north:
            # 过河的兵才能左右走
            dy = -1
            can_trun_right = self._y < 5
        else:
            dy = 1
            can_trun_right = self._y > 4

        locs = [(self._x, self._y + dy)]
        if can_trun_right:
            locs.append((self._x - 1, self._y))
            locs.append((self._x + 1, self._y))

        moves = []
        for x, y in locs:
            if self.can_move(pieces, x - self._x, y - self._y):
                moves.append((x, y))
        return moves
