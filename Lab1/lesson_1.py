from data import distance_matrix, cities
from random import shuffle

class Path:
    def __init__(self, representation) -> None:
        self.representation = representation
        self.distance = distance(self.representation)

    def __repr__(self) -> str:
        return f"Path: {self.representation}; Distance: {self.distance}"

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]
    
def distance(path):
    distance = 0
    for i in range(len(path)):
        distance += distance_matrix[path[i-1]][path[i]]
    return distance

if __name__ == '__main__':
    cities_n = [i for i in range(len(cities))]
    shuffle(cities_n)
    cities_n = Path(cities_n)