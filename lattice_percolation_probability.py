import numpy as np
import matplotlib.pyplot as plt

trials = 300

p_values = np.arange(0.1, 0.91, 0.05)


directions = [(-1,0),(1,0),(0,-1),(0,1)]

def get_percolation_curve(grid_size):
    
    percolation_probabilities = []

    def percolates(grid):

        visited = np.zeros((grid_size, grid_size), dtype=int)

        stack = []

        for col in range(grid_size):

            if grid[0, col] == 1:

                visited[0, col] = 1
                stack.append((0, col))

        while stack:

            row, col = stack.pop()

            for dr, dc in directions:

                r = row + dr
                c = col + dc
    
                if 0 <= r < grid_size and 0 <= c < grid_size:

                    if grid[r, c] == 1 and visited[r, c] == 0:

                        visited[r, c] = 1
                        stack.append((r, c))

        return np.any(visited[grid_size - 1])


    for p in p_values:

        success = 0

        for _ in range(trials):

            grid = (np.random.rand(grid_size, grid_size) < p).astype(int)

            if percolates(grid):

                success += 1

        P = success / trials

        percolation_probabilities.append(P)

        print(f"p = {p:.2f}   Pperc = {P:.3f}")
    
    return percolation_probabilities



P25 = get_percolation_curve(25)
P50 = get_percolation_curve(50)
P100 = get_percolation_curve(100)

plt.figure(figsize=(8,6))

plt.plot(p_values, P25, marker='o', label='25x25')
plt.plot(p_values, P50, marker='s', label='50x50')
plt.plot(p_values, P100, marker='^', label='100x100')

plt.xlabel('Occupation Probability (p)')
plt.ylabel('Percolation Probability')
plt.title('Finite Size Effect in Site Percolation')

plt.grid(True)
plt.legend()

plt.show()