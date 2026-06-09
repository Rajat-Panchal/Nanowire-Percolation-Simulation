# Nanowire Percolation Simulation

## Overview

This project investigates percolation phenomena in random nanowire networks and 2D square lattices using Python. Monte Carlo simulations and graph-based algorithms are employed to study connectivity, source-drain percolation, critical thresholds, and finite-size effects.

## Objectives

- Study percolation in random nanowire networks.
- Analyze source-drain connectivity using graph traversal algorithms.
- Determine how percolation probability varies with nanowire density (Nc).
- Investigate site percolation on 2D square lattices.
- Observe finite-size effects and estimate the percolation threshold.

## Features

- Random nanowire generation with arbitrary orientations.
- Intersection detection between nanowires.
- Graph construction from nanowire networks.
- BFS-based source-drain connectivity analysis.
- Monte Carlo estimation of percolation probability.
- Site percolation simulation on square lattices.
- Finite-size effect analysis for different lattice dimensions.

## Methodology

### Continuum (Nanowire) Percolation

1. Generate random nanowires inside a finite area.
2. Detect intersections between nanowires.
3. Construct a connectivity graph.
4. Identify source and drain nanowires.
5. Use Breadth First Search (BFS) to determine whether a conducting path exists.
6. Repeat over multiple trials to estimate percolation probability.

### Lattice Percolation

1. Generate a square lattice with occupation probability \(p\).
2. Occupied sites represent conducting sites.
3. Use DFS/BFS to identify connected clusters.
4. Check whether a cluster spans from top to bottom.
5. Repeat over many realizations to obtain the percolation probability.

## Tools Used

- Python
- NumPy
- Matplotlib

## Results

The simulations demonstrate:

- Emergence of a critical percolation threshold.
- Increase in percolation probability with nanowire density.
- Sharp transition near the critical occupation probability in lattice percolation.
- Finite-size effects for different lattice dimensions.
- Visualization of conducting pathways and connected clusters.

## Future Improvements

- Conductance matrix calculations for nanowire networks.
- Effective network conductivity estimation.
- Extraction of critical exponents near the percolation threshold.
- Advanced finite-size scaling analysis.
- Comparison with theoretical and experimental percolation models.

