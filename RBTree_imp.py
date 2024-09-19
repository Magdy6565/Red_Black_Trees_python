import random
import math
import string


class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None



class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
        self.size = 0

    def insert(self, val):
        # Ordinary Binary Search Insertion
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # new node must be red

        parent = None
        current = self.root
        while current != self.nil:  # while loop 3l4an t7dd men hwa parent el node elly 3ayz a3mlha insert
            parent = current
            if new_node.val.lower() < current.val.lower():
                current = current.left
            elif new_node.val.lower() > current.val.lower():
                current = current.right
            else:
                return -1
        #And kda m3aya el parent bta3 el inserted node  h4oof  b2a h7ot el new node yeememno wla 4malo
        # Set the parent and insert the new node
        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.val.lower() < parent.val.lower():
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the tree and increment the size
        self.size += 1
        self.fix_insert(new_node)
        return 0
    # def get_black_height(self):
    #     curr = self.root
    #     count = 0
    #     while curr != self.nil:
    #         if curr.red == False:
    #             count += 1
    #         curr = curr.left
    #     return count
    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:  # Lw right child  1) uncle red --> recolor  2) right left --> right rotate then right right  3) right right
                uncle = new_node.parent.parent.left  # uncle
                if uncle.red:
                    uncle.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent # l2n el mo4kla de non terminal  mmkn b3d ma t3ml swap ben colors el p wel gp tla2y mo4kla fel grandparent f y7lha el loop elly b3dha
                else:
                    if new_node == new_node.parent.left: # Lw  right left  e3ml right rotate b3d kda  right right routine
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    # Right Right routine  -->  left rotate grand parent   then swap colors between parent  and grand parent
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.right  # uncle

                if uncle.red:
                    uncle.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False

    def search(self, val):
        curr = self.root
        while curr != self.nil :
            if val.lower() == curr.val.lower():
                return "YES"
            # print(f"Comparison between {val.lower()} and {curr.val.lower()}")
            if val.lower() < curr.val.lower():
                # print("We go left")
                curr = curr.left
            else:
                # print("We go right")

                curr = curr.right
        return "NO"

    # rotate left at node x
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y



    def get_size(self):
        return self.size

    def get_height(self, curr):
        if curr.val == self.nil.val:
            return 0
        return 1 + max(self.get_height(curr.left), self.get_height(curr.right))



def max(x, y):
    if x > y:
        return x
    return y

