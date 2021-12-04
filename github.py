def saiki(n):
    while True:
        if n < 0:
            return 1
        return saiki(n - 1) * n


print("変更を加えます")

# git commit --amend


def test(n):
    while True:
        if n < 0:
            return 0
        return test(n - 1) + n
