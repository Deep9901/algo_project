import random

def total_distance(route, dist):
    return sum(dist[route[i]][route[i+1]] for i in range(len(route)-1)) + dist[route[-1]][route[0]]

def init_population(pop_size, n):
    population = []
    for _ in range(pop_size):
        route = list(range(n))
        random.shuffle(route)
        population.append(route)
    return population

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [-1]*len(parent1)
    child[start:end] = parent1[start:end]
    fill = [city for city in parent2 if city not in child]
    j = 0
    for i in range(len(child)):
        if child[i] == -1:
            child[i] = fill[j]
            j += 1
    return child

def mutate(route, rate=0.02):
    for i in range(len(route)):
        if random.random() < rate:
            j = random.randint(0, len(route)-1)
            route[i], route[j] = route[j], route[i]

def genetic_algorithm_evolution(dist, pop_size=100, generations=300):
    n = len(dist)
    population = init_population(pop_size, n)
    best = min(population, key=lambda r: total_distance(r, dist))
    best_cost = total_distance(best, dist)

    yield best, best_cost  # initial frame

    for gen in range(generations):
        fitness = [(r, 1 / total_distance(r, dist)) for r in population]
        fitness.sort(key=lambda x: x[1], reverse=True)

        new_pop = []
        for _ in range(pop_size // 2):
            parent1, parent2 = random.choices(fitness[:50], k=2)
            child1 = crossover(parent1[0], parent2[0])
            child2 = crossover(parent2[0], parent1[0])
            mutate(child1)
            mutate(child2)
            new_pop.extend([child1, child2])

        population = new_pop
        current_best = min(population, key=lambda r: total_distance(r, dist))
        current_cost = total_distance(current_best, dist)

        if current_cost < best_cost:
            best, best_cost = current_best, current_cost

        yield best, best_cost  # each generation

    yield best, best_cost
