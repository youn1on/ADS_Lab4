from random import randint
from creature import Creature


class GeneticAlgo:
    def __init__(self, population: list[Creature], max_weight):
        self.population = population
        self.__update_best_worst()
        self.__max_weight = max_weight
        self.randCtr = 0

    def __update_best_worst(self):
        self.best = 0
        self.worst = 0
        for num in range(1, len(self.population)):
            if self.population[num] > self.population[self.best]:
                self.best = num
            elif self.population[num] < self.population[self.worst]:
                self.worst = num

    def __get_parent_indexes(self) -> tuple[int, int]:
        value_sum = sum([c.value for c in self.population])
        parents = []
        for p in range(2):
            r = randint(0, value_sum)
            for j in range(len(self.population)):
                if self.population[j].value >= r:
                    parents.append(j)
                    break
                r -= self.population[j].value
            else:
                parents.append(self.population[-1])
        return parents[0], parents[1]

    def __get_new_creatures(self, parents: tuple[int, int]) -> (Creature, None):
        new_creatures = self.population[parents[0]].crossover(self.population[parents[1]], self.__max_weight)
        if randint(1, 10) == 10:
            mutated = [n_creature.mutation_at(randint(0, len(n_creature.chromosome)-1)) for n_creature in new_creatures]
            for i in range(len(new_creatures)):
                if mutated[i].weight < self.__max_weight:
                    new_creatures[i] = mutated[i]
        return max(new_creatures) if len(new_creatures) > 0 else None

    def __update_population(self, new_creature: Creature):
        if new_creature > self.population[self.worst]:
            self.population[self.worst] = new_creature
            self.__update_best_worst()

    def run_iteration(self):
        parents = self.__get_parent_indexes()
        new_creature = self.__get_new_creatures(parents)
        if new_creature is not None:
            self.__update_population(new_creature)
