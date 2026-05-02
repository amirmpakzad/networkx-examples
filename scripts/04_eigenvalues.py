import matplotlib.pyplot as plt
import networkx as nx
import torch

G = nx.gnm_random_graph(100, 500)
print(nx.is_connected(G))

L = nx.normalized_laplacian_matrix(G)
L_array = L.toarray()
L_tensor = torch.tensor(L_array, dtype=torch.float32)

e = torch.linalg.eigvalsh(L_tensor)

print("is connected", nx.is_connected())
print("Largest eigenvalue:", max(e))
print("Smallest eigenvalue:", min(e))

plt.hist(e.numpy(), bins=50) 
plt.xlim(0, 2)
plt.show()
