pymoqy
======

Yet another python-pymongo lib
Extremely magic and experimental

The goal is to make tool that will provide more user readable way for creating complex mongodb queries

Some example usage:

```
<<< q = Query()
<<< q.find = ((~(q.profile.age > 20)) & (q.username == 'test'))()
<<< print q.find

>>>
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