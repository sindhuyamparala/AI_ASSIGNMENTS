import random

knapsack_capacity = 70
item_weights = [15, 25, 35, 45, 55]
item_values = [80, 110, 130, 160, 220]
population_size = 50
generations = 100
mutation_rate = 0.1

def generate_chromosome():
    return [random.choice([0, 1]) for _ in range(len(item_weights))]

def initialize_population():
    return [generate_chromosome() for _ in range(population_size)]

def calculate_fitness(chromosome):
    total_value = sum(c * v for c, v in zip(chromosome, item_values))
    total_weight = sum(c * w for c, w in zip(chromosome, item_weights))
    
    return total_value if total_weight <= knapsack_capacity else 0

def select_parents(population):
    fitness_scores = [calculate_fitness(chromosome) for chromosome in population]
    total_fitness = sum(fitness_scores)
    parents = []
    while len(parents) < population_size:
        selected_index = random.choices(range(len(population)), weights=fitness_scores)[0]
        parents.append(population[selected_index])
    return parents

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(chromosome):
    mutation_point = random.randint(0, len(chromosome) - 1)
    chromosome[mutation_point] = 1 - chromosome[mutation_point]

def apply_mutation(population):
    for chromosome in population:
        if random.random() < mutation_rate:
            mutate(chromosome)

def genetic_algorithm():
    population = initialize_population()
    for generation in range(generations):
        parents = select_parents(population)
        offspring = []
        for i in range(0, len(parents), 2):
            if i + 1 < len(parents):
                child1, child2 = crossover(parents[i], parents[i + 1])
                offspring.extend([child1, child2])
        apply_mutation(offspring)
        population = offspring
    best_solution = max(population, key=calculate_fitness)
    return best_solution, calculate_fitness(best_solution)

best_solution, best_fitness = genetic_algorithm()

print("Best Solution (Selected items):", best_solution)
print("Best Fitness (Total value):", best_fitness)