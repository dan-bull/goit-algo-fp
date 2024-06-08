import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)

    def build_heap(self):
        if not self.heap:
            return None
        root = self.create_node(0)
        self.build_heap_recursive(root, 0)
        return root

    def build_heap_recursive(self, node, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < len(self.heap):
            node.left = self.create_node(left_index)
            self.build_heap_recursive(node.left, left_index)
        if right_index < len(self.heap):
            node.right = self.create_node(right_index)
            self.build_heap_recursive(node.right, right_index)

    def create_node(self, index):
        return Node(self.heap[index])

def draw_heap(heap):
    tree_root = heap.build_heap()
    draw_tree(tree_root)

def main():
    heap = BinaryHeap()
    elements = [10, 20, 15, 30, 40, 50, 100, 25, 5]

    for element in elements:
        heap.insert(element)

    draw_heap(heap)

if __name__ == "__main__":
    main()
