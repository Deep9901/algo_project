import time
from data import generate_random_cities, distance_matrix
from algorithms.heuristics import nearest_neighbor, two_opt, total_distance
from algorithms.dynamic import held_karp
from algorithms.simulated_annealing import simulated_annealing
from algorithms.genetic import genetic_algorithm

def compare_all():
    cities = generate_random_cities(12)  # use smaller size for exact DP
    dist = distance_matrix(cities)

    algorithms = []

    # Nearest Neighbor + 2-opt
    start = time.time()
    route = nearest_neighbor(dist)
    improved = two_opt(route, dist)
    algorithms.append(("Nearest Neighbor + 2-opt", total_distance(improved, dist), time.time()-start))

    # Held–Karp DP
    start = time.time()
    dp_cost = held_karp(dist)
    algorithms.append(("Held–Karp DP", dp_cost, time.time()-start))

    # Simulated Annealing
    start = time.time()
    route_sa, cost_sa = simulated_annealing(dist)
    algorithms.append(("Simulated Annealing", cost_sa, time.time()-start))

    # Genetic Algorithm
    start = time.time()
    route_ga, cost_ga = genetic_algorithm(dist)
    algorithms.append(("Genetic Algorithm", cost_ga, time.time()-start))

    print("\nAlgorithm Comparison:")
    for name, cost, runtime in algorithms:
        print(f"{name:<25} | Cost: {cost:>10.2f} | Time: {runtime:>7.3f}s")

if __name__ == "__main__":
    compare_all()
