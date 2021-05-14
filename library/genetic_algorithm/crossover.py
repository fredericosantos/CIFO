import random, copy

def single_point_xo(p1: list, p2: list):
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
