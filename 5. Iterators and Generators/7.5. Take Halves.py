def solution():
    def integers():
        ints = 1
        while True:
            yield ints
            ints += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        zle = []
        for i in seq:
            if len(zle) == n:
                return zle
            zle.append(i)

    return take, halves, integers


taker = solution()[0]
halvesr = solution()[1]
print(taker(5, halvesr()))
