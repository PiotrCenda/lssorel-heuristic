from typing import Tuple, List
from fitness import fitness_func_energy


def flip_bit(coord: List[int], i: int) -> List[int]:
    """Flips i-th bit of given sequence.

    Args:
        coord (List[int]): sequence
        i (int): i-th bit to flip

    Returns:
        List[int]: flipped sequence
    """
    
    coord[i] = 1 - coord[i]
    
    return coord


def xlastovka_search(L: int, valueTarget: int) -> Tuple[int, int]:
    """Performs xLastovka local search algorithm.

    Args:
        L (int): instance size
        valueTarget (int): best upper bound

    Returns:
        Tuple[int, int]: (coord) best coordinate and best value
    """
    
    # priority queue of pairs (coord, value)
    PQ = list()

    # storage of pivots
    closePivots = set()

    # initialize coordinate
    coord = RandomSolution(L)  # TODO
    
    # evaluation
    value =  fitness_func_energy(coord)
    
    # stopping criteria
    if value <= valueTarget:  # TODO: check sign and whole maximize/minimize thing 
        return coord, value 
    
    PQ.append((coord, value))
    
    while value > valueTarget:
        coord, _ = PQ.pop(0)
        
        # search neighborhood
        for i in range(1, (L + 1) / 2 + 1):
            # flip i-th bit
            sFlipped = flip_bit(coord, i)
            
            # skip if already pivot
            if sFlipped in closePivots:
                continue
            else:
                value = fitness_func_energy(sFlipped)
            
            # stopping criteria
            if value <= valueTarget:  # TODO: again, check sign and whole maximize/minimize thing
                break
            else:
                PQ.append((sFlipped, value))
            
        closePivots.add(coord)
    
    return coord, value
