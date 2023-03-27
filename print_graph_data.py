from hybit_graph.functions import load_data
from hybit_graph.print_functions import print_nodes, print_edges_weights, print_edges

if __name__ == '__main__':
    nodes, edges, edges_weight = load_data("Schnittstellen.xlsx")
    print()
    print_nodes(nodes)
    print_edges_weights(edges_weight)
    print_edges(edges)
