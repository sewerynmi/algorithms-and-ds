
class Node:

    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.data)


root = None # puste drzewo
root = Node("alone") # drzewo z 1 wezlem
# Reczne budowanie drzewa
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

# |       1       |
# |     /   \     |
# |   2       3   |
# |  / \     / \  |
# | 4   5   6   7 |

############### PRZECHODZENIE PRZEZ DRZEWO ######################
# preorder (węzeł, lewe, prawe) [1 2 4 5 3 6 7], odmiana DFS dla grafów
# inorder (lewe, węzeł, prawe) [4 2 5 1 6 3 7], odmiana DFS dla grafów
# postorder (lewe, prawe, węzeł) [4 5 2 6 7 3 1], odmiana DFS dla grafów
# poziomami [1 2 3 4 5 6 7], BFS dla grafów






