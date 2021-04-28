import matplotlib.pyplot as plt


def evaluate(number):
    """A fitness function that takes a base-10 number,
    transforms it into base-2 (binary), and returns the
    number of 1's occuring in the binary representation.

    Args:
        number (int): the integer you want to get the
        fitness for.

    Returns:
        int: the number of 1's in the binary representation.
    """
    return "{0:04b}".format(number).count("1")


def get_neighbours(individual):
    """A neighbourhood funciton for the int / binary
    optimization problem.

    Args:
        individual (int): an int between 1 and 15

    Returns:
        list: a neighbourhood of individuals
    """
    n1 = individual - 1
    n2 = individual + 1
    return [n1, n2]
