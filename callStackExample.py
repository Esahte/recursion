"""create a call stack"""


def A():
    return 'hello ' + B()


def B():
    return 'my ' + C()


def C():
    return 'friend'


print(A())
