class Node:
    def __init__(self,content):
        self._content=content
        self._next=None  

    def insert_elem(self,NewNode):
        NewNode._next=self._next    
        self._next=NewNode


    def remove_elem(self):
        NextNode=self._next
        if(NextNode is None):
            return False
        self._next=NextNode._next



def ExploreList(StartingNode):
    CurNode=StartingNode
    while(CurNode is not None):
        print(CurNode._content)
    CurNode=CurNode._next


def SumEvenList(StartingNode):
    CurNode=StartingNode
    totalEven=0
    while CurNode is not None:
        if CurNode._content %2 == 0:
            totalEven = totalEven + CurNode._content
            CurNode=CurNode._next
    return totalEven


def  SecLargestList(StartingNode):
    if StartingNode is None:
        return None

    if StartingNode._next is None:
        return None

    SecondNode=StartingNode._next
    if StartingNode._content >= SecondNode._content:
        maxel=StartingNode._content
        secel=SecondNode._content

    CurNode=SecondNode._next
    while CurNode is not None:
        if CurNode._content>maxel:
            secel=maxel
            maxel=CurNode._content
        elif CurNode._content>secel:
            secel=CurNode._content

    CurNode=CurNode._next

    return secel


    # def  ReverseListIter(StartingNode):
    # CurNode=StartingNode
    # if  CurNode is None:
    # return None

    # NextNode=CurNode._next
    # CurNode._next=None
    # while NextNode is not None:
    # NextNextNode=NextNode._next

    # NextNode._next=CurNode
    # CurNode=NextNode
    # NextNode=NextNextNode

    # return CurNode

    # def ReverseListRec(StartingNode):
    # if StartingNode is None:
    # return None

    # NextNode=StartingNode._next
    # if NextNode is None:
    # return StartingNode

    # NodeRev=ReverseListRec(NextNode)
    # NextNode._next=StartingNode
    # StartingNode._next=None
    # return NodeRev

#Forming a linked list
Node0=Node(5)
Node1=Node(4)
Node2=Node(3)
Node3=Node(2)
Node4=Node(1)

Node0.insert_elem(Node1)
Node1.insert_elem(Node2)
Node2.insert_elem(Node3)
Node3.insert_elem(Node4)

#Running the functions on the list
#Uncomment the one you need to test 

#Testing the sum of even elements
totalEven=SumEvenList(Node0)
print("Total even: ", totalEven)

#Testing the second largest element
#secel=SecLargestList(Node0)
#print("Secel" , secel)

#Testing the iterative list reversal
#NodeRev=ReverseListIter(Node0)
#ExploreList(NodeRev) 


#Testing the recursive list reversal
#NodeRev=ReverseListRec(Node0)
#ExploreList(NodeRev)