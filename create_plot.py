import json
import math
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import sys

matplotlib.use('Agg')


def latency_comparison_plot(program_latencies, filename='latency_comparison.gif'):
    """
    Creates an animated plot comparing the latency of multiple programs.

    Args:
        program_latencies (list of tuples): A list of tuples, where each tuple contains the program name and the initial latency in seconds.
        time_range (int, optional): The total time range of the plot in seconds. Defaults to 10.
        fps (int, optional): The frames per second of the animation. Defaults to 10.
        filename (str, optional): The filename to save the animation as a GIF. Defaults to 'latency_comparison.gif'.
    """
    num_programs = len(program_latencies)
    program_latencies = sorted(program_latencies, key=lambda v: v[1], reverse=True)
    program_names = list(v[0] for v in program_latencies)

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 1)
    ax.set_xlabel('Latency (%)')
    ax.set_yticks(range(len(program_names) + 2))
    ax.set_yticklabels([""] + program_names + [""])
    ax.set_title('Latency Comparison')
    plt.subplots_adjust(left=.4, right=.9)  # Increase the left margin

    # Create the dots for each program
    dots = []
    latency_values = [latency for _, latency in program_latencies]
    for i, (program, _) in enumerate(program_latencies):
        dot, = ax.plot([], [], 'o', markersize=10, label=program)
        dots.append(dot)

    # Define the animation function
    def animate(frame, frames):
        for i, (pgm, latency) in enumerate(program_latencies):
            # Update the dot position
            rate = 1 / (latency / max(latency_values))
            value = frame / frames * rate
            direction = (0 if math.floor(value) % 2 == 0 else -1)
            x_coord = abs((value % 1) + direction)
            dots[i].set_data([x_coord], [i + 1])
        return dots

    # Create the animation
    interval = 1000 / 25  # ms
    frames = int(max(latency_values) * 1000 / interval) * 2
    fps = int(frames / max(latency_values))
    ani = animation.FuncAnimation(fig, animate,
                                  frames=frames, interval=interval,
                                  blit=True, repeat=True,
                                  fargs=(frames,))
    # Save the animation as a GIF
    ani.save(filename, writer='ffmpeg', fps=fps)
    plt.close()


def read_reports(reportsfile):
    import json
    with open(reportsfile) as f:
        data = json.load(f)
    program_latencies = [
        ('{} ({:.4f}s)'.format(v['command'], v['min']), v['min'])
        for v in data['results']
        if not any(c > 1 for c in v['exit_codes'])  # ignore programs that had errors
    ]
    return program_latencies


# Example usage
program_latencies = [
    ('Program A', 2.5),
    ('Program B', 5.0),
    ('Program C', 7.5),
    ('Program D', 10.0)
]

reports_file = sys.argv[1]
program_latencies = read_reports(reports_file)
latency_comparison_plot(program_latencies)
