def increase(n):
    return lambda x : x+n

f = increase(40)
print f(1)
print f(11)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair : pair[1])
print pairs