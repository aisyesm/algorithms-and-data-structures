class DoublyLinkedBase:
    '''A base class for providing a doubly linked list representation.'''

    class _Node:
        '''Lightweight, nonpublic class for storying a doubly linked node.'''
        __slots__ = '_element', '_prev', '_next'    # streamline memory

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0                              # number of elements

    def __len__(self):
        return self._size

    def _insert_between(self, e, pred, succ):
        '''Add element e between two existing nodes and return new node.'''
        newest = self._Node(e, pred, succ)          # linked to its neighbours
        pred._next = newest
        succ._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        '''Delete nonessential node from the list and return its element'''
        pred = node._prev
        succ = node._next
        pred._next = succ
        succ._prev = pred
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None      # depreciate node
        return element