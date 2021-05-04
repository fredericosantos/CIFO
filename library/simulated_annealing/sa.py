import random, math, copy
from main import Population, Individual


def simulated_annealing(
    pop: Population,
    getFitness: "function",
    getNeighbours: "function",
    L: int = 20,
    c: int = 10,
    alpha: float = 0.95,
) -> Individual:

    # random solution
    ind = random.choice(pop.individuals)

    # invert fitness if minimizing
    m = -1 if pop.optimization == "min" else 1
    getFitness(ind)

    while c > 0.05:
        for _ in range(L):
            getNeighbours(ind)
            rnd_n = random.choice(ind.neighbours)
            getFitness(rnd_n)
            if rnd_n.fitness * m >= ind.fitness * m:
                ind = copy.deepcopy(rnd_n)
            else:
                p = random.uniform(0, 1)
                pc = math.exp(-abs(rnd_n.fitness * m - ind.fitness * m) / c)
                if p < pc:
                    ind = copy.deepcopy(rnd_n)
        c *= alpha
    return ind