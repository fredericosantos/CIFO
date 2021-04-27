from main import Individual
from tsp_data import distance_matrix
import numpy as np


def getFitness(individual: Individual, searchSpace: list):
    """Calculate individual fitness and update the individual's fitness.

    Args:
        individual (Individual): initiated individual class
        searchSpace (list): Search space
    """
    # simplify code
    rep = individual.representation
    # calculate fitness
    fitness = [searchSpace[rep[i - 1]][rep[i]] for i, _ in enumerate(rep)]
    # update individual's fitness
    individual.fitness = sum(fitness)

def getNeighbours(individual: Individual):
    """Generate neighbors of individual by swapping each node pair.

    Args:
        individual (Individual): individual to which we update the neighbors
    """
    rep = individual.representation
    neighbours = [rep.copy() for _ in enumerate(rep[:-1])]
    for i, indv in enumerate(neighbours):
        indv[i], indv[i+1] = indv[i+1], indv[i]
    individual.neighbours = neighbours

