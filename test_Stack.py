from task_6_Stack import Stack


def test_Stack():
    n = Stack()
    n.push(4)
    n.push(10)
    assert n.pop() == 10, "wrong pop value"
    n.push(34)
    assert n.pop() == 34, "wrong pop value"
    n.push(64)
    assert n.pop() == 64, "wrong pop value"
    assert n.pop() == 4, "wrong pop value"
    # test invalid
    n.pop()
    n.push(12)



test_Stack()
