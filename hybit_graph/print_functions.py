def print_nodes(nodes):
    print("Nodes: ")
    for node in nodes:
        print("- %s" % nodes[node].node_info())
    print()


def print_edges(edges):
    print("Edges: ")
    for edge in edges:
        print(edge)
    print()


def print_edges_weights(edges):
    print("Edges Weights:")
    for edge in edges:
        print("From %s" % edge)
        for to in edges[edge]:
            print("\t%s: %d" % (to, edges[edge][to]))
    print()
