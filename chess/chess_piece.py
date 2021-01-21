# coding=utf-8

MAX_X = 8
MAX_Y = 9


class ChessPiece(object):
    """
    棋子类
    """
    def __init__(self, x: int, y: int, is_red: bool, is_north: bool):
        self._x = x
        self._y = y
        self._is_red = is_red  # 是否红方
        self._is_north = is_north  # 是否北方

    @property
    def is_red(self):
        """
        get is red
        """
        return self._is_red

    @property
    def is_north(self):
        """
        get is north
        """
        return self._is_north

    @property
    def image(self):
        """
        获取棋子类图像
        """
        raise NotImplementedError

    @property
    def xy(self):
        """
        get xy
        """
        return self._x, self._y

    def can_move(self, pieces: dict, dx: int, dy: int):
        """
        can move
        """
        if abs(dx) + abs(dy) == 0:
            return False
        new_x = self._x + dx
        new_y = self._y + dy
        # 边界检测
        if new_x < 0 or new_x > MAX_X:
            return False

        if new_y < 0 or new_y > MAX_Y:
            return False

        if ((new_x, new_y) in pieces and
                (pieces[new_x, new_y].is_red == self.is_red)):
            return False
        return True

    def counts(self, pieces: dict, dx: int, dy: int):
        """
        计算 x，x+dx之间的棋子
        计算 y, y+dy之间的棋子
        """
        sx = 0
        sy = 0
        if dx != 0:
            if dx > 0:
                sx = 1
            else:
                sx = -1

        if dy != 0:
            if dy > 0:
                sy = 1
            else:
                sy = -1

        x = self._x + sx
        y = self._y + sy
        new_x = self._x + dx
        new_y = self._y + dy

        res = 0
        while x != new_x or y != new_y:
            if (x, y) in pieces:
                res += 1
            x += sx
            y += sy

        return res

    def get_moves(self, pieces: dict):
        """
        获取所有能移动的位置
        """
        raise NotImplementedError

    def move(self, dx: int, dy: int):
        """
        移动棋子，移动前应该确认能够移动
        """
        self._x += dx
        self._y += dy
