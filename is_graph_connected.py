import networkx as nx

def is_graph_connected(G):
    # Use NetworkX built-in function to check if graph is connected
    # Returns True if every node is reachable from any other node
    return nx.is_connected(G)
