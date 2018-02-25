from referential_array import build_array


class List:
    # instantiate an object
    # initialize an array with maximum as a parameter
    def __init__(self):  # initialise base size to 20
        '''
        Initialises a list for us of chosen size
        :complexity: O(N)
        '''
        # assert maximum > 0, "Enter a valid number"
        self.array = build_array(20)
        self.count = 0
        self.max = 20

    def __len__(self):
        '''
        Finds the length of the list
        :return: self.count
        :complexity: O(1)
        '''
        return self.count

    def is_empty(self):
        '''
        Checks if the list is empty
        :precondition: a valid list
        :return: self.count
        :complexity: O(1)
        '''
        return self.count == 0

    def _is_full(self):
        '''
        Checks if list is full
        :return: True/ false
        :complexity: O(1)
        '''
        return self.count >= len(self.array)

    def __contains__(self, item):
        '''

        :param item:
        :return: True/ False
        :complexity: best case O(1) worst case O(N)
        '''
        if not self.is_empty():
            for i in range(len(self.array)):
                if self.array[i] == str(item):
                    return True
            return False

    def __getitem__(self, index):
        '''

        :param index:
        :return: self.array[index]
        :complexity: O(1)
        '''
        try:
            assert 0 <= index < self.count or -self.count <= index <= 0, "Index out of range"
            if index < 0:
                index = self.count + index
            return self.array[index]
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
        :complexity: O(1)
        '''
        try:
            self.array[index] = str(item)
            return self.array[index]
        except AssertionError:
            print("index out of range")
        except IndexError:
            print("Enter a valid number within range.")
        except TypeError:
            print("Enter an integer as your index")

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
                    if str(self.array[i]) != str(other[i]):
                        return False
                return True
            return False
        except TypeError:
            print("Compare a valid List")

    def append(self, item):
        '''
        appends an item into the list
        :param item:
        :return: self
        :complexity: worst case O(N)
        '''
        # check if we need resizing
        # whenever appending and deleting this must be added
        self.resize()
        try:
            self.array[self.count] = str(item)
            self.count += 1
            return self
        except IndexError:
            return IndexError

    def insert(self, index, item):
        '''
        inserts an element in the correct position at the correct index and shifts everything after that up by 1 index
        :param index:
        :param item:
        :return: self
        '''
        try:
            assert 0 <= index < self.count or -self.count <= index <= 0, "index out of range"
            self.resize()
            if index < 0:
                index = self.count + index
            for i in range(self.count - 1, index - 1, -1):
                self.array[i + 1] = self.array[i]
            self.array[index] = str(item)
            self.count += 1
            return self
        except AssertionError:
            print("Enter a valid number within range")
        except ValueError:
            print("Enter a correct value")
        except TypeError:
            print("Enter a correct integer for index")

    def delete(self, index):
        '''

        :param index:
        :return: True
        :complexity: best case O(1) worst case O(N)
        '''
        try:
            assert 0 <= index < self.count or -self.count <= index <= 0, "index out of range"
            if index < 0:
                index = self.count + index
            for i in range(index, self.count - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.count] = None  # reinitializing empty value back to None
            self.count -= 1
            # at the end just check if resize possible
            self.resize()
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
                if self.array[i] == str(item):
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
        for i in range(self.count):
            representation += str(self.array[i]) + "\n"
        return representation

    # sorting method
    def sort(self, reverse=False):
        '''
        Sort the list using bubble sort, reverse order if reverse=True
        :param reverse:
        :return: True
        :complexity: best case O(N), worst case O(N**2)
        '''
        if not self.is_empty():
            try:
                assert (reverse is True or reverse is False), "Invalid boolean parameter"
                swapped = False
                for i in range(self.count - 1, 0, -1):
                    for j in range(i):
                        if reverse is False:
                            comparison = self.array[j] > self.array[j + 1]
                        elif reverse is True:
                            comparison = self.array[j] < self.array[j + 1]
                        if comparison:
                            t = self.array[j + 1]
                            self.array[j + 1] = self.array[j]
                            self.array[j] = t
                            swapped = True
                    if not swapped:
                        break
                return True
            except AssertionError:
                print("Invalid boolean parameter")

    # resize to two times if it is full
    # resize to half if it occupies 1/8 of max array and is bigger than the base array
    # call this methods when appending
    def resize(self):
        '''
        Resizing a list if
        :return: self.max
        :complexity: best case O(1) worst case O(N)
        '''
        if self._is_full():
            temp = self.array
            self.max = self.max * 2
            self.array = build_array(self.max)
            # Now copy values in
            for i in range(self.count):
                self.array[i] = temp[i]
        elif 20 < self.count < int((1 / 8) * self.max):
            temp = self.array
            self.max = self.max // 2
            self.array = build_array(self.max)
            # Now copy values in
            for i in range(self.count):
                self.array[i] = temp[i]
        return self.max

    # work on this
    def search(self, item):
        '''
        searches for an element in a list
        :param item:
        :return: i or -1
        :complexity: best case O(1), worst case O(N)
        '''

        if not self.is_empty():
            for i in range(len(self.array)):
                temp = str(self.array[i])
                # we need to strip punctuation mark
                temp = temp.strip(',')
                temp = temp.strip("'")
                temp = temp.strip(".")
                temp = temp.strip("-")
                temp = temp.lower()
                item = item.lower()
                item1 = " "+item+" "
                item2 = item+" "
                # its either in the middle beginning or end
                if (item1 in temp) or (item2 in temp) or item in temp:
                    return i
        return -1
