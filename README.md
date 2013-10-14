pymoqy
======

Yet another python-pymongo lib

1. Extremely magic
2. Extremely experimental
3. 95% pythonic mongo operators

The goal is to make tool that will provide more user readable way for creating complex mongodb queries

Some usage example:

*find*
```
>>> q = Query()
>>> q.find = ((~(q.profile.age > 20)) & (q.username == 'test'))
>>> print q.find
{
  "$and": [
    {
      "profile.age": {
        "$not": {
          "$gt": 20
        }
      }
    },
    {
      "username": {
        "$eq": "test"
      }
    }
  ]
}
```

*update*
```
>>> q = Query()
>>> q.username = 'Sergey'
>>> q.profile.age = 28
>>> q.visits += 1
>>> print q.update

{
  "$set": {
    "username": "Sergey",
    "profile.age": 28
  },
  "$inc": {
    "visits": 1
  }
}
```


DOC
===

Building find query
-------------------
operators and grouping:

1. '|' bin 'or' equals to mongodb '$or'
2. '&' bin 'and' equals to '$and'
3. '^' bin 'xor' equals to '$nor' (MongoDB does not have xor operator)
4. '~' bin 'invert' equals to '$not'
5. You can use parentheses for changing operator priority

**Example #1**
```
>>> n1 = Node(1)
>>> n2 = Node(2)
>>> (n1 | n2)()
{'$or': [1, 2]}
```

**Example #2**
```
>>> n1 = Node(1)
>>> n2 = Node(2)
>>> n3 = Node(3)
>>> (n1 | n2 & n2)()
{'$or': [1, {'$and': [2, 3]}]}
```

**Example #3**
```
>>> n1 = Node(1)
>>> n2 = Node(2)
>>> n3 = Node(3)
>>> n4 = Node(4)
>>> (~(n1 | n2) & (n3 ^ n4))()
{'$and': [{'$or': {'$not': [1, 2]}}, {'$nor': [3, 4]}]}
```

**Example #4**
```
>>> q = Query()
>>> q.find = (q.username == 'foobar') & ~(q.age < 10)
>>> q.find
{'$and': [{'username': {'$eq': 'foobar'}}, {'age': {'$not': {'$lt': 10}}}]}
```

Building update queries
-----------------------

**Example #4**
```
>>> q = Query()
>>> q.username = 'nikitinsm'
>>> q.password = hashlib.md5('password').hexdigest()
>>> q.profile.name = 'Sergey'
>>> q.profile.surname = 'Nikitin'
>>> q.profile.age = 28
>>> q.profile.gender = 'M'
>>> q.profile.dob = datetime.datetime(1985, 10, 8).strftime('%Y-%m-%d')
>>> q.created = 1381733783
>>> q.version += 1
>>> q.update
{
  "$set": {
    "username": "nikitinsm",
    "profile.name": "Sergey",
    "created": 1381733783,
    "profile.age": 28,
    "profile.surname": "Nikitin",
    "profile.gender": "M",
    "profile.dob": "1985-10-08",
    "password": "5f4dcc3b5aa765d61d8327deb882cf99"
  },
  "$inc": {
    "version": 1
  }
}
```








