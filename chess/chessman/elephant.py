# coding=utf-8

from chess.chess_piece import ChessPiece
from chess.images import Red_Elephant, BLACK_Elephant


class Elephant(ChessPiece):
    """
    象类
    """
    @property
    def image(self):
        """
        获取棋子图像
        """
        if self._is_red:
            return Red_Elephant
        else:
            return BLACK_Elephant

    def get_moves(self, pieces: dict):
        locs = [
            (+2, - 2),
            (+2, + 2),
            (-2, + 2),
            (-2, - 2),
        ]
        blocks = [
            (self._x + 1, self._y + 1),
            (self._x + 1, self._y - 1),
            (self._x - 1, self._y + 1),
            (self._x - 1, self._y - 1),
        ]

        moves = []
        for i in range(len(blocks)):
            dx, dy = locs[i][0], locs[i][1]

            # 象不能过河
            if self.is_north:
                if (self._y + dy) < 5:
                    continue
            else:
                if (self._y + dy) > 4:
                    continue

            # print(dx, dy)
            # print(blocks[i])
            # 可以移动且不卡像腿
            if self.can_move(pieces, dx, dy) and blocks[i] not in pieces:
                moves.append((self._x + dx, self._y + dy))

        return moves
