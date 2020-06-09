import math

abs = abs

acos = math.acos

asin = math.asin

atan = math.atan


cos = math.cos

exp = math.exp


trunc = math.trunc
log = math.log

_curried = {"max": max, "min": min, "pow": pow, "atan2": math.atan2}

for k in _curried:
    globals()[k] = lambda x: lambda y: _curried[k](x, y)

remainder = lambda n: lambda m: n % m


def map_nan_inf_to_zero(f):
    def result(n):
        if math.isnan(n) or math.isinf(n):
            return 0
        else:
            return f(n)
    return result


round = map_nan_inf_to_zero(round)

floor = map_nan_inf_to_zero(math.floor)

ceil = map_nan_inf_to_zero(math.ceil)

sin = math.sin

sqrt = math.sqrt

tan = math.tan

e = math.e

ln2 = math.log2

ln10 = math.log10

log2e = math.log(math.e, 2)

log10e = math.log(math.e, 10)

pi = math.pi

tau = 2 * math.pi

sqrt1_2 = math.sqrt(1 / 2)

sqrt2 = math.sqrt(2)
