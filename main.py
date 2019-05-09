from stack import Stack


def test_integers():
    s = Stack()
    s.push(5)
    t = s.pop()
    print(t)


def test_floats():
    print("test floats")
    S=Stack(2.3)
    S.push(5.0)
    t=s.pop()
    print(t)



def test_strings():
    print("test string")
    S=Stack("")
    S.push("go nuggets")
    t=S.pop()
    print(t)


def test_exception_int():
    print("exception test")
    S=Stacks(5)
    S.push("go nuggets")
    t=s.pop()
    print(t)


def safe_test_int_exception():
    print("safe non int test")
    S=IntStack()
    S.push(5)





if __name__ == '__main__':
    test_integers()

    try:
        test exception()
    except ValueError:
        print("exception test value error")

    try:
        test_string()
    except ValueError:
        print("string test value error")

    try:
        test_integers()
    except ValueError:
        print("integer test value error")

    try:
        test_floats()
    except ValueError()
        print("float test error")
    try:
        safe_test_nonint()
    except VAlueError()
        print("Safe test non int value error")
    try:
        safe_test_int()
    except
