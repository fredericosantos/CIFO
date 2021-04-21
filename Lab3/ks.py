from charles import Population, Individual
from hc import hill_climb
from copy import deepcopy
from ks_data import weights, values, capacity

    
def evaluate(self):
    fitness = 0
    weight = 0
    for bit in range(len(self.representation)):
        if self.representation[bit] == 1:
            fitness += values[bit]
            weight += weights[bit]
    if weight > capacity:
            fitness = 0
    return fitness

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
    size=20, optim="max", sol_size=len(values), valid_set=[0,1], replacement=True
)


hill_climb(pop, log=True)