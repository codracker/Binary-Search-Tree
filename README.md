# Binary-Search-Tree
To check if a given binary tree is a subtree of another binary
To solve this , I have used two methods:

> isidentical: which checks if two roots are identical or not

>issubtree: which checks if one tree is a subtree of the other binary tree


To test the program 5 test cases are made:

1. **Input**  :  The root node of source is "None"
   **Output** : It is not a subtree

2. **Input** : If source.right.left is changed from 'm' to 'z'
   **Output** : It is not a subtree
   
3. **Input** :  If source.right = Node('g')
   **Output** : It is a subtree
   
4. **Input** : If source.right.left.right = Node('s')
   **Output** : It is not a subtree

5. **Input** :  If source.right.right = Node('l')
   **Output** : It is  a subtree

