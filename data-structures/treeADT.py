class Tree:
    """Abstract Base Class representing a Tree structure."""

    #-------------------- nested Position class -------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return an element stored at this position."""
            raise NotImplementedError('must be implemented by sublass')

        def __eq__(self, o: object) -> bool:
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by sublass')

        def __ne__(self, o: object) -> bool:
            """Return True if other Position does not represent the same location."""
            return not (self == o)

    #------------ abstract methods that concrete subclass must support -----------
    def root(self):
        """Return Position representing the tree's root (None if empty)."""
        raise NotImplementedError('must be implemented by sublass')

    def parent(self, p):
        """Return Position representing p's parent (None if p is root)."""
        raise NotImplementedError('must be implemented by sublass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by sublass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by sublass')
    
    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by sublass')

    #------------ concrete methods implemented in this class -----------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if tree is empty."""
        return len(self) == 0

    #------------------------- tree traversals --------------------------
    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():      # use same order as in positions
            yield p.element()

    def positions(self):
        """Generate an iteration of tree's positions."""
        return self.preorder()

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):   # start recursion
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p                                             # visit p before its subtrees
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

