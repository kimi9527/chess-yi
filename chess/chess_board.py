# coding=utf-8

from chess.chessman.cannon import Cannon
from chess.chessman.elephant import Elephant
from chess.chessman.king import King
from chess.chessman.knight import Knight
from chess.chessman.mandarin import Mandarin
from chess.chessman.pawn import Pawn
from chess.chessman.rook import Rook


class ChessBoard:
    def __init__(self, is_red_first):
        self._pieces = dict()
        self._selected_piece = None
        self._moves = []
        # True代表红色方， False代表黑色方
        self._current_play = is_red_first

        self._pieces[(0, 0)] = Rook(0, 0, True, False)
        self._pieces[(8, 0)] = Rook(8, 0, True, False)
        self._pieces[(1, 0)] = Knight(1, 0, True, False)
        self._pieces[(7, 0)] = Knight(7, 0, True, False)
        self._pieces[(2, 0)] = Elephant(2, 0, True, False)
        self._pieces[(6, 0)] = Elephant(6, 0, True, False)
        self._pieces[(3, 0)] = Mandarin(3, 0, True, False)
        self._pieces[(5, 0)] = Mandarin(5, 0, True, False)
        self._pieces[(4, 0)] = King(4, 0, True, False)
        self._pieces[(1, 2)] = Cannon(1, 2, True, False)
        self._pieces[(7, 2)] = Cannon(7, 2, True, False)
        self._pieces[(0, 3)] = Pawn(0, 3, True, False)
        self._pieces[(2, 3)] = Pawn(2, 3, True, False)
        self._pieces[(4, 3)] = Pawn(4, 3, True, False)
        self._pieces[(6, 3)] = Pawn(6, 3, True, False)
        self._pieces[(8, 3)] = Pawn(8, 3, True, False)

        self._pieces[(0, 9)] = Rook(0, 9, False, True)
        self._pieces[(8, 9)] = Rook(8, 9, False, True)
        self._pieces[(1, 9)] = Knight(1, 9, False, True)
        self._pieces[(7, 9)] = Knight(7, 9, False, True)
        self._pieces[(2, 9)] = Elephant(2, 9, False, True)
        self._pieces[(6, 9)] = Elephant(6, 9, False, True)
        self._pieces[(3, 9)] = Mandarin(3, 9, False, True)
        self._pieces[(5, 9)] = Mandarin(5, 9, False, True)
        self._pieces[(4, 9)] = King(4, 9, False, True)
        self._pieces[(1, 7)] = Cannon(1, 7, False, True)
        self._pieces[(7, 7)] = Cannon(7, 7, False, True)
        self._pieces[(0, 6)] = Pawn(0, 6, False, True)
        self._pieces[(2, 6)] = Pawn(2, 6, False, True)
        self._pieces[(4, 6)] = Pawn(4, 6, False, True)
        self._pieces[(6, 6)] = Pawn(6, 6, False, True)
        self._pieces[(8, 6)] = Pawn(8, 6, False, True)

    @property
    def pieces(self):
        """
        返回棋子
        """
        return self._pieces

    @property
    def images(self):
        """
        get images
        """
        res = dict()
        for pos in self.pieces:
            res[pos] = self.pieces[pos].image

        return res

    @property
    def can_moves(self):
        """
        get can moves image
        """
        res = []
        if self._selected_piece is not None:
            res.append(self._selected_piece.xy)

        if self._moves is not None:
            for pos in self._moves:
                res.append(pos)

        return res

    def get_moves(self):
        """
        获取能移动的位置
        """
        if self._selected_piece:
            self._moves = self._selected_piece.get_moves(self.pieces)

    def select(self, x: int, y: int):
        """
        选择棋子
        """
        # 未选择棋子，选中
        # if self._selected_piece is None:
        # print(x, y, player_is_red)
        if ((x, y) in self.pieces and
                self.pieces[x, y].is_red == self._current_play):
            self._selected_piece = self.pieces[x, y]
            self.get_moves()
            return False, None
        # 选择位置不是指定方棋子， 或没选择棋子， 但没有选中的棋子
        elif self._selected_piece is None:
            return False, None

        # 同一个棋子. 取消选择
        # if self._selected_piece.xy == (x, y):
        #     self._selected_piece = None
        #     self._moves = None
        #     return False, None

        # 移动棋子
        old_x, old_y = self._selected_piece.xy
        # print(x, y)
        if (x, y) in self._moves:
            self._selected_piece = None
            self._moves = []
            game_over = self.move(old_x, old_y, x - old_x, y - old_y)
            if game_over:
                print('游戏结束')
            return True, (old_x, old_y, x, y)
        return False, None

    def move(self, x, y, dx, dy):
        """
        move
        """
        piece = self._pieces[x, y]
        del self._pieces[x, y]

        game_over = False

        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) in self._pieces:
            print('吃子')
            game_over = type(self._pieces[new_x, new_y]) == King

        piece.move(dx, dy)
        self._pieces[x + dx, y + dy] = piece
        self._current_play = not self._current_play
        return game_over
