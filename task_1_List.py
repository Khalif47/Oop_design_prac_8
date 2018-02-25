from referential_array import build_array


class List:
    # instantiate an object
    # initialize an array with maximum as a parameter
    def __init__(self, maximum):  # initialise base size to 20
        '''
        Initialises a list for us of chosen size
        :complexity: O(n)
        '''
        # assert maximum > 0, "Enter a valid number"
        self.max = abs(maximum)
        self.array = build_array(abs(maximum))
        self.count = 0

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
        :complexity: best case O(N) worst case O(N)
        '''
        if not self.is_empty():
            for i in range(len(self.array)):
                if str(self.array[i]) == str(item):
                    return True
            return False

    def __getitem__(self, index):
        '''

        :param index:
        :return: self.array[index]
        :complexity: O(1)
        '''
        try:
            return self.array[index]
        except IndexError:
            print("Enter a valid index within range.")
        except TypeError:
            print("Enter an integer")
        return

    def __setitem__(self, index, item):
        '''

        :param index:
        :param item:
        :return: self.array[index]
        :complexity: O(1)
        '''
        try:
            self.array[index] = item
            return self.array[index]
        except IndexError:
            print("Enter a valid number within range.")
        except TypeError:
            print("Enter an integer")

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
        :complexity: worst case O(N), best case O(1)
        '''
        # check if we need resizing
        # whenever appending and deleting this must be added
        if self.count < self.max:
            self.array[self.count] = str(item)
            self.count += 1
            return self
        else:
            print("List is full")

    def insert(self, index, item):
        '''
        inserts an element in the correct position at the correct index and shifts everything after that up by 1 index
        :param index:
        :param item:
        :return: self
        '''
        # assert 0 < index <= self.count or -self.count < index < 0, 'Index out of range'
        # have to deal with negatives
        # wrapping around
        try:
            if index < 0:
                index = self.count + index
            for i in range(self.count - 1, index - 1, -1):
                self.array[i + 1] = self.array[i]
            self.array[index] = str(item)
            self.count += 1
            return self
        except IndexError:
            print("Enter a valid number within range")
        except ValueError:
            print("Enter a correct value")

    def delete(self, index):
        '''

        :param index:
        :return: True
        :complexity: best case O(N) worst case O(N)
        '''
        assert 0 <= index < self.count or -self.count <= index <= 0, "index out of range"
        if index < 0:
            index = index = self.count + index
            for i in range(index, self.count - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.count] = None  # reinitializing empty value back to None
            self.count -= 1
            # at the end just check if resize possible
            return True
        else:
            for i in range(index, self.count - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.count - 1] = None
            self.count -= 1
            # at the end just check if resize possible
            return True

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
            return print("")

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
        Sort the list using bubble sort, reverse order if reverse=Truen\
        we need to raise exception if it is not True or False
        :param reverse:
        :param reverse, self :
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
                            comparison = int(self.array[j]) > int(self.array[j + 1])
                        elif reverse is True:
                            comparison = int(self.array[j]) < int(self.array[j + 1])
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



