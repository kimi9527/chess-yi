
def Chessman(object):
    def __init__(self, name):
        self.name = name

    @property
    def row(self):
        return self.name