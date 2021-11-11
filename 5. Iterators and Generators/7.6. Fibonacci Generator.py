def fibonacci():
    n = 0
    m = 1
    while True:
        yield n
        o = n
        n = m
        m = o + m


generator = fibonacci()
for i in range(10):
    print(next(generator))
