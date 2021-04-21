from random import choice, uniform
from math import exp

def hill_climb(search_space, log=0):
    """Hill climbs a given search space.

    Args:
        search_space (Population): A Population of solutions
        log (int, optional): Prints info while running if set to 1. Defaults to 0.

    Raises:
        Exception: When unsure if facing maximization or minimization problem.

    Returns:
        Individual: Local optima Individual found in the search.
    """
    # Select a random solution
    start = choice(search_space)
    position = start
    # Counter to ensure we don't loop
    # infinitely if stuck in a plateu of optimas
    iter_plateu = 0
    
    if log == 1:
        print(f"Initial position: {start}")

    while True:
        # Return solution if we found same fitness
        # 5 times - to avoid infinite loop
        if iter_plateu >= 5:
            print(f"Best solution found: {position.fitness}")
            return position

        n = position.get_neighbours()
        n_fit = [i.fitness for i in n]

        if search_space.optim == "max":
            best_n = n[n_fit.index(max(n_fit))]
            if best_n.fitness > position.fitness:
                if log == 1:
                    print(f"Found better solution: {best_n.fitness}")
                iter_plateu = 0
                position = best_n
            elif best_n.fitness == position.fitness:
                if log == 1:
                    print(f"Found better solution: {best_n.fitness}")
                iter_plateu += 1
                position = best_n
            else:
                print(f"Best solution found: {position.fitness}")
                return position

        elif search_space.optim == "min":
            best_n = n[n_fit.index(min(n_fit))]
            if best_n.fitness < position.fitness:
                if log == 1:
                    print(f"Found better solution: {best_n.fitness}")
                iter_plateu = 0
                position = best_n
            elif best_n.fitness == position.fitness:
                if log == 1:
                    print(f"Found better solution: {best_n.fitness}")
                iter_plateu += 1
                position = best_n
            else:
                print(f"Best solution found: {position.fitness}")
                return position
        
        else:
            raise Exception("Problem doesn't specify if minimization or maximization.")


def sim_annealing(search_space, L, c, alpha=0.99):
    # Initialize solution from search space (randomly)
    # Let solution equal starting position
    position = choice(search_space)
    elite = position
    # Initialize L and c
    L_, c_ = L, c 
    # While loop until termination condition 
    while c_ > c/10:
        # Repeat L times (for loop)
        for _ in range(L_):
            # Generate neighbour 
            sol = choice(position.get_neighbours())
            # if neigh is better or equal take
            if sol.fitness >= position.fitness:
                position = sol
                if position.fitness > elite.fitness:
                    elite = position
                    print(f"New Elite: {elite.fitness}")
            # elif some weird function, take if met
            elif uniform(0, 1) < (pc := exp(-abs(sol.fitness - position.fitness)/c_)):
                position = sol
        # Update c and L
        c_ *= alpha
    print(f"Solution ended at: {position.fitness}")
    print(f"Best solution found: {elite.fitness}")
    return elite