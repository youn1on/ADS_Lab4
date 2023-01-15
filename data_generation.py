from random import randint
from creature import Creature
from bag_item import BagItem


def generate_items(number: int, min_val: int, max_val: int, min_weight: int, max_weight: int) -> list[BagItem]:
    set_of_items = []
    for j in range(number):
        item = BagItem(j, randint(min_val, max_val), randint(min_weight, max_weight))
        set_of_items.append(item)
    return set_of_items


def generate_start_population(items: list[BagItem]) -> list[Creature]:
    def get_chromosome(size: int, taken_item: int) -> list[bool]:
        new_chromosome = [False for g in range(size)]
        new_chromosome[taken_item] = True
        return new_chromosome

    creature_list = []
    for k in range(len(items)):
        creature_list.append(Creature(get_chromosome(len(items), k), items))
    return creature_list

