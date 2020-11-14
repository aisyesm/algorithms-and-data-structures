import empty

class ArrayStack:
    '''LIFO Stack implementation using a Python list as underlying storage.'''

    def __init__(self):
        '''Create an empty stack.'''
        self._data = []                     # nonpublic list instance
        self._min_stack = []                 # keeps track of min value of the stack

    def __len__(self):
        '''Return the number of elements in the stack.'''
        return len(self._data)

    def is_empty(self):
        '''Return True if stack is empty.'''
        return len(self._data) == 0

    def push(self, e):
        '''Add element e to the top of the stack.'''
        self._data.append(e)
        print("Pushed {} onto the stack!".format(e))
        if not self._min_stack or self._min_stack[-1] >= e:
            self._min_stack.append(e)

    def top(self):
        '''Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        '''
        if self.is_empty():
            raise empty.Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        '''Return and remove the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        '''
        if self.is_empty():
            raise empty.Empty('Stack is empty')
        print("Removed {} from the stack!".format(self.top()))
        if self.top() == self._min_stack[-1]:
            self._min_stack.pop()

        return self._data.pop()

    def min(self):
        if not self._min_stack:
            raise empty.Empty('Stack is empty')
        return self._min_stack[-1]


# Driver code
if __name__ == "__main__":
    S = ArrayStack()
    S.push(5)
    S.push(3)
    print("Length: {}".format(len(S)))
    print("Min: {}".format(S.min()))
    S.push(10)
    S.push(1)
    print("Length: {}".format(len(S)))
    print("Min: {}".format(S.min()))
    S.pop()
    print("Length: {}".format(len(S)))
    print("Min: {}".format(S.min()))
    S.push(3)
    S.push(3)
    print("Length: {}".format(len(S)))
    print("Min: {}".format(S.min()))
    S.pop()
    print("Length: {}".format(len(S)))
    print("Min: {}".format(S.min()))
    S.pop()
    print("Length: {}".format(len(S)))
    print("Min: {}".format(S.min()))
    S.pop()
    print("Length: {}".format(len(S)))
    print("Min: {}".format(S.min()))
    S.pop()
    print("Length: {}".format(len(S)))
    print("Min: {}".format(S.min()))
    S.pop()
    print("Stack is empty: {}".format(S.is_empty()))
