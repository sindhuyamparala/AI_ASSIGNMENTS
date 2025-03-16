import random
import numpy as np

class JobSchedulingGA:
    def __init__(self, jobs, machines, population_size=50, generations=100, mutation_rate=0.1):
        self.jobs = jobs  
        self.machines = machines 
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        return [np.random.randint(0, self.machines, len(self.jobs)).tolist() for _ in range(self.population_size)]

    def fitness(self, chromosome):
        machine_loads = [0] * self.machines
        for job, machine in enumerate(chromosome):
            machine_loads[machine] += self.jobs[job]
        return -max(machine_loads) 

    def select_parents(self):
        fitness_scores = [self.fitness(chromosome) for chromosome in self.population]
        total_fitness = sum(fitness_scores)
        probabilities = [f / total_fitness for f in fitness_scores]
        parents = random.choices(self.population, weights=probabilities, k=2)
        return parents[0][:], parents[1][:] 

    def crossover(self, parent1, parent2):
        point1, point2 = sorted(random.sample(range(len(self.jobs)), 2))
        child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
        child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
        return child1, child2

    def mutate(self, chromosome):
        if random.random() < self.mutation_rate:
            index = random.randint(0, len(chromosome) - 1)
            chromosome[index] = random.randint(0, self.machines - 1)
        return chromosome

    def run(self):
        for _ in range(self.generations):
            new_population = []
            for _ in range(self.population_size // 2):
                parent1, parent2 = self.select_parents()
                child1, child2 = self.crossover(parent1, parent2)
                new_population.extend([self.mutate(child1), self.mutate(child2)])
            self.population = new_population
        return min(self.population, key=lambda x: -self.fitness(x))

if __name__ == "__main__":
    jobs = [2, 5, 8, 3, 6, 7]
    machines = 3
    job_scheduler = JobSchedulingGA(jobs, machines)
    best_schedule = job_scheduler.run()
    print("Optimal Job Schedule:", best_schedule)