class LinkedListNode:
    def __init__(self, value: object = None) -> object:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, nodes_array: list = []) -> object:
        """
        Create Linked list
        """
        self.head: LinkedListNode = None
        self.tail: LinkedListNode = None

        if nodes_array:
            self.array_to_nodelist(nodes_array)

    def add_node_to_front(self, node: LinkedListNode):
        self.head = node

        if not self.tail:
            self.tail = node

    def add_node_to_end(self, node: LinkedListNode):
        if self.head:
            pass
        else:
            self.head = node

        if self.tail:
            pass
        else:
            self.tail = node

    @staticmethod
    def get_list(node: LinkedListNode = None):
        while node is not None:
            print(f"[{node.value}]")
            node = node.next

    def array_to_nodelist(self, values_array: list = []):
        for value in values_array:
            node = LinkedListNode(value)
            self.add_node_to_end(node)


linked_list = LinkedList([1])
linked_list.get_list()
