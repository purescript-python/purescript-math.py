import math

acos = math.acos

asin = math.asin

atan = math.atan

atan2 = lambda y: lambda x: math.atan2(y, x)

ceil = math.ceil

cos = math.cos

exp = math.exp

floor = math.floor

trunc = math.trunc
log = math.log

_curried = {
    "max": max,
    "min": min,
    "pow": pow,
}

for k in _curried:
    globals()[k] = lambda x: lambda y: _curried[k](x, y)

remainder = lambda n: lambda m: n % m


sin = math.sin

sqrt = math.sqrt

tan = math.tan

e = math.e

ln2 = math.log2

ln10 = math.log10

log2e = math.log(2)

log10e = math.log(10)

pi = math.pi

tau = 2 * math.pi

sqrt1_2 = math.sqrt(1 / 2)

sqrt2 = math.sqrt(2)
