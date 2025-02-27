import nympy as np
import string

class ScrapBooker():
    def shape(self, tpl):
        if not isinstance(tpl, tuple):
            return False
        if not len(tpl) == 2:
            return False
        if not isinstance(tpl[0], int) or not isinstance(tpl[1], int):
            return False
        if tpl[0] < 0 or tpl[1] < 0:
            return False
        return True

    def crop(self, array, dim, position=(0,0)):
        if not isinstance(array, np.ndarray) or not self.shape(dim) or not self.shape(position):
            return None
        px = position[0]
        ex = position[0] + dim[0]
        py = position[1]
        ey = position[1] + dim[1]
        if ex > len(array) or ey > len(array[0]):
            return None
        return array[px:ex,py:ey]

    def thin(self, array, n, axis):

    def juxtapose(self, array, n, axis):

    def mosaic(self, array, dim):
