import numpy as np

from conway_config import FIELD_SIZE


def lifetime_step_numpy(field: 'np.ndarray') -> 'np.ndarray':
    rolled = np.zeros((8, FIELD_SIZE, FIELD_SIZE), dtype=np.int8)
    shifts = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    for l, (di, dj) in enumerate(shifts):
        rolled[l] = np.roll(np.roll(field, di, axis=0), dj, axis=1)
    
    neighboors = rolled.sum(axis=0)

    result = np.zeros_like(field)
    mask = (((field == 0) & (neighboors == 3)) | 
            ((field == 1) & ((neighboors == 2) | (neighboors == 3))))
    result[mask] = 1
    
    return result