items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(budget):
    ratios = [(name, data["calories"] / data["cost"], data["cost"], data["calories"]) for name, data in items.items()]
    ratios.sort(key=lambda x: x[1], reverse=True)

    total_calories = 0
    selected_items = []
    remaining_budget = budget

    # Select items until the budget is exhausted
    for name, ratio, cost, calories in ratios:
        if cost <= remaining_budget:
            selected_items.append(name)
            total_calories += calories
            remaining_budget -= cost

    return selected_items, total_calories


def dynamic_programming(budget):
    n = len(items)
    dp = [0] * (budget + 1)


    selected_items = [[] for _ in range(budget + 1)]

    for name, data in items.items():
        cost = data["cost"]
        calories = data["calories"]

        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                selected_items[b] = selected_items[b - cost] + [name]

    return selected_items[budget], dp[budget]


# Example usage
budget = 100

# Greedy algorithm
greedy_selected, greedy_calories = greedy_algorithm(budget)
print("Greedy Algorithm:")
print("Selected items:", greedy_selected)
print("Total calories:", greedy_calories)

# Dynamic programming
dp_selected, dp_calories = dynamic_programming(budget)
print("\nDynamic Programming:")
print("Selected items:", dp_selected)
print("Total calories:", dp_calories)
