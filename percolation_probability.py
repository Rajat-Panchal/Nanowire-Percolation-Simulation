from percolation_core import percolates
import matplotlib.pyplot as plt

Nc_values = range(700, 1601, 50)
trials = 100

probabilities = []

for Nc in Nc_values:

    success = 0

    for _ in range(trials):

        if percolates(Nc):
            success += 1

    P = success / trials

    probabilities.append(P)

    print(f"Nc = {Nc}   P = {P:.3f}")

plt.figure(figsize=(8,6))

plt.plot(
    list(Nc_values),
    probabilities,
    marker='o'
)

plt.xlabel("Number of Nanowires (Nc)")
plt.ylabel("Percolation Probability")
plt.title("Source-Drain Percolation Probability")

plt.grid(True)

plt.show()