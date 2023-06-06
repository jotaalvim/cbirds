# cbirds

![cbirds'logo](cbirds_logo.png)
---
## Combinator Birds

> This is a port of the haskell package [Data.Aviary.Birds][haskell-docs](https://hackage.haskell.org/package/data-aviary-0.4.0/docs/Data-Aviary-Birds.html).

``cbirds`` is a module intended for demonstration purposes rather than a functional or pratical use.

The only way to make sense of function combinators in python would be in a pointfree context. 
Lucky for us, there is a [pointfree](https://pypi.org/project/pointfree/)
module that allows us, e.g., to compose functions smoothly and enable partial application of functions and methods. 

## Examples

```python
@pointfree
def pflen(l): return len(l) 
@pointfree
def div(a,x): return a // x
@pointfree
def take(n,l): return l[0:n]

# function that return the first half of a list
keephalf = starling (cardinal (take), cardinal (div,2) * pflen)
```

```
>>> keephalf([1,2,3,4,5,6,7,8,9,10])
[1, 2, 3, 4, 5]
```
