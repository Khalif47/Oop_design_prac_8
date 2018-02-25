from task_1_List import List


def test_list():
    test = List(50)
    test.append(4)
    test.append(2)
    test.append(-3)
    assert len(test) == 3, "incorrect length, length should be 3"
    assert test.delete(1) is True, "did not delete"
    assert str(test) == "4\n-3\n", "wrong"
    test.append(-8)
    assert str(test) == "4\n-3\n-8\n", "wrong list"
    test.remove(-3)
    assert str(test) == "4\n-8\n", "wrong list"
    assert len(test) == 2, "incorrect length list"
    test.append(-7)
    test.append(-1)
    test.sort()
    assert str(test) == "-8\n-7\n-1\n4\n", "wrong list"
    test.remove(-7)
    assert str(test) == "-8\n-1\n4\n", "did not remove -7"
    test.append(9)
    assert str(test) == "-8\n-1\n4\n9\n", "did not append 9"
    # assert test.search(-1) == 1, "did not search correctly"
    # assert test.search(4) == 2, "did not search correctly"
    test.sort(False)
    assert str(test) == "-8\n-1\n4\n9\n", "did not sort properly"
    test.delete(2)
    assert str(test) == "-8\n-1\n9\n", "did not delete correctly"
    test.insert(1, -10)
    assert str(test) == "-8\n-10\n-1\n9\n", "did not insert correctly"
    assert len(test) == 4, "not correct length"
    test[1] = 17
    test[3] = 19
    assert str(test) == "-8\n17\n-1\n19\n", "did not insert correctly"
    # assert test.search(19) == 3, "did not search correctly"
    assert (-8 in test) is True, '-8 is in test'
    assert (100 in test) is False, '100 not in test'
    assert test.is_empty() is False, 'list is not empty'
    test.append(-1)
    test.remove(-1)
    assert str(test) == "-8\n17\n19\n", "did not remove correctly"
    # assert test.search(17) == 1, "did not search correctly"
    # assert test.search(-8) == 0, "did not search correctly"
    assert (test == [-8, 17, 19]) is True, "list should be equal"
    assert (test == [-1, -8, 17, 19]) is False, "list should not be equal"
    test.append(8.23)
    assert (test == [-8, 17, 19, 8.23]) is True, "list should be equal"

    # Check if it will print error if appending
    for i in range(50):
        test.append(2)



    return


if __name__ == '__main__':
    test_list()
    print("All test cases passing! ")
