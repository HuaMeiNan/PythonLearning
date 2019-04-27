def huanhuota(n, a, b, c):
    if n == 1:
        print(a ,'->' ,c)

    else:
        huanhuota(n-1, a, c, b)
        print(a, '->', c)
        huanhuota(n-1, b, a, c)

huanhuota(4,'a','b','c')