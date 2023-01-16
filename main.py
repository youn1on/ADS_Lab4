from genetic_algo import GeneticAlgo
from data_generation import *
from output import *


if __name__ == "__main__":
    item_set = generate_items(100, 2, 20, 1, 10)
    print_item_set(item_set)
    start_population = generate_start_population(item_set)
    print_start_populatiion(start_population)
    ga = GeneticAlgo(start_population, 200)
    best, worst = [], []
    for i in range(5000):
        ga.run_iteration()
        best.append(ga.population[ga.best].value)
        worst.append(ga.population[ga.worst].value)
    iteration = best.index(max(best))
    print_best(ga.population[ga.best], item_set, iteration)
    show_statistics(best, worst)
    #print_goal_function(best)


