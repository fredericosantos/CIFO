import random, copy
from library.main import Individual
import numpy as np


def GAO(
    pop,
    generations: int,
    tournament_size: int,
    p_crossover: float = 0.1,
    p_mutation: float = 0.05,
    n_mutations: int = 1,
):
    m = -1 if pop.optimization == "min" else 1
    for _ in range(generations):
        for i in pop.individuals:
            pop.fitness(i)
        # Check if we want elitism and how many elites we keep
        if pop.n_elites > 0:
            pop_prime = sorted(pop.individuals, key=lambda i: i.fitness * m, reverse=True)[:pop.n_elites]
        else:
            pop_prime = []
        # Evolve the rest of the population
        while len(pop_prime) < len(pop.individuals):
            # Select parents from population the representations of the parents
            i1, i2 = pop.selection(tournament_size), pop.selection(tournament_size)

            # Apply crossover ~ probability is given to function
            i1, i2 = pop.crossover(i1, i2, p_crossover)

            for i in [i1, i2]:
                # Apply mutation ~ probability is given to function
                i = pop.mutation(i, p_mutation, n_mutations)
                # Create individual and get its fitness
                i = Individual(representation=i)
                pop.fitness(i)
                if len(pop_prime) < len(pop.individuals):
                    pop_prime.append(i)

        pop.individuals = copy.deepcopy(pop_prime)
        pop.elites = sorted(pop.individuals, key=lambda i: i.fitness * m, reverse=True)[:pop.n_elites]
