import matplotlib.pyplot as plt
import time

def animate_route_evolution(cities, route_generator, title="TSP Evolution"):
    """Visualize TSP route updates in real-time."""
    # Turn on interactive mode
    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 6))

    # Extract coordinates
    x_coords = [c[0] for c in cities]
    y_coords = [c[1] for c in cities]

    # Initialize empty line and text
    (line,) = ax.plot([], [], 'bo-', linewidth=1.5)
    cost_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12)

    ax.set_xlim(min(x_coords) - 10, max(x_coords) + 10)
    ax.set_ylim(min(y_coords) - 10, max(y_coords) + 10)
    ax.set_title(title, fontsize=14)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True, linestyle='--', alpha=0.5)

    # Get first frame to initialize properly
    first = next(route_generator)
    if first:
        route, cost = first
        x = [cities[i][0] for i in route + [route[0]]]
        y = [cities[i][1] for i in route + [route[0]]]
        line.set_data(x, y)
        cost_text.set_text(f"Cost: {cost:.2f}")
        plt.pause(0.1)

    # Animation loop
    for route, cost in route_generator:
        x = [cities[i][0] for i in route + [route[0]]]
        y = [cities[i][1] for i in route + [route[0]]]
        line.set_data(x, y)
        cost_text.set_text(f"Cost: {cost:.2f}")
        plt.pause(0.05)  # this replaces flush_events()

    plt.ioff()
    plt.show(block=True)
