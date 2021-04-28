from main import Individual
from ks_data import weights, values, capacity
import numpy as np


def getFitness(individual: Individual):
    """Calculate individual fitness and update the individual's fitness.

    Args:
        individual (Individual): initiated individual class
    """
    # simplify code
    rep = individual.representation
    # calculate fitness
    individual.weight = sum(rep * np.array(weights))
    if individual.weight > capacity:
        individual.fitness = capacity - individual.weight
    else:
        individual.fitness = sum(rep * np.array(values))

def getNeighbours(individual: Individual):
    """Generate neighbors of individual by swapping one bit at a time in each position

    Args:
        individual (Individual): individual to which we update the neighbors
    """
    rep = individual.representation
    neighbours = [rep.copy() for _ in enumerate(rep[:-1])]
    for i, indv in enumerate(neighbours):
        ind[i] ^= 1
    individual.neighbours = neighbours


if __name__ == "__main__":
    pass