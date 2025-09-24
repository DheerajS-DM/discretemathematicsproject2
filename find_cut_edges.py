import networkx as nx

def find_cut_edges(G):
    # Use NetworkX bridges function to find edges whose removal disconnects the graph
    # Return them as a list of tuples
    return list(nx.bridges(G))
