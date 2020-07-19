def print_formatted(N):
    w = len("{0:b}".format(N))
    for i in range(1,N+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))
