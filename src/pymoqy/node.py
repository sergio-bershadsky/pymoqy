from pprint import PrettyPrinter

pp = PrettyPrinter(indent=1)


class Node(object):

    data = None
    type = None
    initial = True

    def __init__(self, data, initial=True):
        self.data = data
        self.initial = initial

    def __repr__(self):
        return pp.pformat(self.data)

    def __and__(self, other):
        try:
            return Node({'$and': self.data['$and'] + [other.data]})
        except (TypeError, KeyError):
            return Node({'$and': [self.data, other.data]})

    def __or__(self, other):
        try:
            return Node({'$or': self.data['$or'] + [other.data]})
        except (TypeError, KeyError):
            return Node({'$or': [self.data, other.data]})

    def __xor__(self, other):
        try:
            return Node({'$nor': self.data['$nor'] + [other.data]})
        except (TypeError, KeyError):
            return Node({'$nor': [self.data, other.data]})

    def __invert__(self):
        try:
            key, value = self.data.items()[0]
            return Node({key: {'$not': value}})
        except (AttributeError, IndexError):
            return Node({'$not': self.data})

    def __call__(self):
        return self.data