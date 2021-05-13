import random, copy
from main import Individual
import numpy as np


def gene_mutation(representation: list, p_mutation: float, valid_set: list) -> list:
    for i, gene in enumerate(representation):
        if random.random() <= p_mutation:
            valid_set_c = valid_set.copy()
            valid_set_c.remove(gene)
            representation[i] = random.choice(valid_set_c)
    return representation


def single_mutation(representation: list, valid_set: list) -> list:
    # get random point in representation
    idx = random.randint(0, len(representation) - 1)
    # copy valid set of values and make sure we don't get the same value
    valid_set_c = valid_set.copy()
    valid_set_c.remove(representation[idx])

    # change the representation point
    representation[idx] = random.choice(valid_set_c)
    return representation

def swap_mutation(representation: list, p_mutation: float, n_mutations: int) -> list:
    idx1, idx2 = random.sample(range(len(representation)), 2)
    r = representation
    r[idx1], r[idx2] = r[idx2], r[idx1]

    return r