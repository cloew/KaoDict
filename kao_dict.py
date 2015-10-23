from kao_decorators import proxy_for

@proxy_for('_dict', ['__iter__', '__contains__', '__len__', '__getitem__', '__setitem__'])
class KaoDict(object):
    """ Represents a Dictionary """
    INSTANCE_ATTRS = {'_dict'}
    
    def __init__(self, d=None):
        """ Initialize with the dictionary """
        if d is None:
            d = {}
        self._dict = d
            
    def __getattr__(self, attr):
        """ Return the value for the given attr """
        try:
            return self._dict[attr]
        except KeyError:
            raise AttributeError(attr)
        
    def __setattr__(self, attr, value):
        """ Return the value for the given attr """
        if attr in self.INSTANCE_ATTRS:
            object.__setattr__(self, attr, value)
        else:
            self._dict[attr] = value