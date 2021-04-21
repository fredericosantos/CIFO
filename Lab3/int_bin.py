from charles import *
from hc import hill_climb
from copy import deepcopy


def evaluate(self):
    return self.representation.count(1)


def get_neighbours(self):
    n = [deepcopy(self.representation) for i in range(len(self))]
    
    for count, i in enumerate(n):
        if i[count] == 1:
            i[count] = 0
        elif i[count] == 0:
            i[count] = 1

    n = [Individual(i) for i in n]
    return n

Individual.evaluate = evaluate
Individual.get_neighbours = get_neighbours

pop = Population(
    size=20, optim="max", sol_size=4, valid_set=[0,1], replacement=True
)

hill_climb(pop, log=True)