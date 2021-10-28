# Trees

## Challenge

Implement Binary Tree and BST

## Approach & Efficiency

## Requirements

1. Node

* [x] Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

2. Binary Tree

* [] Create a Binary Tree class
    - [] Define a method for each of the depth first traversals:
        * [] pre order
        * [] in order
        * [] post order which returns an array of the values, ordered appropriately.
* [] Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

3. Binary Search Tree

* [] Create a Binary Search Tree class
    - [] This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
    - [] Add
        * [] Arguments: value
        * [] Return: nothing
        * [] Adds a new node with that value in the correct location in the binary search tree.
    - [] Contains
        * [] Argument: value
        * [] Returns: boolean indicating whether or not the value is in the tree at least once.

## Test Requirements

* [] Can successfully instantiate an empty tree
* [] Can successfully instantiate a tree with a single root node
* [] Can successfully add a left child and right child to a single root node
* [] Can successfully return a collection from a preorder traversal
* [] Can successfully return a collection from an inorder traversal
* [] Can successfully return a collection from a postorder traversal
# White Board

![Trees](trees.jpg)