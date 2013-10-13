from pymoqy.node import Node


class Path(object):

    _data = None
    _query = None

    def __init__(self, query=None):
        self._data = list()
        self._query = query

    def __getattr__(self, item):
        if item[:2] == '__':
            return object.__getattribute__(self, item)
        self._data.append(item)
        return self

    def __setattr__(self, key, value):
        if key[:1] == '_':
            object.__setattr__(self, key, value)
        else:
            self._query and self._query.update.append({'$set': {str(self): value}})

    def __repr__(self):
        return '.'.join(self._data)
    __str__ = __repr__

    #comparison magic
    def __gt__(self, other):
        return Node({str(self): {'$gt': other}})

    def __ge__(self, other):
        return Node({str(self): {'$gte': other}})

    def __lt__(self, other):
        return Node({str(self): {'$lt': other}})

    def __le__(self, other):
        return Node({str(self): {'$lte': other}})

    def __mod__(self, other):
        return Node({str(self): {'$mod': other}})

    def __eq__(self, other):
        if self._data[-1][:3] == 's__':
            return Node({'.'.join(self._data[:-1]): {'$%s' % self._data[-1][3:]: other}})
        return Node({str(self): {'$eq': other}})