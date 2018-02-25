from task_2_List import List
from task_6_Stack import Stack


# implement a editor class


class TextEditor:
    def __init__(self):
        self.list = List()
        self.stack = Stack()

    def insert_num(self, line_num, word):
        '''

        :param line_num:
        :param word:
        :return: list
        :complexity: worst case O(N) best case O(N)
        '''
        self.stack.push((line_num,'we', 'no'))
        self.list.insert(line_num, word)
        return self.list

    def read_filename(self, filename):
        '''

        :param filename:
        :return: list
        :complexity: O(N)
        '''
        try:
            file = open(filename)
            for line in file:
                line = line.strip("\n")
                self.list.append(line)
            file.close()
            return self.list
        except FileNotFoundError:
            print("Enter a correct file")

    def write_filename(self, filename):
        '''

        :param filename:
        :complexity: O(N)
        '''
        file = open(filename, "w")
        for i in range(len(self.list)):
            file.write(self.list[i] + "\n")
        file.close()

    # def write_filename(self, filename):
    def print_num1_num2(self, num1, num2):
        '''

        :param num1:
        :param num2:
        :return: string
        :complexity: O(N)
        '''
        try:
            num1 = int(num1)
            num2 = int(num2)
            assert num1 < num2, "invalid positions"
            string = ""
            while num1 < num2:
                string += self.list[num1] + "\n"
                num1 += 1
            return string
        except TypeError:
            print('enter correct intervals')
        except ValueError:
            print('Enter Valid position number')
        except AssertionError:
            print('invalid positions')

    def delete_num(self, line):
        '''

        :param line:
        :return: list
        :complexity: best case O(N), worst case O(N)
        '''
        # push line number first
        # use a tuple to represent line num and item for insert
        self.stack.push((line, self.list[line]))
        self.list.delete(line)
        return self.list

    def undo(self):
        '''
        :return: list
        :complexity: O(1) however complexity considers insert so best case O(1) and worst case O(N)
        '''
        try:
            my_tuple = self.stack.pop()
            # if length of tuple is two I must insert line and line num
            if len(my_tuple) == 2:
                self.list.insert(int(my_tuple[0]), str(my_tuple[1]))
            else:
                self.list.delete(int(my_tuple[0]))
            return self.list
        except TypeError:
            print('Stack is empty! ')

    def search_word(self, word):
        '''

        :param word:
        :return: n
        :complexity: best case O(1), worst case O(N)
        '''
        word = word.lower()
        n = self.list.search(word)
        return n


