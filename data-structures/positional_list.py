from doubly_linked_list import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    '''A sequential container of elements allowing positional access.'''

    class Position:
        '''An abstraction representing the location of a single element.'''

        def __init__(self, container, node):
            '''Constructor should not be invoked by the user.'''
            self._container = container
            self._node = node

        def element(self):
            '''Return an element stored at this Position.'''
            return self._node._element

        def __eq__(self, other):
            '''Return True if other is a Position representing the same location.'''
            return type(other) is type(self) and other._node is self._node

        def __nq__(self, other):
            '''Return True if other does not represent the same location.'''
            return not (self == other)
    
    #---------------------- utility methods --------------------------
    def _validate(self, p):
        '''Return position's node, or raise appropriate error if invalid'''
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p._node is None:     # convetion for depresiated nodes
            raise ValueError('p is no longer valid.')
        return p._node

    def _make_position(self, node):
        '''Return Position instance for a given Node (or None if sentinel).'''
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    #-------------------------- accessors -----------------------------
    def first(self):
        '''Return the first Postion in the list (or None if the list is empty.)'''
        return self._make_position(self._header._next)

    def last(self):
        '''Return the last Postion in the list (or None if the list is empty.)'''
        return self._make_position(self._trailer._prev)

    def before(self, p):
        '''Return Postion just before the p (or None if p is first.)'''
        node = self._validate(p)
        return self._make_position(self.node._prev)

    def after(self, p):
        '''Return Postion just after the p (or None if p is last.)'''
        node = self._validate(p)
        return self._make_position(self.node._next)

    def __iter__(self):
        '''Generate forward iteration of the elements of the list.'''
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #-------------------------- mutators -----------------------------
    # override inherited version to return Position, rather than node
    def _insert_between(self, e, pred, succ):
        '''Add element between two nodes and return Position.'''
        node = super()._insert_between(e, pred, succ)
        self._make_position(node)

    def add_first(self, e):
        '''Insert element e at the front of the list and return Position.'''
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        '''Insert element e at the back of the list and return Position.'''
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        '''Insert element before position p and return new Position'''
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        '''Insert element after position p and return new Position'''
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        '''Remove and return the element at position p.'''
        original = self._validate(p)
        return self._delete_node(original)      #inherited method

    def replace(self, p, e):
        '''Replace the element at Position p with e.
        
        Return the element formely at Position p.
        '''
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value