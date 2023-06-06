# cbirds

![cbirds'logo](cbirds_logo.png)
---
## Combinator Birds

> This is a port of the haskell package [Data.Aviary.Birds](https://hackage.haskell.org/package/data-aviary-0.4.0/docs/Data-Aviary-Birds.html).

``cbirds`` is a module intended for demonstration purposes rather than a functional or pratical use.

The only way to make sense of function combinators in python would be in a pointfree context. 
Lucky for us, there is a [pointfree](https://pypi.org/project/pointfree/)
module that allows us, e.g., to compose functions smoothly and enable partial application of functions and methods. 

## Examples

Let's define a function keephalf, keephalf is a function that return the first half of a list. 
The first step is to define our own (@pointfree) version of length, integer divisionand and take function but whith.
```python
@pointfree
def pflen(l): return len(l) 
@pointfree
def div(a,x): return a // x
@pointfree
def take(n,l): return l[0:n]
```

We can use the starling bird,it passes a value straight and also through a function to another function of arity 2, and the
caridinal that swaps the argument order.
```python
def cardinal(f,x,y): return f (y,x)
def starling(f,g,x): return f (x) (g(x))

keephalf = starling (cardinal (take), cardinal (div,2) * pflen)
```

```
>>> keephalf([1,2,3,4,5,6,7,8,9,10])
[1, 2, 3, 4, 5]
```
