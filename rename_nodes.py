def rename_nodes(nodes):
    """
    Converts list of (x, y) coordinate tuples into a dictionary
    mapping node IDs (N1, N2, ...) to coordinates.
    """
    node_mapping = {}
    for i, coord in enumerate(nodes, start=1):
        node_id = f'N{i}'  # Label nodes as N1, N2, N3, ...
        node_mapping[node_id] = coord
    return node_mapping
