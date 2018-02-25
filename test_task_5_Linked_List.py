from task_5_Linked_List import List


def test_list():
    test = List()
    test.append(4)
    test.append(2)
    test.append(-3)
    assert len(test) == 3, "incorrect length, length should be 3"
    test.delete(1)
    assert str(test) == "4\n-3\n", "wrong"
    test.append(-8)
    assert str(test) == "4\n-3\n-8\n", "wrong list"
    test.remove(-3)
    assert str(test) == "4\n-8\n", "wrong list"
    test.delete(-1)
    assert str(test) == "4\n"
    test.delete(0)
    assert str(test) == ""
    test.append(4)
    test.append(-8)
    assert len(test) == 2, "incorrect length list"
    test.append(-7)
    test.append(-1)
    test.sort(False)

    # Now test for invalid values
    # getting
    n = test[-400]
    n = test["nothing"]
    # setting
    test[-500] = 60
    test["p"] = 0
    # equal
    n = test == "2"
    n = test == "me"
    # insert
    test.insert(-400, 20)
    test.insert("pe", "no")
    test[1] = 2
    print(test.search(2))
    print(test)


if __name__ == "__main__":
    test_list()
