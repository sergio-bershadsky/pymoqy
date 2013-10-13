from pymoqy.path import Path


class Query(object):

    update = None
    find = None

    def __init__(self):
        self.update = {}
        self.find = {}

    def __repr__(self):
        return str( (self.update, self.find) )

    def __getattr__(self, item):
        if item[:2] == '__':
            return object.__getattribute__(self, item)
        return getattr(Path(self), item)

    def __setattr__(self, item, value):
        #print item, value
        if hasattr(self, item):
            object.__setattr__(self, item, value)
        else:
            setattr(Path(self), item, value)

    def __delattr__(self, item):
        delattr(Path(self), item)