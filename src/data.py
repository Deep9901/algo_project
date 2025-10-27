import numpy as np

def generate_random_cities(n=25, seed=42):
    np.random.seed(seed)
    return np.random.rand(n, 2) * 100  # random 2D coordinates

def distance_matrix(cities):
    n = len(cities)
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist[i, j] = np.linalg.norm(cities[i] - cities[j])
    return dist
