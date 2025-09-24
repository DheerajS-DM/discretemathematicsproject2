import networkx as nx

def simulate_removal(G, nodes_to_remove=None, edges_to_remove=None):
    # Create a copy of the input graph to avoid modifying original
    H = G.copy()
    
    # If a list of nodes to remove is provided, remove them from the graph copy
    if nodes_to_remove:
        H.remove_nodes_from(nodes_to_remove)
    
    # If a list of edges to remove is provided, remove them from the graph copy
    if edges_to_remove:
        H.remove_edges_from(edges_to_remove)
    
    # Return the modified graph copy
    return H
