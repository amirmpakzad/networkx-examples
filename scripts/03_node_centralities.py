import networkx as nx
import torch

def compute_centralities(G):
    """Compute three centrality measures and stack as node features."""
    betweenness = nx.betweenness_centrality(G)
    closeness = nx.closeness_centrality(G)
    eigenvector = nx.eigenvector_centrality(G, max_iter=1000)
    
    # Convert to tensor
    x = torch.stack([
        torch.tensor(list(betweenness.values()), dtype=torch.float32),
        torch.tensor(list(closeness.values()),  dtype=torch.float32),
        torch.tensor(list(eigenvector.values()), dtype=torch.float32)
    ], dim=1)
    
    return x


if __name__ == "__main__":
    G = nx.erdos_renyi_graph(n=100, p=0.1, seed=42)
    
    x = compute_centralities(G)
    
    print(f"Feature matrix shape: {x.shape}")   # (100, 3)
    print(f"First node features:\n{x[0]}")
    print(f"\nFeature means:\n{x.mean(dim=0)}")