"""
First the Node class needs to be created because every item in a linked list
is a node item containing the data and the pointer to the node it links to
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None


"""
Next the linked list can be created and initialized with the head as none 
because it doesn't exist yet and the number of nodes to 0 because its empty
"""


class LinkedList:

    def __init__(self):
        self.head = None
        self.numOfNodes = 0

        """
        Functions for the LinkedList class:
        """

    # function to insert a new node at the beginning of the list O(1)
    def insert_start(self, data):

        # first increase the number of nodes by 1
        self.numOfNodes = self.numOfNodes + 1
        # then insert the data into the new node
        new_node = Node(data)

        # check to see if there is a head
        if not self.head:
            # if not create it with the new node
            self.head = new_node
        # if there is a head
        else:
            # set the pointer of the new node to the old head
            new_node.nextNode = self.head
            # set the new node as the new head of the list
            self.head = new_node

    # function to insert a new node at the end of the list O(N)
    def insert_end(self, data):

        # first increase the number of nodes by 1
        self.numOfNodes = self.numOfNodes + 1
        # then insert the data into the new node
        new_node = Node(data)

        # get a reference to the head node to begin iteration
        actual_node = self.head

        # iterate the node looking for the node that points to Null
        while actual_node.nextNode is not None:
            # if not the last node pointing to Null
            # change active_node to the next node its pointing to
            actual_node = actual_node.nextNode

        # when we find the node that is pointing to Null
        # change its pointer to point to the new node
        actual_node.nextNode = new_node

    # function to get the size of the linked list
    def size_of_list(self):
        # return the number of nodes the list contains
        return self.numOfNodes

    # function to traverse the linked list and print all of its nodes data
    def traverse(self):

        # set the reference to the first node
        actual_node = self.head

        # iterate the list while the referenced node is not Null
        while actual_node is not None:
            # print out the actual_node data value
            print(actual_node.data)
            # move the reference to the next node in the list
            actual_node = actual_node.nextNode


"""
use the functions just created
"""
# create a new LinkedList
linked_list = LinkedList()
# insert a few nodes at the beginning of the list O(1)
linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_start(7)
# insert a node at the end of the list O(N)
linked_list.insert_end(10)
# print the node values of the list O(N)
linked_list.traverse()













