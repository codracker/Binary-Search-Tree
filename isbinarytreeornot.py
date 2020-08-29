# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:35:26 2020

@author: Muskaan Jain
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isidentical(root1,root2):
    if(root1 == None and root2 == None):
        return True
    if(root1 != None and root2 != None and root1.data == root2.data):
        target_l = isidentical(root1.left , root2.left)
        target_r = isidentical(root1.right, root2.right)
        if(target_l and target_r):
            return True
        return False
    return  False

def issubtree(target,source):
    if(source is None):   #testcase1
        return True
    if(target is None):
        return False
    if isidentical(target,source):
        return True
    else:
        target_l=issubtree(target.left,source)
        target_r=issubtree(target.right, source)
        return target_l or target_r

# tree

target = Node('a')
target.left = Node('b')
target.right = Node('c')
target.right.left = Node('j')
target.right.right = Node('g')
target.left.left = Node('d')
target.left.right = Node('e')
target.left.left.left = Node('h')
target.left.left.right = Node('i')
target.left.right.right = Node('k')
target.right.right.right = Node('l')
target.right.right.left = Node('m')   #for test case2 change to 'z'

source = Node('c')
source.left = Node('j')
source.right = Node('g')     #for test case3 
source.right.left = Node('m')
source.right.right = Node('l') #for test case5
#source.right.left.right = Node('s')    #for test case4


if issubtree(target,source):
    print("It is a Subtree")
else:
    print("It is not a Subtree")
