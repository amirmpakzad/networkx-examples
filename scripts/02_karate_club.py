import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt

G = nx.karate_club_graph()

print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
print(f"Node 5 club: {G.nodes[5]['club']}")

# Basic metrics
print(f"Avg shortest path: {nx.average_shortest_path_length(G):.3f}")
print(f"Diameter: {nx.diameter(G)}")

# Community detection
communities = list(community.louvain_communities(G))
print(f"Number of communities: {len(communities)}")

# Visualization
pos = nx.spring_layout(G, seed=42)

community_colors = {node: i for i, comm in enumerate(communities) for node in comm}
node_colors = [community_colors[node] for node in G.nodes()]

plt.figure(figsize=(10, 7))
nx.draw(G, pos, 
        node_color=node_colors, 
        cmap=plt.cm.tab10, 
        with_labels=True, 
        node_size=600, 
        font_size=10,
        font_color='white',
        edge_color='gray',
        width=1.2)
   
#plt.savefig("../../results/karate_communities.png", dpi=300, bbox_inches='tight')
plt.show()