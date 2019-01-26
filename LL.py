""" Node and LinkedList classes """


class LinkedListNode:
    """
    Node to be used in linked list

    === Attributes ===
    @param LinkedListNode next_: successor to this LinkedListNode
    @param object value: data this LinkedListNode represents
    """

    def __init__(self, value, next_=None):
        """
        Create LinkedListNode self with data value and successor next_.

        @param LinkedListNode self: this LinkedListNode
        @param object value: data of this linked list node
        @param LinkedListNode|None next_: successor to this LinkedListNode.
        @rtype: None
        """
        self.value = value
        self.next_ = next_

    def __str__(self):
        """
        Return a user-friendly representation of this LinkedListNode.

        @param LinkedListNode self: this LinkedListNode
        @rtype: str

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """

        result = '{} ->'.format(self.value)
        current = self
        while current is not None:
            if current.next_ is None:
                result += '|'
            else:
                result += ' {} ->'.format(current.next_.value)
            current = current.next_
        return result

    def __eq__(self, other):
        """
        Return whether LinkedListNode self is equivalent to other.

        @param LinkedListNode self: this LinkedListNode
        @param LinkedListNode|object other: object to compare to self.
        @rtype: bool

        >>> LinkedListNode(5).__eq__(5)
        False
        >>> n1 = LinkedListNode(5, LinkedListNode(7))
        >>> n2 = LinkedListNode(5, LinkedListNode(7, None))
        >>> n1.__eq__(n2)
        True
        """
        # we'll say 2 nodes are equal if the linked lists
        # beginning at those nodes are also equal
        self_node = self
        other_node = other
        while (self_node is not None
               and other_node is not None
               and type(self_node) == type(other_node)
               and self_node.value == other_node.value):
            # self_node.next_ == other_node.next_ is a recursive call here
            self_node = self_node.next_
            other_node = other_node.next_

        # return True if we reached the end of both lists
        # and False otherwise
        return self_node is None and other_node is None


class LinkedList:
    """
    Collection of LinkedListNodes

    === Attributes ==
    @param: LinkedListNode front: first node of this LinkedList
    @param LinkedListNode back: last node of this LinkedList
    @param int size: number of nodes in this LinkedList
                        a non-negative integer
    """

    def __init__(self):
        """
        Create an empty linked list.

        @param LinkedList self: this LinkedList
        @rtype: None
        """
        self.front = None
        self.back = None
        self.size = 0

    def __str__(self):
        """
        Return a human-friendly string representation of
        LinkedList self.

        @param LinkedList self: this LinkedList

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> print(lnk)
        5 ->|
        """
        return str(self.front)

    def __eq__(self, other):
        """
        Return whether LinkedList self is equivalent to
        other.

        @param LinkedList self: this LinkedList
        @param LinkedList|object other: object to compare to self
        @rtype: bool

        >>> LinkedList().__eq__(None)
        False
        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(5)
        >>> lnk.__eq__(lnk2)
        True
        """
        return (type(self) == type(other) and
                self.front == other.front)

    def append(self, value):
        """
        Insert a new LinkedListNode with value after self.back.

        @param LinkedList self: this LinkedList.
        @param object value: value of new LinkedListNode
        @rtype: None

        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> lnk.size
        1
        >>> print(lnk.front)
        5 ->|
        >>> lnk.append(6)
        >>> lnk.size
        2
        >>> print(lnk.front)
        5 -> 6 ->|
        """
        assert ((self.front is None and self.back is None) or
                (self.front is not None and self.back is not None))
        new_node = LinkedListNode(value)
        if self.front is None:
            self.front = new_node
        else:
            self.back.next_ = new_node
        self.back = new_node
        self.size += 1

    def prepend(self, value):
        """
        Insert value before LinkedList self.front.

        @param LinkedList self: this LinkedList
        @param object value: value for new LinkedList.front
        @rtype: None

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> str(lnk.front)
        '2 -> 1 -> 0 ->|'
        >>> lnk.size
        3
        """
        # create a new node
        # set its next to be current front
        # update current front to new node
        self.front = LinkedListNode(value, self.front)
        self.size += 1
        if self.back is None:
            # ie empty list
            self.back = self.front

    def delete_front(self):
        """
        Delete LinkedListNode self.front from self.

        Assume self.front is not None

        @param LinkedList self: this LinkedList
        @rtype: None

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.delete_front()
        >>> str(lnk.front)
        '1 -> 0 ->|'
        >>> lnk.size
        2
        >>> lnk.delete_front()
        >>> lnk.delete_front()
        >>> str(lnk.front)
        'None'
        """
        assert self.size > 0, 'cannot delete from empty list'
        # make the second node the front
        # decrement size
        # maybe update back
        if self.front is self.back:
            self.back = None
        self.front = self.front.next_
        self.size -= 1

    def __getitem__(self, index):
        """
        Return the value at LinkedList self's position index.

        @param LinkedList self: this LinkedList
        @param int index: position to retrieve value from
        @rtype: object

        >>> lnk = LinkedList()
        >>> lnk.prepend(1)
        >>> lnk.prepend(0)
        >>> lnk.__getitem__(1)
        1
        >>> lnk[-1]
        1
        """
        if index < 0:
            index += self.size
        if index >= self.size or self.size == 0 or index < 0:
            raise IndexError('invalid index')
        current = self.front
        for __ in range(index):
            current = current.next_
            assert current is not None, 'reached invalid index'
        return current.value

    def __contains__(self, value):
        """
        Return whether LinkedList self contains value.

        @param LinkedList self: this LinkedList.
        @param object value: value to search for in self
        @rtype: bool

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.__contains__(1)
        True
        >>> 1 in lnk
        True
        >>> lnk.__contains__(3)
        False
        """
        # start at the beginning of the list
        # check every item
        # if you find a match, return True
        # if we get to the end, return False

        current = self.front
        while current is not None:
            if current.value == value:
                return True
            current = current.next_
        return False

    def __reversed__(self):

        cur = self.front
        self.back = cur
        nxt = cur.next_
        prev = None
        while cur is not None:
            cur.next_ = prev
            prev = cur
            cur = nxt
            if nxt:
                nxt = cur.next_
        self.front = prev


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    lnk = LinkedList()
    lnk.prepend(0)
    lnk.prepend(1)
    lnk.prepend(2)
    print(lnk)
    lnk.__reversed__()
    print(lnk)



