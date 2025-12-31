import numpy as np
import time

import field_generator
from config import (
    USE_NUMPY,
    USE_NUMPY_UNEFFECTIVE, 
    STEPS, 
    FIELD_SIZE, 
    VERBOSE, 
    ANIMATION
    )
import conway_stdPyArr
import conway_numpy
import animated_field


def load_field(filename: str):
    with open(filename, "r") as f:
        lines = f.readlines()
    lines = lines[:FIELD_SIZE]
    if USE_NUMPY:
        field_array = np.zeros((FIELD_SIZE, FIELD_SIZE), dtype=np.int8)
        for i, line in enumerate(lines):
            line = line[:FIELD_SIZE]
            for j, char in enumerate(line):
                field_array[i, j] = 1 if char == "1" else 0
        return field_array
    else:
        field_list = []
        for line in lines:
            row = [1 if char == "1" else 0 for char in line]
            field_list.append(row)
        return field_list
    

def simulate_life(field):
    if USE_NUMPY:
        if USE_NUMPY_UNEFFECTIVE:
            sim_func = conway_numpy.lifetime_step_numpy_uneffective 
        else:
            sim_func = conway_numpy.lifetime_step_numpy
    else:
        sim_func = conway_stdPyArr.lifetime_step_stdPyArr

    history = []
    
    if USE_NUMPY:
        history.append(field.copy())
    else:
        history.append([row[:] for row in field])
    
    start_time = time.time()

    for _ in range(1, STEPS + 1):
        field = sim_func(field)

        if USE_NUMPY:
            history.append(field.copy())
        else:
            history.append([row[:] for row in field])
    
    total_time = time.time() - start_time
    print(total_time)

    return history


def main():
    if VERBOSE:
        from config import FIELD_SIZE, STEPS

        print("=" * 30)
        print("THE CONWAY'S GAME OF LIFE")
        print("=" * 30)
        print(f"field size: {FIELD_SIZE}x{FIELD_SIZE}")
        print(f"steps: {STEPS}")
        print("using ", end="")
        if USE_NUMPY:
            print(f"{"uneffective numpy" if USE_NUMPY_UNEFFECTIVE
                     else "numpy"}")
        else:
            print("lists")
    
    field_file = field_generator.get_field()
    if VERBOSE:
        print(f"using file: {field_file}")
    field = load_field(field_file)

    history = simulate_life(field)

    if ANIMATION:
        animated_field.animate_history(history)


if __name__ == "__main__":
    main()
