# Necessary imports
    from matplotlib import pyplot as plt
    import matplotlib.animation as animation


# On top of *.py file (setting up plot)
    fig = plt.figure(figsize=(5, 6))
    plt.xlim((-.5, 4.5))
    plt.ylim((-.5, 5.5))
    plt.xticks([x-.5 for x in range(5)])
    plt.yticks([x-.5 for x in range(6)])
    plt.grid()


# Inside main function (static paths and obstacles)
    plt.plot(*tuple(zip(*path.path)), label='Computed path', linestyle='--')
    plt.plot(*tuple(zip(*path.spath)), label='Smoothed path', linestyle='--')
    obstacles = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                obstacles.append((x, y))
    plt.scatter(*tuple(zip(*obstacles)), s=3100, marker='s')    # adjust size parameter


# Inside run function
    # robot_positions and robot_positions2 - list of tuples with robot coordinates for each step
    # particles_positions – list of lists of tuples with particles coonrinades
    # All lists with coordinates should be filled inside while-loop
    plt.plot(*tuple(zip(*robot_positions)), label='Estimated robot path')
    plt.plot(*tuple(zip(*robot_positions2)), label='True robot path')
    plt.legend(loc='upper left')

    def update(frame):
        return (
            plt.scatter(*tuple(zip(*particles_positions[frame])), s=1, marker=',', c='b'),
            plt.scatter(*robot_positions2[frame], c='r')
        )

    ani = animation.FuncAnimation(fig, update, frames=range(len(particles_positions)), blit=True, repeat=False, interval=100)
    plt.show()
