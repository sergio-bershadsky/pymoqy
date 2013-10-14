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

1. | - logical 'or' equals to mongodb '$or'
2. & - logical 'and' equals to '$and'
3. ^ - logical 'xor' equals to '$nor' (MongoDB does not have xor operator)
4. ~ - logical 'invert' equals to '$not'
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








