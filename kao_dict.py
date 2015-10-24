from collections.abc import MutableMapping

class KaoDict(MutableMapping):
    """ Represents a Dictionary """
    INSTANCE_ATTRS = {'_dict'}
    
    def __init__(self, *args, **kwargs):
        """ Initialize with the dictionary """
        self._dict = dict(*args, **kwargs)
            
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
            
    # Mapping overrides
    def __getitem__(self, key):
        return self._dict[key]
        
    def __setitem__(self, key, value):
        self._dict[key] = value
        
    def __delitem__(self, key):
        del self._dict[key]
        
    def __iter__(self, key):
        return iter(self._dict)
        
    def __len__(self):
        return len(self._dict)