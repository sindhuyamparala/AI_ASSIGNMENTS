import random

class BinPackingGA:
    def __init__(self, items, bin_capacity, population_size=50, generations=100, mutation_rate=0.1):
        self.items = items
        self.bin_capacity = bin_capacity
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        return [random.sample(range(len(self.items)), len(self.items)) for _ in range(self.population_size)]

    def fitness(self, chromosome):
        bins = []
        for item_idx in chromosome:
            placed = False
            for bin in bins:
                if sum(bin) + self.items[item_idx] <= self.bin_capacity:
                    bin.append(self.items[item_idx])
                    placed = True
                    break
            if not placed:
                bins.append([self.items[item_idx]])
        return len(bins)

    def select_parents(self):
        sorted_population = sorted(self.population, key=self.fitness)
        return sorted_population[:2]

    def crossover(self, parent1, parent2):
        point = random.randint(1, len(self.items) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2

    def mutate(self, chromosome):
        if random.random() < self.mutation_rate:
            idx1, idx2 = random.sample(range(len(chromosome)), 2)
            chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
        return chromosome

    def run(self):
        for _ in range(self.generations):
            new_population = []
            for _ in range(self.population_size // 2):
                parent1, parent2 = self.select_parents()
                child1, child2 = self.crossover(parent1, parent2)
                new_population.extend([self.mutate(child1), self.mutate(child2)])
            self.population = new_population
        return min(self.population, key=self.fitness)

if __name__ == "__main__":
    items = [4, 8, 1, 4, 2, 6, 7]
    bin_capacity = 10
    bin_packing = BinPackingGA(items, bin_capacity)
    best_packing = bin_packing.run()
    print("Optimal Bin Packing Order:", best_packing)
