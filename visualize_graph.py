import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(G, highlight_nodes=None, highlight_edges=None, title="Graph"):
    # Generate positions for each node using spring layout for visual clarity
    pos = nx.spring_layout(G)
    
    # Draw the base graph: light blue nodes, gray edges, labeled nodes
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800, font_size=12)
    
    # If a list of nodes to highlight is provided, draw them in red
    if highlight_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=highlight_nodes, node_color='red')
    
    # If a list of edges to highlight is provided, draw them in thicker red lines
    if highlight_edges:
        nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, edge_color='red', width=2)
    
    # Set the title of the plot window
    plt.title(title)
    
    # Display the plot window to the user
    plt.show()
