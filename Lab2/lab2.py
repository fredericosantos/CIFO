"""
base 10: 1 to 15
base 2: 0010 to 1111
fitness: sum of numbers in base 2

"""
import random
import utils

bin_set = [i for i in range(1, 60)]


def eval(value):
    return utils.evaluate(value)


def hillClimb(search_space):
    # random solution
    x = random.choice(search_space)
    local_optimum = x
    while True:
        neighbours = utils.get_neighbours(x)
        for neighbor in neighbours:
            better_optimum = False
            if eval(neighbor) > eval(local_optimum):
                local_optimum = neighbor
                print(local_optimum)
                better_optimum = True
        if not better_optimum:
            return local_optimum

