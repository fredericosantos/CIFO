import random, copy
from main import Population, Individual
import numpy as np


def GAO(
    pop: Population, generations: int, select, crossover, mutation, getFitness
) -> Individual:
    # Check if individuals have fitness
    if not pop.individuals[0].fitness:
        for i in pop.individuals:
            getFitness(i)
    # Check if we want elitism and how many elites we keep
    if (pop.n_elites > 0):
        pop_prime = sorted(pop.individuals, key= lambda i: i.fitness)[:pop.n_elites]
    else:
        pop_prime = []
        
    # Evolve the rest of the population
    while len(pop_prime) < len(pop):
        # Select parents from population the representations of the parents
        i1, i2 = select(pop), select(pop)

        # Apply crossover ~ probability is given to function
        i1, i2 = crossover(i1, i2)

        for i in [i1, i2]:
            # Apply mutation ~ probability is given to function
            i = mutate(i)
            # Create individual and get its fitness
            i = Individual(representation=i)
            getFitness(i)
        
        new_pop.append(i1)
        if len(new_pop) < len(pop):
            new_pop.append(i2)
    
    pop.individuals = new_pop