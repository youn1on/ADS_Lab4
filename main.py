from genetic_algo import GeneticAlgo
from data_generation import *
from output import *


if __name__ == "__main__":
    item_set = generate_items(100, 2, 20, 1, 10)
    start_population = generate_start_population(item_set)
    ga = GeneticAlgo(start_population, 200)
    best, worst = [], []
    for i in range(10000):
        ga.run_iteration()
        best.append(ga.population[ga.best].value)
        worst.append(ga.population[ga.worst].value)
    print(ga.population[ga.best].value, ga.population[ga.worst].value)
    show_statistics(best, worst)



