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
    for i, ind in enumerate(pop.individuals):

        # invert fitness if minimizing
        m = -1 if pop.optimization == "min" else 1
        getFitness(ind)
        c_ = c
        while c_ > 0.05:
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
            c_ *= alpha
        pop.individuals[i] = copy.deepcopy(ind)

    if pop.n_elites > 0:
        pop.elites = sorted(pop.individuals, key= lambda i: i.fitness)[:pop.n_elites]