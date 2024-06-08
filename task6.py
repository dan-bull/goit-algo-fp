items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    # Список вартостей і калорій
    costs = [items[item]['cost'] for item in items]
    calories = [items[item]['calories'] for item in items]
    n = len(items)
    
    # Таблиця для зберігання максимальних калорій для кожного бюджету
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Заповнюємо таблицю dp
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-costs[i-1]] + calories[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Знаходимо які страви були вибрані
    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            item = list(items.keys())[i-1]
            selected_items.append(item)
            w -= costs[i-1]
    
    selected_items.reverse()
    return selected_items, dp[n][budget]

# Приклад використання
budget = 100
greedy_result, greedy_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", greedy_result)
print("Total calories:", greedy_calories)

dp_result, dp_calories = dynamic_programming(items, budget)
print("Dynamic Programming:")
print("Selected items:", dp_result)
print("Total calories:", dp_calories)
