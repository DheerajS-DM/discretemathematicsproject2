from is_graph_connected import is_graph_connected
from find_cut_vertices import find_cut_vertices
from find_cut_edges import find_cut_edges
from visualize_graph import visualize_graph
from highlight_weak_points import highlight_weak_points

def analyze_graph_structure(G):
    # Analyze connectivity and weak points; display results and visualization
    print("Is the graph connected?", is_graph_connected(G))
    cut_vertices = find_cut_vertices(G)
    print("Cut vertices:", cut_vertices)
    cut_edges = find_cut_edges(G)
    print("Cut edges:", cut_edges)
    highlight_weak_points(G)
