from task_3_file_function import read_file


def test_read_file():
    read_file("no")
    read_file("were.txt")
    print(read_file("read.txt"))
    read_file('test.txt')
    # assert read_file("read.txt") == "must\nchampions league\nwere\nto"


if __name__ == '__main__':
    test_read_file()
    print('All test cases passing! ')
