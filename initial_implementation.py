import random
import pygad
import os
import wandb
import numpy as np
from fitness import fitness_func_energy, on_generation, on_generation_xlastovka
## basic configuration
api_key = open("wandb_api_key.txt", "r")
key = api_key.read()
api_key.close()
os.environ["WANDB_API_KEY"] = key
on_gen_list = [on_generation,on_generation_xlastovka]
SEED = 1234
random.seed(SEED)


for on_gen_func in on_gen_list:
    hyperparameters_default = dict(
    seed=SEED,
    num_bits=64,
    num_generations=1000000,
    num_parents_mating=2,
    sol_per_pop=5,
    parent_selection_type="rank",
    mutation_type="random",
    crossover_type="scattered",
    mutation_percent_genes=10,
    on_gen_list = on_gen_func.__name__
    )
    
    wandb.init(
        project="lssorel_tests",
        group="final_tests",
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
        num_generations=num_generations,
        num_parents_mating=num_parents_mating,
        sol_per_pop=sol_per_pop,
        num_genes=num_bits,
        init_range_low=-1,
        init_range_high=2,
        gene_type=int,
        gene_space=[-1,1],
        fitness_func=fitness_func_energy,
        on_generation=on_gen_func,
        stop_criteria="reach_0.0",
        random_seed=SEED,
        mutation_type = mutation_type,
        parent_selection_type=parent_selection_type,
        crossover_type=crossover_type,
        mutation_percent_genes=10,
        

    )

    ga_entity.run()
    wandb.finish()