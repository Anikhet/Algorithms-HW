"""
CSCI-603: Trees (week 10)
Author: Sean Strout @ RIT CS

This is an implementation of a binary tree node.
"""
from typing import Any


class BTNode:
    """
    A binary tree node contains:
     :slot val: A user defined value
     :slot left: A left child (BTNode or None)
     :slot right: A right child (BTNode or None)
    """
    __slots__ = 'val', 'left', 'right'
    val: Any
    left: 'BTNode'
    right: 'BTNode'

    def __init__(self, val: Any, left: 'BTNode' = None, right: 'BTNode' = None) -> None:
        """
        Initialize a node.
        :param val: The value to store in the node
        :param left: The left child (BTNode or None)
        :param right: The right child (BTNode or None)
        :return: None
        """
        self.val = val
        self.left = left
        self.right = right


def testBTNode() -> None:
    """
    A test function for BTNode.
    :return: None
    """
    left = BTNode(10)
    right = BTNode(20)
    parent = BTNode(30)
    parent.left = left
    parent.right = right
    print('parent (30):', parent.val)
    print('left (10):', parent.left.val)
    print('right (20):', parent.right.val)


if __name__ == '__main__':
    testBTNode()



class BST:
    """
    A binary search tree.
    """
    __slots__ = 'root', 'size'
    root: BTNode
    size: int

    def __init__(self) -> None:
        """
        Initialize the tree.
        :return: None
        """
        self.root = None
        self.size = 0

    def __insert(self, val: int, node: BTNode) -> None:
        """
        The recursive helper function for inserting a new value into the tree.
        :param val: The value to insert
        :param node: The current node in the tree (BTNode)
        :return: None
        """
        if val < node.val:                     # check if need to go left
            if node.left == None:              # if no left child
                node.left = BTNode(val)        # insert it here
            else:                              # otherwise 
                self.__insert(val, node.left)  # traverse with the left node
        else:                                  # need to go right
            if node.right == None:             # if no right child
                node.right = BTNode(val)       # insert it here                               
            else:                              # otherwise 
                self.__insert(val, node.right) # traverse with the right node

    def insert(self, val: int) -> None:
        """
        Insert a new value into the tree
        :param val: The value to insert
        :return: None
        """   
        if self.root == None:              # if tree is empty
            self.root = BTNode(val)        # create root node with the value
        else:                              # otherwise
            self.__insert(val, self.root)  # call helper function with root
        self.size += 1

    def __contains(self, val: int, node: BTNode) -> bool:
        """
        The recursive helper function for checking if a value is in the tree.
        :param val: The value to search for
        :param node: The current node (BTNode)
        :return: True if val is present, False otherwise
        """
        if node == None:      # if there is no node 
            return False      # we went past a leaf and the val is not there
        elif val == node.val: # if the values match
            return True       # return success
        elif val < node.val:  # if no match, but val is lesser
            return self.__contains(val, node.left)  # recurse with left node
        else:                 # otherwise
            return self.__contains(val, node.right) # recurse with right node

    def contains(self, val: int) -> bool:
        """
        Returns whether a value is in the tree or not.
        :param val: The value to search for
        :return: True if val is present, False otherwise
        """
        # call the recursive helper function with the root node
        return self.__contains(val, self.root)

    

