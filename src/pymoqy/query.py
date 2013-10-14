from pymoqy.path import Path


class Query(object):

    update = None
    find = None

    def __init__(self):
        self.update = {}

    def __repr__(self):
        return str( (self.update, self.find) )

    def __getattr__(self, item):
        if item[:2] == '__':
            return object.__getattribute__(self, item)
        return getattr(Path(self), item)

    def __setattr__(self, key, value):
        if key[0] == '_' or key in ('update', 'find'):
            object.__setattr__(self, key, value)
        else:
            setattr(Path(self), key, value)

    def __delattr__(self, item):
        delattr(Path(self), item)