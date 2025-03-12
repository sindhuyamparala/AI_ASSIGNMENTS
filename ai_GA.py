import random

POPULATION_SIZE = 100

GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

TARGET = "Sindhu"

class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(cls):
        return random.choice(GENES)

    @classmethod
    def create_gnome(cls):
        gnome_len = len(TARGET)
        return [cls.mutated_genes() for _ in range(gnome_len)]

    def mate(self, par2):
        child_chromosome = []

        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())

        return Individual(child_chromosome)

    def cal_fitness(self):
        return sum(1 for gs, gt in zip(self.chromosome, TARGET) if gs != gt)

def initialize_population():
    return [Individual(Individual.create_gnome()) for _ in range(POPULATION_SIZE)]

def select_parents(population):
    return random.sample(population, k=2)

def crossover(parent1, parent2):
    child_chromosome = []
    for gp1, gp2 in zip(parent1.chromosome, parent2.chromosome):
        prob = random.random()
        if prob < 0.45:
            child_chromosome.append(gp1)
        elif prob < 0.90:
            child_chromosome.append(gp2)
        else:
            child_chromosome.append(Individual.mutated_genes())

    return Individual(child_chromosome)

def mutate_chromosome(chromosome):
    return [random.choice(GENES) if random.random() < 0.1 else gene for gene in chromosome]

def mutate(individual):
    return Individual(mutate_chromosome(individual.chromosome))

def main():
    global POPULATION_SIZE
    generation = 1
    found = False
    population = initialize_population()

    while not found:
        population = sorted(population, key=lambda x: x.fitness)

        if population[0].fitness == 0:
            found = True
            break

        new_generation = []
        new_generation.extend(population[:int(0.1 * POPULATION_SIZE)])

        for _ in range(int(0.9 * POPULATION_SIZE)):
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            new_generation.append(child)
        population = new_generation

        print("Generation: {}\tString: {}\tFitness: {}".format(
            generation,
            "".join(population[0].chromosome),
            population[0].fitness))
        generation += 1

    print("Final Generation: {}\tString: {}\tFitness: {}".format(
        generation,
        "".join(population[0].chromosome),
        population[0].fitness))

if __name__ == '__main__':
    main()