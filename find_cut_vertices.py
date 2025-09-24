import networkx as nx

def find_cut_vertices(G):
    # Use NetworkX articulation_points function
    # This returns nodes that, when removed, increase number of connected components
    # Convert the generator to a list and return
    return list(nx.articulation_points(G))
