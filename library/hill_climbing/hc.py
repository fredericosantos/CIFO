import random, copy
from main import Population, Individual
import numpy as np


def hill_climb(
    pop: Population, getFitness: "function", getNeighbours: "function"
) -> Individual:
    """Hill Climb on a population of individuals by giving the function and
    fitness function and a function to get neighbours. Return the best individual.

    Args:
        pop (Population): Population to hill climb
        getFitness (function): function to get fitness of an individual
        getNeighbours (function): function to get neighbours of an individual

    Returns:
        Individual: Return the best individual found
    """
    # random solution
    ind = random.choice(pop.individuals)

    # invert fitness if minimizing
    m = -1 if pop.optimization == "min" else 1
    visited = {}
    getFitness(ind)
    while True:
        print()
        print(f"{ind.fitness = }")
        ind_representation_str = "".join([str(i) for i in ind.representation])
        if ind_representation_str in visited.keys():
            print(f"{ind_representation_str = } found in visited individuals")
            ind = copy.deepcopy(visited[ind_representation_str])
            ind.number_n_visited += 1
            if ind.number_n_visited == ind.len_max:
                print("maximum neighbours visited in plateau")
                return ind
        else:
            print(f"{ind_representation_str = }")
            getNeighbours(ind)
            for n in ind.neighbours:
                getFitness(n)
            # Calculate fitness of neighbours given optimization type by m
            ns_fitness = ([n.fitness for n in ind.neighbours] * np.array(m)).tolist()
            # How many neighbours have the best fitness
            ind.len_max = sum((np.array(ns_fitness) == max(ns_fitness)))
            ind.number_n_visited = 0

        # Get best neighbour
        best_n_idx = ns_fitness.index(max(ns_fitness))
        best_n = ind.neighbours[best_n_idx]
        # print(f"{m = } // {best_n.fitness = } // {ind.fitness = }")
        print(
            f"{best_n.fitness = } ;; {ind.fitness = } ;; diff = {ind.fitness - best_n.fitness}"
        )
        if (best_n.fitness * m) > (ind.fitness * m):
            # if (ind.fitness - best_n.fitness) * m < 0:
            print(f"{(best_n.fitness * m) = } > {(ind.fitness * m) = }")
            visited = {}
            ind = copy.deepcopy(best_n)

        elif best_n.fitness == ind.fitness:
            print(f"found plateau on {best_n.representation}")
            # Change the best neighbour's fitness value to never be max again
            ind.neighbours[best_n_idx].fitness -= 1 * m
            visited[ind_representation_str] = ind
            ind = copy.deepcopy(best_n)
        else:
            return ind
