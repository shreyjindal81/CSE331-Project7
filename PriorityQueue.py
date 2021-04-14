"""
Shrey Jindal
Project 5 - PriorityHeaps - Solution Code
CSE 331 Fall 2020
Dr. Sebnem Onsay
"""

from typing import List, Any
from Project7.PriorityNode import PriorityNode, MaxNode, MinNode


class PriorityQueue:
    """
    Implementation of a priority queue - the highest/lowest priority elements
    are at the front (root). Can act as a min or max-heap.
    """

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   DO NOT MODIFY the following attributes/functions
    #   Modify only below indicated line
    __slots__ = ["_data", "_is_min"]

    def __init__(self, is_min: bool = True):
        """
        Constructs the priority queue
        :param is_min: If the priority queue acts as a priority min or max-heap.
        """
        self._data = []
        self._is_min = is_min

    def __str__(self) -> str:
        """
        Represents the priority queue as a string
        :return: string representation of the heap
        """
        return F"PriorityQueue [{', '.join(str(item) for item in self._data)}]"

    __repr__ = __str__

    def to_tree_str(self) -> str:
        """
        Generates string representation of heap in Breadth First Ordering Format
        :return: String to print
        """
        string = ""

        # level spacing - init
        nodes_on_level = 0
        level_limit = 1
        spaces = 10 * int(1 + len(self))

        for i in range(len(self)):
            space = spaces // level_limit
            # determine spacing

            # add node to str and add spacing
            string += str(self._data[i]).center(space, ' ')

            # check if moving to next level
            nodes_on_level += 1
            if nodes_on_level == level_limit:
                string += '\n'
                level_limit *= 2
                nodes_on_level = 0
            i += 1

        return string

    def is_min_heap(self) -> bool:
        """
        Check if priority queue is a min or a max-heap
        :return: True if min-heap, False if max-heap
        """
        return self._is_min

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line
    def __len__(self) -> int:
        """
        finds total elements in the queue
        :return: integer value of total elements
        """
        return len(self._data)

    def empty(self) -> bool:
        """
        tells if queue is empty
        :return: bool indicating emptiness
        """
        return len(self._data) == 0

    def peek(self) -> PriorityNode:
        """
        get root value if present
        :return: root node if present else none
        """
        return self._data[0] if len(self) != 0 else None

    def get_left_child_index(self, index: int) -> int:
        """
        gets the index of the left child
        :param index: the parent index
        :return: the child index
        """
        return 2*index+1 if len(self) > 2*index+1 else None

    def get_right_child_index(self, index: int) -> int:
        """
        gets the index of the right child
        :param index: the parent index
        :return: the child index
        """
        return 2*index+2 if len(self) > 2*index+2 else None


    def get_parent_index(self, index: int) -> int:
        """
        gets the index of the parent
        :param index: the child index
        :return: the parent index
        """
        return (index - 1)//2 if index != 0 else None

    def push(self, priority: Any, val: Any) -> None:
        """
        TODO
        :param priority:
        :param val:
        :return:
        """
        if self._is_min:
            self._data.append(MinNode(priority, val))
        else:
            self._data.append(MaxNode(priority, val))

        self.percolate_up(len(self._data)-1)

    def pop(self) -> PriorityNode:
        """
        return the root node
        :return: the root node
        """
        if self.empty():
            return None
        self._data[0], self._data[len(self)-1] = self._data[len(self)-1], self._data[0]
        final = self._data.pop()
        self.percolate_down(0)
        return final

    def get_minmax_child_index(self, index: int) -> int:
        """
        get min or max of the 2 children based on type of node
        :param index: the parent index
        :return: the favored child index
        """
        left = self.get_left_child_index(index)
        right = self.get_right_child_index(index)
        if left is None:
            return None
        if right is None:
            return left
        if self._data[left] > self._data[right]:
            return right
        return left


    def percolate_up(self, index: int) -> None:
        """
        percolate upwards
        :param index: the index to percolate
        :return: none
        """
        if index >= len(self):
            return
        pi = self.get_parent_index(index)
        if pi is not None and self._data[index] < self._data[pi]:
            self._data[pi],self._data[index] = self._data[index], self._data[pi]
            self.percolate_up(pi)

    def percolate_down(self, index: int) -> None:
        """
        percolate downwards
        :param index: the index to percolate
        :return: none
        """
        child = self.get_minmax_child_index(index)
        if child is None:
            return
        if self._data[child] < self._data[index]:
            self._data[child], self._data[index] = self._data[index], self._data[child]
            self.percolate_down(child)


class MaxHeap:
    """
    Implementation of a max-heap - the highest value is at the front (root).

    Initializes a PriorityQueue with is_min set to False.

    Uses the priority queue to satisfy the min heap properties by initializing
    the priority queue as a max-heap, and then using value as both the priority
    and value.
    """

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   DO NOT MODIFY the following attributes/functions
    #   Modify only below indicated line

    __slots__ = ['_pqueue']

    def __init__(self):
        """
        Constructs a priority queue as a max-heap
        """
        self._pqueue = PriorityQueue(False)

    def __str__(self) -> str:
        """
        Represents the max-heap as a string
        :return: string representation of the heap
        """
        # NOTE: This hides implementation details
        return F"MaxHeap [{', '.join(item.value for item in self._pqueue._data)}]"

    __repr__ = __str__

    def to_tree_str(self) -> str:
        """
        Generates string representation of heap in Breadth First Ordering Format
        :return: String to print
        """
        return self._pqueue.to_tree_str()

    def __len__(self) -> int:
        """
        Determine the amount of nodes on the heap
        :return: Length of the data inside the heap
        """
        return len(self._pqueue)

    def empty(self) -> bool:
        """
        Checks if the heap is empty
        :returns: True if empty, else False
        """
        return self._pqueue.empty()

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line
    def peek(self) -> Any:
        """
        get root value
        :return: value of root
        """
        return self._pqueue.peek().value

    def push(self, val: Any) -> None:
        """
        push value to heap
        :param val: the value to push
        :return: none
        """
        self._pqueue.push(val, val)

    def pop(self) -> Any:
        """
        pop root from heap
        :return: value of root
        """
        return self._pqueue.pop().value if self._pqueue.peek() else None


class MinHeap(MaxHeap):
    """
    Implementation of a max-heap - the highest value is at the front (root).

    Initializes a PriorityQueue with is_min set to True.

    Inherits from MaxHeap because it uses the same exact functions, but instead
    has a priority queue with a min-heap.
    """

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   DO NOT MODIFY the following attributes/functions
    __slots__ = []

    def __init__(self):
        """
        Constructs a priority queue as a min-heap
        """
        super().__init__()
        self._pqueue._is_min = True


def heap_sort(array: List[Any]) -> None:
    """
    implement heap sort
    :param array: the array to sort
    :return:  nothing
    """
    heap = MaxHeap()
    for element in array:
        heap.push(element)

    i = len(heap) - 1
    while not heap.empty():
        array[i] = heap.pop()
        i -= 1


def current_medians(array: List[int]) -> List[int]:
    """
    take list of int and return list of median of ints till that point
    :param array: the input list
    :return: list of medians
    """
    s = PriorityQueue(False)
    g = PriorityQueue(True)
    if len(array) == 0:
        return []
    mid = array[0]
    s.push(mid, mid)
    final = list()
    final.append(mid)
    for i in range(1, len(array)):
        x = array[i]
        if len(s) > len(g):
            if x < mid:
                g.push(s.peek().priority, s.peek().priority)
                s.pop()
                s.push(x, x)
            else:
                g.push(x, x)
            mid = (s.peek().priority+g.peek().priority)/2
        elif len(s) < len(g):
            if x > mid:
                s.push(g.peek().priority, g.peek().priority)
                g.pop()
                g.push(x, x)
            else:
                s.push(x, x)
            mid = (s.peek().priority+g.peek().priority)/2.0
        else:
            if x < mid:
                s.push(x, x)
                mid = s.peek().priority
            else:
                g.push(x, x)
                mid = g.peek().priority
        final.append(mid)
    return final
