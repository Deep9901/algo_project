def total_distance(route, dist):
    return sum(dist[route[i]][route[i+1]] for i in range(len(route)-1)) + dist[route[-1]][route[0]]

def nearest_neighbor(dist):
    n = len(dist)
    unvisited = set(range(1, n))
    route = [0]
    while unvisited:
        last = route[-1]
        next_city = min(unvisited, key=lambda c: dist[last][c])
        unvisited.remove(next_city)
        route.append(next_city)
    route.append(0)
    return route

def two_opt(route, dist):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route)-2):
            for j in range(i+1, len(route)-1):
                if j - i == 1: continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if total_distance(new_route, dist) < total_distance(best, dist):
                    best = new_route
                    improved = True
        route = best
    return best
