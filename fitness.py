import timeit
import numpy as np


def on_generation(ga_instance):
    """Determine what happens with the beginning of every generation."""
    print(f"Generation = {ga_instance.generations_completed}")
    print(f"Best solution fitness = {ga_instance.best_solutions_fitness[-1]}")

    

def fitness_func_energy(solution, sol_idx=None):
    """Calculates energy of sequence solution.

    Args:
        solution: Numpy array consisting of -1 and 1. 
        sol_idx: Variable is requested by pygad
    """
    # off-peak autocorrelations

    autocorrelations = np.correlate(solution, solution, 'full')
    autocorrelations = autocorrelations[-len(solution)+1:]
    # the energy
    solution_fitness = np.sum(np.power(autocorrelations, 2))
    ## I suppose we only need to minimize energy 
    return -solution_fitness


if __name__ == "__main__":
    random_solution_sequence = np.random.choice([-1, 1], size=10000, replace=True)
    print(f"Sequence: {random_solution_sequence}\n")
    
    t = timeit.Timer(lambda: fitness_func_energy(random_solution_sequence)) 
    autocorrelation, energy = fitness_func_energy(random_solution_sequence)
    
    print(f"Autocorrelation: {autocorrelation}")
    print(f"Energy: {energy}")
    print(f"Runtime: {t.timeit(30)}s\n")
    