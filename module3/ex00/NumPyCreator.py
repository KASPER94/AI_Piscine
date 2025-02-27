import numpy as np
import collections

class NumPyCreator():
    def _from_type(self, obj, otype):
        np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
        if not isinstance(obj, otype):
            return None
        array = np.array(obj)
        if array.dtype is np.dtype('object'):
            return None
        if (len(array.shape)) == 2:
            for elem in obj:
                if not isinstance(elem, otype):
                    return None
        return array
    
    def from_list(self, lst):
        return self._from_type(lst, list)
    
    def from_tuple(self, tpl):
        return self._from_type(tpl, tuple)
    
    def from_iterable(self, itr):
        return self._from_type(itr, collections.Iterable)
    
    def from_shape(self, shape, value = 0):
        if isinstance(shape, tuple):
            return np.zeros(shape)
            # return np.full(shape, value)
        return None
    
    def random(self, shape):
        if isinstance(shape, tuple):
            return np.random.random(shape)
        return None
    
    def identity(self, n):
        if isinstance(n, int) and n >= 0:
            return np.identity(n)
        return None
