import random, copy
from ssl import OP_NO_TLSv1_1


def single_point_co(p1: list, p2: list):
    poopoo = random.randint(1, len(p1))
    offspring1 = p1[:poopoo] + p2[:poopoo]
    offspring2 = p1[poopoo:] + p2[poopoo:]

    return offspring1, offspring2


def cycle_co(p1: list, p2: list):
    r_len = len(p1)
    offspring1, offspring2 = {}, {}
    keys = offspring1.keys()
    idx = random.choice(list(set(range(r_len)) - set(keys)))
    while len(keys) < r_len:
        if idx in keys:
            idx = random.choice(list(set(range(r_len)) - set(keys)))
            p1, p2 = p2, p1
        else:
            offspring1[idx] = p1[idx]
            offspring2[idx] = p2[idx]
            idx = p2.index(p1[idx])
    o1 = [offspring1[i] for i in range(r_len)]
    o2 = [offspring2[i] for i in range(r_len)]
    return o1, o2


def arithmetic_co(p1: list, p2: list):
    # set alpha
    a = random.uniform(0, 1)
    o1 = [p1[i] * a + (1 - a) * p2[i] for i, _ in enumerate(p1)]
    o2 = [p2[i] * a + (1 - a) * p1[i] for i, _ in enumerate(p1)]
    return o1, o2


def pmx_co(p1: list, p2: list):
    idx1, idx2 = sorted(random.sample(range(len(p1)), 2))
    o1, o2 = p1, p2
    p1_substring = p1[idx1:idx2]
    p2_substring = p2[idx1:idx2]
    o1_dict = {}
    o2_dict = {}

    for i, n in enumerate(p2_substring):
        o1_dict[o1.index(n)] = p1_substring[i]
    for i, n in enumerate(p1_substring):
        o2_dict[o2.index(n)] = p2_substring[i]
    o1[idx1:idx2] = p2_substring
    o2[idx1:idx2] = p1_substring

    for i, v in o1_dict.items():
        o1[i] = v
    for i, v in o2_dict.items():
        o2[i] = v
    return o1, o2


if __name__ == "__main__":
    p1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    p2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]

    print(pmx_co(p1, p2))
