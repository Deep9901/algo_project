import random
import math

def total_distance(route, dist):
    return sum(dist[route[i]][route[i+1]] for i in range(len(route)-1)) + dist[route[-1]][route[0]]

def simulated_annealing_evolution(dist, initial_temp=10000, cooling_rate=0.995, stop_temp=1):
    n = len(dist)
    route = list(range(n))
    random.shuffle(route)

    best_route = route[:]
    best_cost = total_distance(best_route, dist)
    temp = initial_temp

    yield best_route, best_cost  # first frame

    while temp > stop_temp:
        i, j = sorted(random.sample(range(n), 2))
        new_route = route[:i] + route[i:j][::-1] + route[j:]
        new_cost = total_distance(new_route, dist)
        delta = new_cost - best_cost

        if delta < 0 or random.random() < math.exp(-delta / temp):
            route = new_route
            if new_cost < best_cost:
                best_cost = new_cost
                best_route = route

        temp *= cooling_rate
        yield best_route, best_cost  # yield intermediate frame

    yield best_route, best_cost
