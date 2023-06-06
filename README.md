# cbirds
![](cbirds_logo.png)
---
## Combinator Birds

> This is a port of the haskell package [Data.Aviary.Birds](https://hackage.haskell.org/package/data-aviary-0.4.0/docs/Data-Aviary-Birds.html).

``cbirds`` is a module intended for demonstration purposes rather than a functional or pratical use.

The only way to make sense of function combinators in python would be in a pointfree context. 
Lucky for us, there is a [pointfree](https://pypi.org/project/pointfree/)
module that allows us, e.g., to compose functions smoothly and enable partial application of functions and methods. 

## Examples

Let's define a function keephalf, keephalf is a function that return the first half of a list. 
```
>>> keephalf([1,2,3,4,5,6,7,8,9,10])
[1, 2, 3, 4, 5]
```
In this example the * symbol is means function composition (from the ``pointfree`` module). For the ones wanting to
reach te highest level of bird use, theres a combinator that composes functions: the **bluebird** but for reasons of
readability we'll use * ,for now.

The most intuitive birds to use in this example is the **phoenix**.
The phoenix passes a single value through two different functions, 
and pass the results to a two-parameter function. We'll also use the **idiot** bird, that is the identity function.

```python
#phoenix x y z w = x (y w) (z w)
#idiot x = x

keephalf = phoenix (take, cardinal (div,2) * pflen, idiot)
```

Let's try different birds now, let's use the **starling** and the **cardinal** .
The starling passes a value straight and also through a function to another function of arity 2, and the
caridinal that swaps the argument order.

```python
#starling = x y z = x z (y z)
#cardinal x y z = x (z y)

keephalf2 = starling (cardinal (take), cardinal (div,2) * pflen)
```

We can also use the **warbler** and the **cardinal__**. The warbler is a elementary duplicator, the cardinal__
pass first argument straight, and second argument through a function,
to a two-parameter function

```python
#cardinal_ x y z w = x (y w) z
#warbler x y = x y y
keephalf3 = warbler (cardinal_ (take , cardinal(div, 2) * pflen))
```




The first step is to define our own (@pointfree) version of length, integer division and and take.
```python
@pointfree
def pflen(l): return len(l) 
@pointfree
def div(a,x): return a // x
@pointfree
def take(n,l): return l[0:n]
```


