import numpy as np


class Population:
    def __init__(self, individuals: list, optimization: "min / max"):
        self.individuals = individuals
        self.optimization = optimization.lower()
        # self.replacement = replacement
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