
for j in range(1000):
    i = 63 * (23 + j*40)
    assert (i % 8 == 1 and i % 6 == 3)
    print i
