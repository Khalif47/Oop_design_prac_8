from task_2_List import List


def read_file(filename):
    '''

    :param filename:
    :return text:
    :complexity: O(N)
    '''
    # initialise an object from class list
    try:
        text = List()
        file = open(filename)
        for line in file:
            line = line.strip("\n")
            text.append(line)
        file.close()
        return text
    except FileNotFoundError:
        print("File not found")


print(read_file('trial.txt'))
