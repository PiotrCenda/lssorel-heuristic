from typing import Tuple, List
import numpy as np
def calculate_energy(sequence):
    autocorrelations = np.correlate(sequence, sequence, 'full')
    autocorrelations = autocorrelations[-len(sequence)+1:]
    energy =  np.sum(np.power(autocorrelations, 2))
    return -energy


def flip_bit(coord: List[int], i: int) -> List[int]:
    """Flips i-th bit of given sequence.

    Args:
        coord (List[int]): sequence
        i (int): i-th bit to flip

    Returns:
        List[int]: flipped sequence
    """
  
    coord[i] = - coord[i]

    return coord


def xlastovka_search(sequence : List[int], L: int, valueTarget: int, max_iter : int = 1000) -> Tuple[int, int]:
    """Performs xLastovka local search algorithm.

    Args:
        sequence (List[int]): initial sequence of bits
        L (int): instance size
        valueTarget (int): best upper bound
        max_iter (int, optional): maximum number of iterations for local search. Defaults to 1000.

    Returns:
        Tuple[int, int]: (coord) best coordinate and best value
    """
    
    # priority queue of pairs (coord, value)
    PQ = list()

    # storage of pivots
    closePivots = []

    # initialize coordinate
    coord = list(sequence)  # TODO
    
    # evaluation
    value =  valueTarget

    PQ.append((coord, value))

    n_iter = 0
    while n_iter < max_iter:
        n_iter += 1
    
        if len(PQ) == 0:
            break ## if there are no more unique pairs to check break the loop
        else:
            coord, _ = PQ.pop(0)
    
        # search neighborhood
        for i in range(0, int(L/ 2) + 1): ## removed L+1 as it was float
            # flip i-th bit
            sFlipped = flip_bit(coord, i)
            # skip if already pivot
            
            if sFlipped in closePivots:
                
                continue
            else:
                value = calculate_energy(sFlipped)
               
            # stopping criteria
            if value > valueTarget:
                return sFlipped, value
                # stop_flag = True  ## if we found better value,break the loop and return the 
                
                # break
            else:
                coord = sFlipped
                PQ.append((sFlipped, value))
            
        closePivots.append(coord)
    # if value < valueTarget:
    #     ## if we failed to find new best value, return the old one with old coords
    #     best_value = valueTarget
    #     coord = sequence
    # else:
    #     best_value = value
    return coord, valueTarget
if __name__ == "__main__":
    for _ in range(1000):
        random_solution_sequence = np.random.choice([-1, 1], size=16, replace=True)
        energy_init = calculate_energy(random_solution_sequence)
        coord,energy = xlastovka_search(random_solution_sequence,len(random_solution_sequence), energy_init)
        if energy_init > energy:
            print(f"Something went wrong! New fitness value is {energy}, old is {energy_init}")
    print(f"New fitness value is {energy}, old is {energy_init}")

