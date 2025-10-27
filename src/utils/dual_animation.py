import matplotlib.pyplot as plt
import matplotlib.animation as animation

def dual_animation(cities, gen1, gen2, name1="Simulated Annealing", name2="Genetic Algorithm", save=False):
    """Animate two algorithms side by side using FuncAnimation."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    plt.suptitle("TSP Evolution Comparison", fontsize=14)

    artists = []

    # Extract coordinates
    x = [c[0] for c in cities]
    y = [c[1] for c in cities]

    # Setup each subplot
    lines, texts = [], []
    for ax, name in zip(axes, [name1, name2]):
        line, = ax.plot([], [], 'bo-', linewidth=1.5)
        text = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=10)
        ax.set_xlim(min(x)-5, max(x)+5)
        ax.set_ylim(min(y)-5, max(y)+5)
        ax.set_title(name)
        ax.grid(True, linestyle='--', alpha=0.4)
        lines.append(line)
        texts.append(text)

    # Preload frames
    frames1 = list(gen1)
    frames2 = list(gen2)
    total_frames = min(len(frames1), len(frames2))

    def update(frame):
        route1, cost1 = frames1[frame]
        route2, cost2 = frames2[frame]

        x1 = [cities[i][0] for i in route1 + [route1[0]]]
        y1 = [cities[i][1] for i in route1 + [route1[0]]]
        x2 = [cities[i][0] for i in route2 + [route2[0]]]
        y2 = [cities[i][1] for i in route2 + [route2[0]]]

        lines[0].set_data(x1, y1)
        lines[1].set_data(x2, y2)
        texts[0].set_text(f"Cost: {cost1:.2f}")
        texts[1].set_text(f"Cost: {cost2:.2f}")

        return lines + texts

    ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=100, blit=False, repeat=False)

    if save:
        ani.save("tsp_dual_evolution.mp4", writer="ffmpeg", fps=10)
        print("🎥 Saved as tsp_dual_evolution.mp4")

    plt.show()
