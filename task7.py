import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def monte_carlo_simulation(num_simulations):
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_simulations):
        dice1, dice2 = roll_dice()
        dice_sum = dice1 + dice2
        sum_counts[dice_sum] += 1
    
    probabilities = {sum_value: count / num_simulations for sum_value, count in sum_counts.items()}
    
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, color='skyblue')
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Імовірність')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.xticks(sums)
    plt.grid(axis='y')
    plt.show()

def main():
    num_simulations = 10000
    probabilities = monte_carlo_simulation(num_simulations)
    
    print("Ймовірності сум при киданні двох кубиків:")
    for sum_value, probability in probabilities.items():
        print(f"Сума {sum_value}: {probability:.4f}")
    
    plot_probabilities(probabilities)

if __name__ == "__main__":
    main()
