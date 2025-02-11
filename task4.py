import matplotlib.pyplot as plt
import networkx as nx
import heapq


class BinaryHeap:
    def __init__(self, elements=None):
        self.heap = []
        if elements:
            for element in elements:
                heapq.heappush(self.heap, element)

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def extract_min(self):
        return heapq.heappop(self.heap) if self.heap else None

    def get_tree_representation(self):
        edges = []
        for i in range(len(self.heap)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(self.heap):
                edges.append((self.heap[i], self.heap[left]))
            if right < len(self.heap):
                edges.append((self.heap[i], self.heap[right]))
        return edges

    def visualize(self):
        edges = self.get_tree_representation()
        G = nx.DiGraph()
        G.add_edges_from(edges)

        pos = self._hierarchy_pos(G, list(G.nodes())[0]) if G.nodes else {}

        plt.figure(figsize=(8, 5))
        nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightblue', font_size=10, font_weight='bold')
        plt.show()

    def _hierarchy_pos(self, G, root, width=1., vert_gap=0.2, xcenter=0.5, pos=None, parent=None, level=0):
        if pos is None:
            pos = {root: (xcenter, 1 - level * vert_gap)}
        else:
            pos[root] = (xcenter, 1 - level * vert_gap)

        children = list(G.neighbors(root))
        if len(children) > 0:
            dx = width / 2
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = self._hierarchy_pos(G, child, width=dx, vert_gap=vert_gap, xcenter=nextx, pos=pos, parent=root,
                                          level=level + 1)
        return pos


# Example usage
data = [10, 20, 15, 30, 40, 50, 25]
bh = BinaryHeap(data)
bh.visualize()
