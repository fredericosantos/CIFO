import random, copy
from main import Population, Individual
import numpy as np


# Should return representation of individual

def fps(pop: Population) -> list:
    m = -1 if pop.optimization == "min" else 1

    # If the fitness is negative, return fitness = 0
    # Make sure the fitness number works in positive numbers
    total_fitness = sum([i.fitness if i.fitness > 0 else 0 for i in pop.individuals]) * m

    # Make a weighted choice
    choice = np.random.choice([i for i, _ in enumerate(pop.individuals)], p=a/sum(a))
    # return the representation of the individual
    return pop.individuals[choice].representation

def tournament(pop: Population, size: int):
    tournament = random.sample(pop.individuals, size=size)
    m = -1 if pop.optimization == "min" else 1
    winner = sorted(pop.individuals, key= lambda i: i.fitness * m)[0]
    # return the representation of the individual
    return winner.representation