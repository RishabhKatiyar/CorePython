class A:
    def __init__(self):
        print('In A init')


class B(A):
    def __init__(self):
        print('In B init')
        super().__init__()

b = B()
