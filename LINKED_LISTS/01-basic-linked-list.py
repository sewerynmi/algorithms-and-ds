
class Node:
    def __init__(self, content):
        self._content = content
        self._next = None
    
    def insert_elem(self, NewNode):
        NewNode._next = self._next
        self._next = NewNode
        
    def remove_element(self):
        NextNode = self._next
        if(NextNode in None):
            return False
        self._next = NextNode._next
        
        
def ExploreList(StartingNode):
    CurNode = StartingNode
    while(CurNode is not None):
        print(CurNode._content)
        CurNode = CurNode._next
    
    total = 0
    CurNode = StartingNode
    while(CurNode is not None):
        total = total + CurNode._content
        CurNode = CurNode._next
    return total
    
    
# Sum all even element of the list
def SumEvenListElements(StartingNode):
    CurNode = StartingNode
    SumTotalEven = 0
    while CurNode is not None:
        if CurNode._content % 2 == 0:
            SumTotalEven = SumTotalEven + CurNode._content
        CurNode = CurNode._next
    return SumTotalEven


def SecLargestListElement(StartingNode):
    if StartingNode is None:
        return None
    if StartingNode._next is None:
        return None
    
    SecondNode = StartingNode._next
    if StartingNode._content >= SecondNode._content:
        maxEl = StartingNode._content
        secEl = SecondNode._content
    
    CurNode = SecondNode._next
    while CurNode._next is not None:
        if CurNode._content > maxEl:
            secEl = maxEl
            maxEl = CurNode._content
        elif CurNode._content > secEl:
            secEl = CurNode._content
            
        CurNode = CurNode._next
    return secEl


def ReverseList(head):
    previous = None
    current = head
    next = None
    
    while (current is not None):
        next = current._next
        current._next = previous
        previous = current
        current = next
    
    head = previous
    return head

# TEST TEST TES

# Forming a linked list
Node0=Node(5)
Node1=Node(4)
Node2=Node(3)
Node3=Node(2)
Node4=Node(1)

Node0.insert_elem(Node1)
Node1.insert_elem(Node2)
Node2.insert_elem(Node3)
Node3.insert_elem(Node4)

print("\TEST\n")
ExploreList(Node0)

print("\nSum Total Even elemens\n")
print("Sum even el [assert: 6] : ", SumEvenListElements(Node0)) #6

print("\nSecond Largest list element\n")
print("[assert: 4] : ", SecLargestListElement(Node0)) #4

ReverseList(Node0)
ExploreList(Node0)
