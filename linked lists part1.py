# 1st way to create linked list

class LinkedListNode:
    def __init__(self,value,nextNode=None):
        self.value = value
        self.nextNode = nextNode
node1 = LinkedListNode(6)
node2 = LinkedListNode(3)
node3 = LinkedListNode(4)
node4 = LinkedListNode(10)

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

currentNode = node1
while True:
    print(currentNode.value,"->",end=" ")
    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode