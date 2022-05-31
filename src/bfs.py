from typing import List
import Node from node
import queue

class BFS:
    def __init__(self, initialValue: int) -> None:
        # define the root node
        self.root = Node(value=initialValue)
        self.frontier = []
        self.explored = []
    
    def addChindren(self, value: int, node: Node) -> List:
        return node.children.append(Node(value=value))
    
    def traversal(self, root: Node):
        # From the root traverse breadth first
        # the code is in accordance to Russell and Norvich

        self.frontier.append(root)
        while not self.frontier.empty():
            self.explored.append(self.frontier[0])
            print(f"Value of the node is {self.frontier[0].value}")
            self.frontier.pop(0)
            
            # if it has children
            for i in root.children:
                if i != None:
                    self.frontier.append(i)
                else:
                    pass