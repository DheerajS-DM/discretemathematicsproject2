from is_graph_connected import is_graph_connected
from simulate_removal import simulate_removal

def analyze_connectivity_change(G, nodes_to_remove=None, edges_to_remove=None):
    # Print connectivity status of the original graph
    print("Is the original graph connected?", is_graph_connected(G))
    
    # Create a modified graph after removing specified nodes or edges
    H = simulate_removal(G, nodes_to_remove=nodes_to_remove, edges_to_remove=edges_to_remove)
    
    # Print connectivity status after removal
    print("Is the graph connected after removal?", is_graph_connected(H))
    
    # Return the modified graph for further analysis or visualization
    return H
