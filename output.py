import matplotlib.pyplot as plt
from bag_item import BagItem
from creature import Creature


def show_statistics(b, w):
    y_values = [iteration for iteration in range(len(b))]
    plt.plot(y_values, b, 'g', label="Найкращі рішення")
    plt.plot(y_values, w, 'r', label="Найгірші рішення")
    plt.title("Графік залежності розв'язку від числа ітерацій")
    plt.xlabel("Число ітерацій")
    plt.ylabel("Якість рішення")
    plt.legend()
    plt.show()


def print_item_set(item_set: list[BagItem]):
    print("Доступнi предмети:")
    for i in range(len(item_set)):
        item = item_set[i]
        print(f"Предмет {i} Цінність: {item.value} Вага: {item.weight}")
    print()


def print_start_populatiion(start_population: list[Creature]):
    for i in range(len(start_population)):
        print(f"Особина {i}: цінність: {start_population[i].value}, вага: {start_population[i].weight }")
    print()


def print_best(best: Creature, item_set: list[BagItem], iteration: int):
    print(f"Найкраща вартість: {best.value}, вага найкращої особини: {best.weight}")
    print("Обрані предмети:")
    for item in [item_set[i] for i in range(len(item_set)) if best.chromosome[i]]:
        print(f"Цінність: {item.value} Вага: {item.weight}")
    print(f"Ітерація, на якій було знайдено найкраще значення: {iteration}")
    print()


def print_goal_function(goal_function: list[int]):
    for i in range(0, len(goal_function), len(goal_function)//20):
        print(f"{i+1}: {goal_function[i]}")
    print(f"{len(goal_function)}: {goal_function[-1]}")
