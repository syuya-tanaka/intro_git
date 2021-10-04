def saiki(n):
    while True:
        if n < 0:
            return 1
        return saiki(n - 1) * n
