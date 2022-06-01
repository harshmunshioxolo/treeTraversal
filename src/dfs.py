import queue
from typing import List

from node import Node


class DFS:
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

        # The change with respect to the BFS is the way this expands. It will still add the childred
        """
                    A
                /\       \
            B       C       D
           /  \     
          D    E

        If the tree is in aforementioned form, then the DFS would work as follows
        frontier = [A] <--- Root Node
        explore = []

        # 1. Open the first node and check for childred
        frontier = [B,C,D]
        explored = [A]

        # 2. Open the first element from the list
        frontier = [D, E, C, D]
        explored = [A, B]

        # 3. ----

        Pattern:
            Always explore the 1st element
            Always INSERT the next children at position 0

        """
        self.frontier.append(root)
        while len(self.frontier) != 0:
            self.explored.append(self.frontier[0])
            print(f"Value of the node is {self.frontier[0].value}")
            self.frontier.pop(0)

            # if it has children
            for i in range(len(root.children)):
                if i != None:
                    index = 0 + i
                    self.frontier.insert(index, root.children[i])
                else:
                    self.frontier.pop(0)

            if len(self.frontier) > 0:
                root = self.frontier[0]
            else:
                print(f"Successfully traversed the tree")


if __name__ == "__main__":
    # generate a root

    root = DFS(initialValue=10)
    root.addChindren(value=20, node=root.root)
    root.addChindren(value=30, node=root.root)
    root.addChindren(value=40, node=root.root.children[0])
    root.addChindren(value=50, node=root.root.children[0])

    root.traversal(root=root.root)
