import random, copy
from main import Population, Individual
import numpy as np


def GAO(
    pop: Population, generations: int, select, crossover, mutation
) -> Individual:
    for i in pop.individuals:
        pop.fitness(i)
    # Check if we want elitism and how many elites we keep
    if (pop.n_elites > 0):
        pop_prime = sorted(pop.individuals, key= lambda i: i.fitness)[:pop.n_elites]
    else:
        pop_prime = []
    new_pop = []
    # Evolve the rest of the population
    while len(pop_prime) < len(pop):
        # Select parents from population the representations of the parents
        i1, i2 = pop.select(), pop.select()

        # Apply crossover ~ probability is given to function
        i1, i2 = pop.crossover(i1, i2)

        for i in [i1, i2]:
            # Apply mutation ~ probability is given to function
            i = pop.mutation(i)
            # Create individual and get its fitness
            i = Individual(representation=i)
            pop.fitness(i)
        
        new_pop.append(i1)
        if len(new_pop) < len(pop):
            new_pop.append(i2)
    
    pop.individuals = new_pop