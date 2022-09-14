# Tree as List of Lists
# No OOP

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    t = root.pop(1) # remove item on the left of the root (1) and assign it to 't'
    
    if len(t) > 1 : # if left had any elements
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root, newBranch):
    t = root.pop(2) # remove item on the right of the root (2) and assign it to 't'
    
    if len(t) > 1 : # if right had any elements
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]



# =========== TESTING =============

r = BinaryTree(3)
insertLeft(r, 4)
print(r)
insertLeft(r,5)
print(r)
insertRight(r,2)
print(r)
insertRight(r,10)
print(r)

l = getLeftChild(r)
print("Left child: ", l)