import numpy as np

def match_lines_to_nodes(line_segments, node_mapping, node_tolerance=15):
    """
    Match line endpoints (x1,y1),(x2,y2) to closest nodes,
    where nodes given as {node_id: (x, y)}.
    Returns list of edges as [(node_id_1, node_id_2), ...].
    """
    edges = []
    nodes_ids = list(node_mapping.keys())
    nodes_coords = list(node_mapping.values())
    
    for x1, y1, x2, y2 in line_segments:
        # Find nearest node id to first endpoint
        distances1 = [np.linalg.norm(np.array((x1, y1)) - np.array(coord)) for coord in nodes_coords]
        min_idx1 = np.argmin(distances1)
        n1 = nodes_ids[min_idx1]
        
        # Find nearest node id to second endpoint
        distances2 = [np.linalg.norm(np.array((x2, y2)) - np.array(coord)) for coord in nodes_coords]
        min_idx2 = np.argmin(distances2)
        n2 = nodes_ids[min_idx2]
        
        # Check distance tolerance before adding edge
        if distances1[min_idx1] <= node_tolerance and distances2[min_idx2] <= node_tolerance:
            edges.append((n1, n2))
    return edges
