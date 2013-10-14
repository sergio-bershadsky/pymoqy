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
>>> q.find = ((~(q.profile.age > 20)) & (q.username == 'test'))()
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