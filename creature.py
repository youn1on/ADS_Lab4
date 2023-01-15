from bag_item import BagItem


class Creature:
    def __init__(self, chromosome: list[bool], item_set: list[BagItem]):
        self.chromosome = chromosome
        self.item_set = item_set
        self.value = sum([i.value for (i, g) in zip(item_set, chromosome) if g])
        self.weight = sum([i.weight for (i, g) in zip(item_set, chromosome) if g])

    def crossover(self, another_creature, weight_limit):
        l = len(self.chromosome)
        child1 = self.chromosome[:int(l/3)]+another_creature.chromosome[int(l/3):int(2*l/3)]+self.chromosome[int(2*l/3):]
        child2 = another_creature.chromosome[:int(l/3)]+self.chromosome[int(l/3):int(2*l/3)]+another_creature.chromosome[int(2*l/3):]
        child_creature1 = Creature(child1, self.item_set)
        child_creature2 = Creature(child2, self.item_set)
        return [ch for ch in [child_creature1, child_creature2] if ch.weight <= weight_limit]


    def mutation_at(self, pos: int):
        if 0 > pos > len(self.chromosome):
            raise Exception()
        new_chromosome = [g for g in self.chromosome]
        new_chromosome[pos] = not self.chromosome[pos]
        nc = Creature(new_chromosome, self.item_set)
        return nc

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __str__(self):
        s = '['
        for g in self.chromosome:
            s += '1,' if g else '0,'
        s = s[:-1]+f'] = {self.value} ({self.weight})'
        return s

    def __repr__(self):
        return str(self)
