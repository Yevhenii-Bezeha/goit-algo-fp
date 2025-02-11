import random
import matplotlib.pyplot as plt

# Simulation of rolling two dice
num_simulations = 100000  # Number of simulations
sum_counts = {i: 0 for i in range(2, 13)}  # Counter for each possible sum

# Run the simulation
for _ in range(num_simulations):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total_sum = die1 + die2
    sum_counts[total_sum] += 1

# Calculate probabilities based on simulations
probabilities = {sum_: count / num_simulations * 100 for sum_, count in sum_counts.items()}

# Analytical probabilities
analytic_probabilities = {
    2: 1/36 * 100,
    3: 2/36 * 100,
    4: 3/36 * 100,
    5: 4/36 * 100,
    6: 5/36 * 100,
    7: 6/36 * 100,
    8: 5/36 * 100,
    9: 4/36 * 100,
    10: 3/36 * 100,
    11: 2/36 * 100,
    12: 1/36 * 100
}

# Plot comparison graph
x = list(probabilities.keys())
y_sim = list(probabilities.values())
y_analytic = list(analytic_probabilities.values())

plt.figure(figsize=(10, 6))
plt.bar(x, y_sim, width=0.4, label='Monte Carlo', alpha=0.6, color='blue', align='center')
plt.bar(x, y_analytic, width=0.4, label='Analytical', alpha=0.6, color='red', align='edge')

plt.xlabel('Sum of two dice')
plt.ylabel('Probability (%)')
plt.title('Comparison of Probabilities (Monte Carlo vs Analytical Calculations)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(x)
plt.show()

# Probability table
print("Probability table:")
print(f"{'Sum':<5} {'Probability (Monte Carlo)':<30} {'Probability (Analytical)'}")
for sum_ in range(2, 13):
    print(f"{sum_:<5} {probabilities[sum_]:<30.2f} {analytic_probabilities[sum_]:.2f}")
