import random
from utils.visualization import animate_route_evolution

# Generate random coordinates
def generate_cities(n=10):
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

# Dummy generator that yields random routes
def fake_route_gen(n=10, steps=50):
    cities = list(range(n))
    for _ in range(steps):
        random.shuffle(cities)
        yield cities[:], random.uniform(200, 500)

if __name__ == "__main__":
    cities = generate_cities(10)
    animate_route_evolution(cities, fake_route_gen(10), "Fake Route Evolution Test")
