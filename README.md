pymoqy
======

Yet another python-pymongo lib
Extremely magic and experimental

The goal is to make tool that will provide more user readable way for creating complex mongodb queries

Some example usage:

```
>>> user = User()
>>> print (~(user.hero.level > 1)) & (user.username == 'test')

result:

{
  "$and": [
    {
      "hero.level": {
        "$not": {
          "$gt": 1
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