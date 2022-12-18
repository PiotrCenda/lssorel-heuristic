import random
import pygad
import os
import wandb
import numpy as np
from fitness import fitness_func_energy, on_generation
## basic configuration
api_key = open("wandb_api_key.txt", "r")
key = api_key.read()
api_key.close()
os.environ["WANDB_API_KEY"] = key

SEED = 1234
random.seed(SEED)

hyperparameters_default = dict(
    seed=SEED,
    num_bits=16,
    num_generations=10000,
    num_parents_mating=2,
    sol_per_pop=5,
    parent_selection_type="rank",
    mutation_type="adaptive",
    crossover_type="scattered",
    mutation_percent_genes=10,
    mode="inference",
)

wandb.init(
    project="lssorel_tests",
    group="initial_sweep",
    config=hyperparameters_default,
)


config = wandb.config

num_bits = config.num_bits
num_generations = config.num_generations
num_parents_mating = config.num_parents_mating
sol_per_pop = config.sol_per_pop
parent_selection_type = config.parent_selection_type
crossover_type = config.crossover_type
mutation_type = config.mutation_type


ga_entity = pygad.GA(
    num_generations=10000,
    num_parents_mating=num_parents_mating,
    sol_per_pop=sol_per_pop,
    num_genes=num_bits,
    init_range_low=-1,
    init_range_high=2,
    gene_type=int,
    gene_space=[-1,1],
    fitness_func=fitness_func_energy,
    on_generation=on_generation,
    stop_criteria="reach_0.0",
    random_seed=SEED,
    mutation_type = mutation_type,
    parent_selection_type=parent_selection_type,
    crossover_type=crossover_type
    #mutation_probability=0.4,
    

)

ga_entity.run()