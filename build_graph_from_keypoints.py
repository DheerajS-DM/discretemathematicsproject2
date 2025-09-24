import networkx as nx

def build_graph_from_keypoints(keypoints, edges):
    """
    Build a NetworkX graph from keypoints and pre-defined edges.
    keypoints: list of (x,y) tuples.
    edges: list of tuples (idx1, idx2) connecting keypoint indices.
    """
    G = nx.Graph()
    # Add nodes with IDs N1, N2, ...
    for i, point in enumerate(keypoints, start=1):
        G.add_node(f'N{i}', pos=point)
    
    for e in edges:
        n1 = f'N{e[0]+1}'  # edge indices zero-based
        n2 = f'N{e[1]+1}'
        G.add_edge(n1, n2)
        
    return G
