import networkx as nx
import matplotlib.pyplot as plt 


G = nx.Graph()
G.add_node("A")
G.add_nodes_from(["B", "C"])

G.add_edge("A", "B", weight=0.5)
G.add_edge("B", "C", weight=2)
G.add_edge("C", "D", weight=0.9)
G.add_edge("B", "D", weight=0.4)

weights = nx.get_edge_attributes(G, "weight")

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos=pos, with_labels=True, node_size=500, font_color="lightblue")
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=weights)
plt.show()


clustering = nx.clustering(G)
avg_clustering = nx.average_clustering(G)

print("clustering:", clustering)
print("average clustering:", avg_clustering)