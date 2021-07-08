# BST Breadth-First Traversal Modification 😷🌳

Binary Search Tree *Post-Order* traversal using Breadth-First Traversal.

Pre-Order traverses from: *Left Child -> Right Child -> Parent*

Instead of a typical a depth-first traversal, where it traverses each path in-terms of depth, this algorithm traverses laterally. As the algorithm traverses, it also adds the nodes to a Queue (uses an array as an underlying data structure where all the nodes are initially placed when traversed), which is the underlying data structure for a typical breadth-first algorithm. Moreover, there are three cases where the algorithm may add a node(s) to the underlying array, which then will be added to the Queue:
   
   1) If both the current node's *right path* and *left path* are `None`, then `pass`
   2) If the current node's *right path* is `None`, add the node in the left path to the Queue
   3) If the current node's *left path* is `None`, add the node in the right path to the Queue
  
 If none of these cases are met, both nodes in both paths are added to the Queue in order of *right to left*. 
 
 What makes this algorithm a *Post-Order* traversal is the fact that we first add the left child and right child to the array, then the parent. On average, the parent node is always indexed *two more* compared to the *left child* and *one more* compared to the *right child*. This arrangement can be represented by the index expressions for typical `Heap` structures for both parent and child nodes:
 
  - `parent_idx = idx // 2`
  - `left_child_idx = idx * 2`
  - `right_child_idx = idx * 2 + 1`

 Time Complexity: `O(n)` (Matches typical Breadth-First algorithms and Depth-First Traversal. 
 
 # More Information
 
 `Queue.py` is the file where the underlying *Queue* Data Structure is used
 
 Made in Python 🐍
