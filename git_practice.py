print('hello')
print('say hello')
print('git add')
print('眠たいですね')
print('いろいろありますね')


def saiki(x):
    while True:
        if x < 0:
            return 0
        return saiki(x - 1) + x


print(saiki(10))
