__all__ = ['matmul', 'func', 'func2', 'x']


def matmul(x, y):
    res = [[0] * len(x)] * len(y[0])
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                res[i][j] += x[i][k] * y[k][j]

    return res


def _secretfunc():
    pass


def func():
    print('this is a function')


def func2():
    print('this is a second function')


x = 5

if __name__ == '__main__':
    print(x)
