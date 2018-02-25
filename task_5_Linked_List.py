from Node import Node


class List:
    def __init__(self):
        self.head = 0
        self.count = 0

    def __len__(self):
        return self.count

    def __eq__(self, other):
        '''
        checks if List is equal to the python one.
        :param other:
        :return: True/ False
        :complexity: worst O(N), best case O(1)
        '''
        try:

            if len(other) == self.count:
                for i in range(self.count):
                    if str(self[i]) != str(other[i]):
                        return False
                return True
            return False
        except TypeError:
            print("Compare a valid List")

    def _is_empty(self):
        '''

        :return:
        :complexity: O(1)
        '''
        return self.count == 0

    def is_full(self):
        '''

        :return: o(1)
        '''
        return False

    def __getitem__(self, index):
        '''
        :complexity: best case O(1) worst case O(N)
        :param index:
        :return: nodee
        '''
        try:
            assert 0 <= index < self.count or -self.count <= index <= 0, "Index out of range"
            if index < 0:
                index = self.count + index
            node = self.head
            for _ in range(index):
                node = node.next
            return node
        except AssertionError:
            print("index out of range")
        except IndexError:
            print("Enter a valid index within range.")
        except TypeError:
            print("Enter an integer")

    def __setitem__(self, index, item):
        '''

        :param index:
        :param item:
        :return: self.array[index]
        :complexity: O(N) best case O(1)
        '''
        try:
            assert 0 <= index < self.count or -self.count <= index <= 0, "Index out of range"
            if index < 0:
                index = self.count + index
            node = self.head
            for _ in range(index):
                node = node.next
            node.item = item
            return node.item
        except AssertionError:
            print("index out of range")
        except IndexError:
            print("Enter a valid number within range.")
        except TypeError:
            print("Enter an integer")

    # def insert(self, index, item):
    #     '''
    #     inserts an element in the correct position at the correct index and shifts everything after that up by 1 index
    #     :param index:
    #     :param item:
    #     :complexity: best case O(1), worst case O(N)
    #     :return: self
    #     '''
    #     try:
    #         assert 0 <= index < self.count or -self.count <= index <= 0, "index out of range"
    #         if index < 0:
    #             index = self.count + index
    #         if index == 0:
    #             self.head = Node(item, self.head)
    #         else:
    #             node = self.__getitem__(index - 1)
    #             node.next = Node(str(item), node.next)
    #         self.count += 1
    #     except AssertionError:
    #         print("Enter a valid number within range")
    #     except ValueError:
    #         print("Enter a correct value")
    #     except TypeError:
    #         print("Enter a correct integer for index")

    def insert(self, item):
        new = self.head
        if self.is_full():
            return False
        if self.count == 0:
            self.head = Node(item)
        elif self.count > 0:
            while new.item < item:
                new = new.next
            nex = Node(item)



    def append(self, item):
        if self.count > 0:
            node = self.__getitem__(self.count - 1)
            node.next = Node(str(item))
        elif self.count == 0:
            self.head = Node(str(item))
        self.count += 1

    def delete(self, index):
        '''

        :param index:
        :return: True
        :complexity: best case O(1) worst case O(N)
        '''
        try:
            if not self._is_empty():
                assert 0 <= index < self.count or -self.count <= index <= 0, "index out of range"
                if index < 0:
                    index = self.count + index
                if index == 0:
                    # if position at the start of the list
                    self.head = self.head.next
                elif index == self.count - 1:
                    # if the last element in the list
                    node = self.__getitem__(self.count - 2)
                    node.next = None
                else:
                    # anything in betwwen
                    node = self.__getitem__(index - 1)
                    node.next = node.next.next
                self.count -= 1
                return True

        except AssertionError:
            print("Index out of range")
        except TypeError:
            print("Enter a string")

    def remove(self, item):
        '''

        :param item:
        :return: True
        :complexity: worst case O(N**2) best case O(N)
        '''
        try:
            for i in range(len(self)):
                if str(self[i]) == str(item):
                    self.delete(i)
            return True
        except ValueError:
            return ValueError

    def __str__(self):
        '''
                returns a string representation
                :return: representation
                :complexity: O(N)
        '''
        representation = ""
        for i in range(len(self)):
            representation += str(self[i]) + "\n"
        return representation

    # sort the list
    def sort(self, reverse=False):
        '''
        Sort the list using bubble sort, reverse order if reverse=True
        :param reverse:
        :return: True
        :complexity: best case O(N), worst case O(N**2)
        '''
        if not self._is_empty():
            try:
                assert (reverse is True or reverse is False), "Invalid boolean parameter"
                swapped = False
                for i in range(self.count - 1, 0, -1):
                    for j in range(i):
                        if reverse is False:
                            comparison = str(self[j]) < str(self[j + 1])
                        elif reverse is True:
                            comparison = str(self[j]) > str(self[j + 1])
                        if comparison:
                            t = str(self[j + 1])
                            self[j + 1] = str(self[j])
                            self[j] = t
                            swapped = True
                    if not swapped:
                        break
                return True
            except AssertionError:
                print("Invalid boolean parameter")

    def search(self, item):
        '''
        searches for an element in a list
        :param item:
        :return: i or -1
        :complexity: best case O(1), worst case O(N)
        '''

        if not self._is_empty():
            for i in range(self.count):
                temp = str(self[i])
                # we need to strip punctuation mark
                temp = temp.strip(',')
                temp = temp.strip("'")
                temp = temp.strip(".")
                temp = temp.strip("-")
                temp = temp.lower()
                item = str(item)
                item = item.lower()
                item1 = " " + item + " "
                item2 = item + " "
                # its either in the middle beginning or end
                if (item1 in temp) or (item2 in temp) or item in temp:
                    return i
        return -1


if __name__ == "__main__":
    n = List()
    n.append(3)
    n.append(6)
    n.insert(1, 100)
    n.delete(0)
    n.remove(3)
    n.append(12)
    n.remove(6)
    n.sort()
