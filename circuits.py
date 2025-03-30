import networkx as nx
import matplotlib.pyplot as plt

def draw_circuit(graph, title, filename):
    pos = nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='black', node_size=2000)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title(title)
    plt.savefig(filename)  # Save the image
    print(f"Image saved as {filename}")  # Print confirmation
    plt.show()

# Example 1: Simple Series Circuit
graph_series = nx.Graph()
graph_series.add_edge("A", "B", weight=5)
graph_series.add_edge("B", "C", weight=10)
draw_circuit(graph_series, "Series Circuit", "series_circuit.png")

# Example 2: Simple Parallel Circuit
graph_parallel = nx.Graph()
graph_parallel.add_edge("A", "B", weight=5)
graph_parallel.add_edge("A", "B", weight=10)
draw_circuit(graph_parallel, "Parallel Circuit", "parallel_circuit.png")

# Example 3: Complex Circuit
graph_complex = nx.Graph()
graph_complex.add_edge("A", "B", weight=5)
graph_complex.add_edge("B", "C", weight=10)
graph_complex.add_edge("A", "C", weight=15)
draw_circuit(graph_complex, "Complex Circuit", "complex_circuit.png")
