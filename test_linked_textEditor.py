from linked_textEditor import TextEditor

tester = TextEditor()


def test_textEditor():
    tester.read_filename('test.txt')
    tester.insert_num(0, 'we')
    tester.insert_num(1, 'must')
    assert tester.search_word('we') == 0, "wrong list structure or search implementation"
    print(tester.insert_num(1, 'you'))
    assert tester.search_word('you') == 1, "wrong list structure or search implementation"
    assert tester.search_word('no') == 4, "wrong list structure or search implementation"
    assert tester.search_word('infinite') == 5, "wrong list structure or search implementation"
    tester.insert_num(-1, 'yes')
    assert tester.search_word('yes') == 5, "wrong list structure or search implementation"
    tester.delete_num(-2)
    assert tester.search_word('infinite') == 5, "wrong list structure or search implementation"
    tester.delete_num(2)
    assert tester.search_word('to') == 2, "wrong list structure or search implementation"

    # tester.undo()
    # assert tester.search_word('infinite') == 5, "wrong list structure or search implementation"

    # invalid cases
    tester.read_filename('sfojkeo')
    tester.read_filename('ehbfe')
    tester.read_filename('never')
    tester.insert_num(100, 'we')
    tester.insert_num(-50, 'must')
    tester.insert_num(50, 'no')
    tester.delete_num(-100)
    tester.delete_num(15)
    tester.delete_num('ab')
    tester.print_num1_num2(0, 3)
    tester.print_num1_num2(20, 50)
    tester.print_num1_num2('yes', 'yes')


if __name__ == '__main__':
    test_textEditor()
    print('All test cases passing! ')
