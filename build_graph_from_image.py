import networkx as nx

def build_graph_from_image(nodes, edge_list):
    # Construct a NetworkX graph from detected nodes and edges
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edge_list)
    return G
