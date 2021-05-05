import numpy as np


class Population:
    """Population for optimization
    """

    def __init__(self, individuals: list, optimization: str, n_elites: int = 0):
        """Args:
            individuals (list): List of Individual
            optimization (str): max or min
            n_elites (int, optional): Number of individuals to retain at each generation. Defaults to 0.

        Raises:
            ValueError: [description]
        """
        self.individuals = individuals
        self.optimization = optimization.lower()
        self.n_elites = n_elites
        if n_elites > 0:
            self.elites = []
        if self.optimization not in ["min", "max"]:
            raise ValueError("Set optimization to min or max.")

    def selection(self, func, *args, **kwargs) -> None:
        func(self, *args, **kwargs)

    def crossover(self, func, *args, **kwargs) -> None:
        func(self, *args, **kwargs)

    def mutation(self, func, *args, **kwargs) -> None:
        func(self, *args, **kwargs)

    def evolve(self) -> None:
        pass


class Individual:
    def __init__(self, representation: list) -> None:
        self.representation = representation
        self.fitness = None
        self.neighbours = None

    def __len__(self):
        return len(self.representation)

    def __repr__(self):
        return f"Individual <{self.fitness}>"


# TODO create function that generates a population with abstract code
def generatePopulation() -> Population:
    pass
