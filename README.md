# Nested Classes

A decorator that fixes scope resolution in classes.

```python
from nestedclasses import nestedclasses

@nestedclasses()
class A:
    x = 1
    class B:
        y = x + 1

assert A.x   == 1
assert A.B.y == 2
```

## Motivation

Say you're using classes for configurations, and want to nest them like so:

```python
class config:
    root = '/app'
    class log:
        path = os.path.join(root, 'log.txt')
```

Turns out that for some obscure reason, scoping doesn't work the way you'd expect it to when it comes to class bodies:
this code ``NameError``s with ``name 'root' is not defined``. Unless...

```python
@nestedclasses()
class config:
    root = '/app'
    class log:
        path = os.path.join(root, 'log.txt')

assert config.log.path == '/app/log.txt'
```
