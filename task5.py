import networkx as nx
import matplotlib.pyplot as plt


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = TreeNode(value)
                return
            else:
                queue.append(node.left)
            if not node.right:
                node.right = TreeNode(value)
                return
            else:
                queue.append(node.right)

    def bfs_traversal(self):
        if not self.root:
            return []
        queue = [self.root]
        visited = []
        while queue:
            node = queue.pop(0)
            visited.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return visited

    def dfs_traversal(self):
        if not self.root:
            return []
        stack = [self.root]
        visited = []
        while stack:
            node = stack.pop()
            visited.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return visited


def visualize_tree(tree, traversal_order, title):
    G = nx.DiGraph()
    node_positions = {}

    def add_edges(node, x=0, y=0, level=1):
        if node:
            node_positions[node.value] = (x, -y)
            if node.left:
                G.add_edge(node.value, node.left.value)
                add_edges(node.left, x - 1 / level, y + 1, level * 2)
            if node.right:
                G.add_edge(node.value, node.right.value)
                add_edges(node.right, x + 1 / level, y + 1, level * 2)

    add_edges(tree.root)
    colors = generate_colors(len(traversal_order))
    node_colors = {value: colors[i] for i, value in enumerate(traversal_order)}

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos=node_positions, with_labels=True, node_size=2000,
            node_color=[node_colors[n] for n in G.nodes()], font_size=10, edge_color='gray')
    plt.title(title)
    plt.show()


def generate_colors(n):
    return ["#%02x%02x%02x" % (int(18 + i * (200 / n)), int(150 + i * (80 / n)), int(240 - i * (200 / n))) for i in
            range(n)]


if __name__ == "__main__":
    tree = BinaryTree()
    for i in range(1, 11):
        tree.insert(i)

    bfs_order = tree.bfs_traversal()
    dfs_order = tree.dfs_traversal()

    visualize_tree(tree, bfs_order, "Breadth-First Search Traversal")
    visualize_tree(tree, dfs_order, "Depth-First Search Traversal")
