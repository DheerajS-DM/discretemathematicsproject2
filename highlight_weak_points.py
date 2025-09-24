from find_cut_vertices import find_cut_vertices
from find_cut_edges import find_cut_edges
from visualize_graph import visualize_graph

def highlight_weak_points(G):
    # Find all articulation points (cut vertices) in the graph
    cut_vertices = find_cut_vertices(G)
    
    # Find all bridges (cut edges) in the graph
    cut_edges = find_cut_edges(G)
    
    # Visualize the graph highlighting these weak points in red
    visualize_graph(G, highlight_nodes=cut_vertices, highlight_edges=cut_edges, title="Weak Points Highlighted")
