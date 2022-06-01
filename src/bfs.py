import queue
from typing import List

from node import Node


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
        while len(self.frontier) != 0:
            self.explored.append(self.frontier[0])
            print(f"Value of the node is {self.frontier[0].value}")
            self.frontier.pop(0)

            # if it has children
            for i in root.children:
                if i != None:
                    self.frontier.append(i)
                else:
                    self.frontier.pop(0)

            if len(self.frontier) > 0:
                root = self.frontier[0]
            else:
                print(f"Successfully traversed the tree")


if __name__ == "__main__":
    # generate a root

    root = BFS(initialValue=10)
    root.addChindren(value=20, node=root.root)
    root.addChindren(value=30, node=root.root)
    root.addChindren(value=40, node=root.root.children[0])
    root.addChindren(value=50, node=root.root.children[0])

    root.traversal(root=root.root)
