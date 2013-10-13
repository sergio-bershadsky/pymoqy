pymoqy
======

Yet another python-pymongo lib
1. Extremely magic
2. Extremely experimental
3. 95% pythonic mongo operators

The goal is to make tool that will provide more user readable way for creating complex mongodb queries

Some usage example:

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