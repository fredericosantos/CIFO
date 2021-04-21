from charles.search import sim_annealing
from charles.charles import Population, Individual
from charles.search import hill_climb
from copy import deepcopy
from data.ks_data import weights, values, capacity
import numpy as np


def evaluate(self):
    fitness = np.sum(np.array(self.representation) @ np.array(values))
    weight = np.sum(np.array(self.representation) @ np.array(weights))

    if weight > capacity:
        fitness = capacity - weight
    return fitness


def get_neighbours(self):
    n = [deepcopy(self.representation) for i in range(len(self.representation))]

    for count, i in enumerate(n):
        if i[count] == 1:
            i[count] = 0
        elif i[count] == 0:
            i[count] = 1

    n = [Individual(i) for i in n]
    return n


# Monkey Patching
Individual.evaluate = evaluate
Individual.get_neighbours = get_neighbours

pop = Population(
    size=20, optim="max", sol_size=len(values), valid_set=[0, 1], replacement=True
)

hill_climb(pop, log=1)
sim_annealing(pop, L=20, c=100)