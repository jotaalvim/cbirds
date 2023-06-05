from pointfree import *


@pointfree
def idiot(a): return a 
"""
I combinator - identity bird / idiot bird - Haskell 'id'.

idiot :: a -> a
"""

def kestrel (a,_b): return a
"""
kestrel :: a -> b -> a
K combinator - kestrel - Haskell 'const'. Corresponds to the encoding of @true@ in the lambda calculus.
"""

@pointfree
def bluebird(f,g,x): return f(g(x))
"""
bluebird :: (b -> c) -> (a -> b) -> a -> c
B combinator - bluebird - Haskell ('.').
"""

@pointfree
def cardinal(f,x,y): return f (y,x)
"""
C combinator - cardinal - Haskell 'flip'.
cardinal :: (a -> b -> c) -> b -> a -> c
"""

@pointfree
def applicator(a,b): return a(b)
"""
A combinator - apply / applicator - Haskell ('$').
This is also called @i-star@.
applicator :: (a -> b) -> a -> b
"""

@pointfree
def psi(f,g,x,y): return x(y(z), y(w))
"""
 Psi combinator - psi bird (?) - Haskell 'on'.
psi :: (b -> b -> c) -> (a -> b) -> a -> a -> c
"""


@pointfree
def becard(f,g,h,x): return f (g (h (x)))
"""
B3 combinator - becard.
becard :: (c -> d) -> (b -> c) -> (a -> b) -> a -> d
"""


@pointfree
def blackbird (f,g,x,y): return f(g(x,y))
"""
B1 combinator - blackbird - specs 'oo'.
blackbird :: (c -> d) -> (a -> b -> c) -> a -> b -> d
"""

@pointfree
def bluebird_ (f,x,g,y): return f (x) (g (y))
"""
B' combinator - bluebird prime.
bluebird' :: (a -> c -> d) -> a -> (b -> c) -> b -> d
"""


@pointfree
def bunting (f,g,x,y,z): return f (g (x,y,z))
"""
B2 combinator - bunting - specs 'ooo'.
bunting :: (d -> e) -> (a -> b -> c -> d) -> a -> b -> c -> e
"""

@pointfree
def cardinal_ (f,g,x,y): return f (g(y),x)
"""
C' combinator - no name.
cardinal' :: (c -> a -> d) -> (b -> c) -> a -> b -> d
"""


@pointfree
def cardinalstar (f,x,y,z): return f (x,z,y)
"""
C* combinator - cardinal once removed.
cardinalstar :: (a -> c -> b -> d) -> a -> b -> c -> d
"""

@pointfree
def cardinalstarstar (f,s,t,u,v): return  f(s,t,v,u)
"""
C** combinator - cardinal twice removed.
cardinalstarstar :: (a -> b -> d -> c -> e) -> a -> b -> c -> d -> e
"""


@pointfree
def dickcissel (f,x,y,g,z): return f (x,y,g(z))
"""
D1 combinator - dickcissel.
dickcissel :: (a -> b -> d -> e) -> a -> b -> (c -> d) -> c -> e
"""


@pointfree
def dove(f,x,g,y): return f (x, g(y))
"""
D combinator - dove.
dove :: (a -> c -> d) -> a -> (b -> c) -> b -> d
"""

@pointfree
def dovekie(f,g,x,h,z): return f (g(x),h(z))
"""
D2 combinator - dovekie.
dovekie :: (c -> d -> e) -> (a -> c) -> a -> (b -> d) -> b -> e
"""

@pointfree
def eagle (f,x,g,y,z): return f (x, g(y,z))
"""
E combinator - eagle.
eagle :: (a -> d -> e) -> a -> (b -> c -> d) -> b -> c -> e
"""

@pointfree
def eaglebald (f,g,s,t,h,u,v): return f (g(s,t), h(u,v))
"""
E \^ - bald eagle.
For alphabetical regularity it is somewhat misnamed here as
eaglebald.
eaglebald :: (e -> f -> g)
          -> (a -> b -> e)
          -> a -> b
          -> (c -> d -> f)
          -> c -> d -> g
"""

@pointfree
def finch (x,y,f): return f (y,x)
"""
F combinator - finch.
finch :: a -> b -> (b -> a -> c) -> c
"""

@pointfree
def finchstar (f,x,y,z): return f(z,y,x)
"""
F* combinator - finch once removed.
finchstar :: (c -> b -> a -> d) -> a -> b -> c -> d
"""

@pointfree
def finchstarstar (f,s,t,u,v): return f (s,v,u,t)
"""
F** combinator - finch twice removed.
finchstarstar :: (a -> d -> c -> b -> e) -> a -> b -> c -> d -> e
"""


@pointfree
def goldfinch (f,g,x,y) : return f (y, g(x) )
"""
G combinator - goldfinch.
goldfinch :: (b -> c -> d) -> (a -> c) -> a -> b -> d
"""

@pointfree
def hummingbird (f,x,y): return f (x,y,x)
"""
H combinator - hummingbird.
hummingbird :: (a -> b -> a -> c) -> a -> b -> c
"""


@pointfree
def idstar (f,x): return (f,x)
"""
I* combinator - identity bird once removed
-- Alias of 'applicator', Haskell\'s ('$').
idstar :: (a -> b) -> a -> b
"""

@pointfree
def idstarstar (f,x,y): return f (x,y)
"""
I** combinator - identity bird twice removed
idstarstar :: (a -> b -> c) -> a -> b -> c
"""


@pointfree
def jalt (f,x,_y): return f (x)
"""
Alternative J combinator - this is the J combintor of Joy,
-- Rayward-Smith and Burton (see. Antoni Diller \'Compiling
-- Functional Languages\' page 104). It is not the J - jay
-- combinator of the literature.
jalt :: (a -> c) -> a -> b -> c
"""

@pointfree
def jalt_ (f,x,y,_z): return f (x,y)
"""
J' combinator - from Joy, Rayward-Smith and Burton.
-- See the comment to 'jalt'.
jalt' :: (a -> b -> d) -> a -> b -> c -> d
"""

@pointfree
def jay (f,x,y,z): return f (x, f(z,y))
"""
J combinator - jay.
-- This is the usual J combinator.
jay :: (a -> b -> b) -> a -> b -> a -> b
"""


@pointfree
def kite (_x,y): return y
"""
Ki - kite.
-- Corresponds to the encoding of @false@ in the lambda calculus.
kite :: a -> b -> b
"""

@pointfree
def owl(x,y): return y(x(y))
"""
O combinator - owl.
owl :: ((a -> b) -> a) -> (a -> b) -> b
"""


@pointfree
def phoenix (f,g,h,x): return f (g(x), h(x))
"""
(Big) Phi combinator - phoenix - Haskell 'liftM2'.
--
-- This is the same function as 'Data.Aviary.Birds.starling''.
--
phoenix :: (b -> c -> d) -> (a -> b) -> (a -> c) -> a -> d
"""


@pointfree
def quacky (x,f,g): return g(f(x))
"""
Q4 combinator - quacky bird.
quacky :: a -> (a -> b) -> (b -> c) -> c
"""

@pointfree
def queer (f,g,x): return g (f (x))
"""
Q combinator - queer bird.
--
-- Haskell @(\#\#)@ in Peter Thiemann\'s Wash, reverse composition.
queer :: (a -> b) -> (b -> c) -> a -> c
"""

@pointfree
def quirky(f,x,g): return g (f(x))
"""
Q3 combinator - quirky bird.
quirky :: (a -> b) -> a -> (b -> c) -> c
"""


@pointfree
def quixotic(f,x,g): return f (g(x))
"""
Q1 combinator - quixotic bird.
quixotic :: (b -> c) -> a -> (a -> b) -> c
"""

@pointfree
def quizzical(x,f,g): return f (g(x))
"""
Q2 combinator - quizzical bird.
quizzical :: a -> (b -> c) -> (a -> b) -> c
"""


@pointfree
def robin(x,f,y): return f(y,x)
"""
R combinator - robin.
robin :: a -> (b -> a -> c) -> b -> c
"""


@pointfree
def robinstar(f,x,y,z): return f(y,z,x)
"""
R* combinator - robin once removed.
robinstar :: (b -> c -> a -> d) -> a -> b -> c -> d
"""

@pointfree
def robinstarstar(f,s,t,u,v): return f(s, u, v, t)
"""
R** combinator - robin twice removed.
robinstarstar :: (a -> c -> d -> b -> e) -> a -> b -> c -> d -> e
"""

@pointfree
def starling(f,g,x): return f (x, g(x))
"""
S combinator - starling.
--
-- Haskell: Applicative\'s @(\<*\>)@ on functions.
--
-- Substitution.
starling :: (a -> b -> c) -> (a -> b) -> a -> c
"""


@pointfree
def starling_(f,g,h,x): return f (g(x), h(x))
"""
S' combinator - starling prime - Turner\'s big phi.
-- Haskell: Applicative\'s 'liftA2' on functions (and similarly
-- Monad\'s 'liftM2').
--
-- This is the same function as 'Data.Aviary.Birds.phoenix'.
--
starling' :: (b -> c -> d) -> (a -> b) -> (a -> c) -> a -> d
"""


@pointfree
def thrush(x,f): return f(x)
"""
T combinator - thrush.
-- Haskell @(\#)@ in Peter Thiemann\'s Wash, reverse application.
thrush :: a -> (a -> b) -> b
"""

@pointfree
def vireo(x,y,f): return f(x,y)
"""
V combinator - vireo (pairing).
vireo :: a -> b -> (a -> b -> c) -> c
"""

@pointfree
def vireostar(f,x,y,z): return f(y,x,z)
"""
V* combinator - vireo once removed.
vireostar :: (b -> a -> b -> d) -> a -> b -> b -> d
"""

@pointfree
def vireostarstar(f,s,t,u,v): return f(s,v,t,u)
"""
V** combinator - vireo twice removed.
vireostarstar :: (a -> c -> b -> c -> e) -> a -> b -> c -> c -> e
"""


@pointfree
def warbler(f,x): return f (x,x)
"""
W combinator - warbler - elementary duplicator.
warbler :: (a -> a -> b) -> a -> b
"""

@pointfree
def warbler1 (x,f): return f(x,x)
"""
W1 combinator - converse warbler.
-- 'warbler' with the arguments reversed.
warbler1 :: a -> (a -> a -> b) -> b
"""

@pointfree
def warblerstar (f,x,y): return f(x,y,y)
"""
W* combinator - warbler once removed.
warblerstar :: (a -> b -> b -> c) -> a -> b -> c
"""

@pointfree
def warblerstarstar(f,x,y,z): return f(x,y,z,z)
"""
W** combinator - warbler twice removed.
warblerstarstar :: (a -> b -> c -> c -> d) -> a -> b -> c -> d
"""


#-------------------------------------------------------------------------------
@pointfree
def pflen(l): return len(l)
@pointfree
def div(a,x): return a // x
@pointfree
def take(n,l): return l[0:n]

# function that return the first half of a list
#pfhalf: return starling (cardinal (take), cardinal (div,2) * pflen)
pfhalf = starling (cardinal (take), cardinal (div,2) * pflen)
#-------------------------------------------------------------------------------


