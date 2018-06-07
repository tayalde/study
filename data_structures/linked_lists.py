
class Node(object):
    """Holds datum and pointer for linked list.

    Unit that holds data and next_node pointer in linked lists.
    
    Attributes:
        _data: Any data type to be stored in the Node.
        _next_node: Node that follows the current one.
    """

    def __init__(self, data=None, next_node=None):
        """Inits Node with data and next_node."""
        self._data = data
        self._next_node = next_node

    def get_data(self):
        """Returns data held in node."""
        return self._data

    def get_next(self):
        """Returns the next node."""
        return self._next_node

    def set_data(self, new_data):
        """Changes node's data to new_data"""
        self._data = new_data

    def set_next(self, new_node):
        """Adds node to point to."""
        self._next_node = new_node


class LinkedList(object):
    """List of nodes, each containing data and a pointer to the next node.

    List of nodes from which you can insert new nodes at the _head of the list,
    get the size of the list, search for data within the list, and delete nodes
    containing specific data.

    Attributes:
        _head: Node at the very beginning of the list
    """

    def __init__(self, _head=None):
        """Inits LinkedList with _head, _head is None by default."""
        self._head = None

    def insert(self, data):
        """Inserts new node at _head of list."""
        new_node = Node(data)
        new_node.set_next(self._head)
        self._head = new_node

    def size(self):
        """Counts number of nodes in list, and returns size."""
        current = self._head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        """Searches for data in linked list, returns Node containing data."""
        current = self._head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data is not in list.")
        return current

    def delete(self, data):
        """Searches for data in linked list, deletes Node containing data."""
        current = self._head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data is not in list.")
        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

class DNode(Node):
    """Node for a doubly linked list, points to previous node as well.

    Refer to Node definition for more information.

    Attributes:
        _data: Any type of data
        _next_node: Next node contained in the same linked list
        _prev_node: Previous node contained in the same linked list
    """

    def __init__(self, data=None, next_node=None, prev_node=None):
        """Inits DNode by super-"ing" Node"""
        super().__init__(data, next_node)
        self._prev_node = prev_node

    def get_prev(self):
        """Getter for _prev_node"""
        return self._prev_node

    def set_prev(self, new_node):
        """Setter for _prev_node"""
        self._prev_node = new_node

