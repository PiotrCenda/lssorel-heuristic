import timeit
import numpy as np
#import wandb
import xlastovka

def on_generation_xlastovka(ga_instance):
    """Determine what happens with the beginning of every generation."""
    print(f"Generation = {ga_instance.generations_completed}")
    print(f"Best solution fitness pre local= {ga_instance.best_solutions_fitness[-1]}")

    for n,old_solution in enumerate(ga_instance.population):
        old_energy = ga_instance.last_generation_fitness[n]
        new_solution, new_fitness = xlastovka.xlastovka_search(old_solution, len(old_solution), old_energy,max_iter=1000)
        if new_fitness > old_energy:
            ga_instance.population[n] = new_solution
            ga_instance.last_generation_fitness[n] = new_fitness
        best_solution, best_solution_fitness, best_match_idx = ga_instance.best_solution(
            pop_fitness=ga_instance.last_generation_fitness
            )
        ga_instance.best_solutions_fitness[-1] = best_solution_fitness
    print(f"Best solution fitness post local= {ga_instance.best_solutions_fitness[-1]}")
    # wandb.log(
    #     {
    #         "fitness": ga_instance.best_solutions_fitness[-1],
    #         "generation": ga_instance.generations_completed,
    #     }
    # )
def on_generation(ga_instance):
    """Determine what happens with the beginning of every generation."""
    print(f"Generation = {ga_instance.generations_completed}")
    print(f"Best solution fitness pre local= {ga_instance.best_solutions_fitness[-1]}")
    # wandb.log(
    #     {
    #         "fitness": ga_instance.best_solutions_fitness[-1],
    #         "generation": ga_instance.generations_completed,
    #     }
    # )





    

def fitness_func_energy(solution, sol_idx=None):
    """Calculates energy of sequence solution.

    Args:
        solution: Numpy array consisting of -1 and 1. 
        sol_idx: Variable is requested by pygad
    """
    return xlastovka.calculate_energy(solution)


if __name__ == "__main__":
    random_solution_sequence = np.random.choice([-1, 1], size=64, replace=True)
    t = timeit.Timer(lambda: fitness_func_energy(random_solution_sequence)) 
    energy = fitness_func_energy(random_solution_sequence)
    print(f"Energy: {energy}")
    print(f"Runtime: {t.timeit(30)}s\n")
    