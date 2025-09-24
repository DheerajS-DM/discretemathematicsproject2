import networkx as nx

def represent_structure_as_graph(vertices, edges):
    # Create a new empty undirected graph
    G = nx.Graph()
    
    # Add all given vertices (nodes) to the graph
    G.add_nodes_from(vertices)
    
    # Add all given edges (connections) between vertices
    G.add_edges_from(edges)
    
    # Return the constructed graph object
    return G
