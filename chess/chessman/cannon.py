# coding=utf-8

from chess.chess_piece import ChessPiece
from chess.images import Red_Cannon, BLACK_Cannon

MAX_X = 8  # 0-8
MAX_Y = 9  # 0-9


class Cannon(ChessPiece):
    """
    炮类
    """
    @property
    def image(self):
        """
        获取棋子图像
        """
        if self._is_red:
            return Red_Cannon
        else:
            return BLACK_Cannon

    def get_moves(self, pieces: dict):
        moves = []

        # 炮只能横竖-隔山打牛
        for x in range(MAX_X + 1):
            dx = x - self._x
            if self.can_move(pieces, dx, 0):
                cnt = self.counts(pieces, dx, 0)
                # 不隔山打牛不能吃子
                if cnt == 0 and (x, self._y) not in pieces:
                    moves.append((x, self._y))
                # 隔山打牛必须吃子
                elif cnt == 1 and (x, self._y) in pieces:
                    moves.append((x, self._y))

        for y in range(MAX_Y + 1):
            dy = y - self._y
            if self.can_move(pieces, 0, dy):
                cnt = self.counts(pieces, 0, dy)
                # 不隔山打牛不能吃子
                if cnt == 0 and (self._x, y) not in pieces:
                    moves.append((self._x, y))
                # 隔山打牛必须吃子
                elif cnt == 1 and (self._x, y) in pieces:
                    moves.append((self._x, y))
        return moves
