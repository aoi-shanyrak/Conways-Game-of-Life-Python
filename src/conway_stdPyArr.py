from typing import List

from config import FIELD_SIZE


def _count_neighboors_stdPyArr(i: int, j: int, field: List[List[0 | 1]]) -> int:
    count = 0
    for di in range(3):
        for dj in range(3):
            if di == 1 and dj == 1:
                continue
            ti = FIELD_SIZE - 1 if di == 0 else di - 1
            tj = FIELD_SIZE - 1 if dj == 0 else dj - 1

            ni = (i + ti) % FIELD_SIZE
            nj = (j + tj) % FIELD_SIZE

            count += field[ni][nj]
    
    return count


def lifetime_step_stdPyArr(field: List[List[0 | 1]]) -> List[List[0 | 1]]:
    result = [[0 for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]
    for i in range(FIELD_SIZE):
        for j in range(FIELD_SIZE):
            count = _count_neighboors_stdPyArr(i, j, field)
            if field[i][j]:
                result[i][j] = 1 if 2 <= count <= 3 else 0
            else:
                result[i][j] = 1 if count == 3 else 0
    return result