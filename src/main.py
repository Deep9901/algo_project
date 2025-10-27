import time
import numpy as np
import matplotlib.pyplot as plt

from data import generate_random_cities, distance_matrix
from algorithms.heuristics import nearest_neighbor, two_opt, total_distance
from algorithms.dynamic import held_karp
from algorithms.simulated_annealing import simulated_annealing_evolution
from algorithms.genetic import genetic_algorithm_evolution

# --- Utility for static plotting ---
def plot_all_routes(cities, routes_data):
    n = len(routes_data)
    plt.figure(figsize=(14, 8))
    for i, (name, route, cost) in enumerate(routes_data):
        plt.subplot(2, (n + 1) // 2, i + 1)
        x = [cities[i][0] for i in route + [route[0]]]
        y = [cities[i][1] for i in route + [route[0]]]
        plt.plot(x, y, 'bo-', linewidth=1.2)
        plt.title(f"{name}\nCost: {cost:.2f}")
        plt.axis('off')
    plt.suptitle("Final Routes Found by Each Algorithm", fontsize=14)
    plt.tight_layout()
    plt.show()

def plot_city_map(cities):
    plt.figure(figsize=(6, 6))
    plt.scatter([c[0] for c in cities], [c[1] for c in cities], color='blue')
    for i, (x, y) in enumerate(cities):
        plt.text(x + 1, y + 1, str(i), fontsize=8)
    plt.title("Map of 25 Cities")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

def plot_comparison_bar(results):
    names = [r[0] for r in results]
    costs = [r[1] for r in results]
    plt.figure(figsize=(8, 5))
    plt.bar(names, costs, color='cornflowerblue')
    plt.xticks(rotation=20, ha='right')
    plt.ylabel("Total Distance (Cost)")
    plt.title("Algorithm Performance Comparison")
    plt.tight_layout()
    plt.show()

# --- Main driver ---
def main():
    np.random.seed(42)
    cities = generate_random_cities(25)
    dist = distance_matrix(cities)

    print("\n=== Traveling Salesman Problem with 25 Cities ===")

    results = []  # (algorithm, cost, time)
    routes_data = []  # (name, route, cost)

    # --- 1️⃣ Nearest Neighbor + 2-opt ---
    start = time.time()
    route_nn = nearest_neighbor(dist)
    route_nn_opt = two_opt(route_nn, dist)
    nn_cost = total_distance(route_nn_opt, dist)
    results.append(("Nearest Neighbor + 2-opt", nn_cost, time.time() - start))
    routes_data.append(("Nearest Neighbor + 2-opt", route_nn_opt, nn_cost))

    # --- 2️⃣ Held–Karp Dynamic Programming (Exact) ---
    start = time.time()
    # Note: DP will be *very slow* beyond ~20 cities, so we’ll run it on first 12 for demonstration
    small_dist = dist[:12, :12]
    dp_cost = held_karp(small_dist)
    results.append(("Held–Karp DP (12 cities)", dp_cost, time.time() - start))
    dp_route = list(range(12))
    routes_data.append(("Held–Karp DP (12 cities)", dp_route, dp_cost))

    # --- 3️⃣ Simulated Annealing ---
    start = time.time()
    sa_route, sa_cost = list(simulated_annealing_evolution(dist))[-1]
    results.append(("Simulated Annealing", sa_cost, time.time() - start))
    routes_data.append(("Simulated Annealing", sa_route, sa_cost))

    # --- 4️⃣ Genetic Algorithm ---
    start = time.time()
    ga_route, ga_cost = list(genetic_algorithm_evolution(dist))[-1]
    results.append(("Genetic Algorithm", ga_cost, time.time() - start))
    routes_data.append(("Genetic Algorithm", ga_route, ga_cost))

    # --- Print consistent summary ---
    print("\n=== Final Results ===")
    print(f"{'Algorithm':<35} | {'Cost':>10} | {'Time (s)':>10}")
    print("-" * 60)
    for name, cost, runtime in results:
        print(f"{name:<35} | {cost:>10.2f} | {runtime:>10.3f}")

    # --- Plot city map ---
    plot_city_map(cities)

    # --- Plot routes ---
    plot_all_routes(cities, routes_data)

    # --- Plot performance comparison ---
    plot_comparison_bar(results)

if __name__ == "__main__":
    main()
