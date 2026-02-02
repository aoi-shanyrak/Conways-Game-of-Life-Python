import os
import random

from config import (
    VERBOSE,
    TEST_DIR,
    FIELD_NUMBER,
    FIELD_SIZE,
    DENSITY_VALUE
)


def get_field() -> str:
    filename = f"{TEST_DIR}/{FIELD_NUMBER}.txt"
    if FIELD_NUMBER is not None and os.path.exists(filename):
        return filename
    
    return create_field()


def create_field() -> str:
    os.makedirs(TEST_DIR, exist_ok=True)

    if DENSITY_VALUE is None:
        den_value = 0.15
    else:
        den_value = DENSITY_VALUE

    density = max(0.0, min(1.0, den_value))
    mode_name = f"{density:.3f}"
    
    existing_files = []
    if os.path.exists(TEST_DIR):
        existing_files = [f for f in os.listdir(TEST_DIR)
                          if f.endswith(".txt") and f[:-4].isdigit()]
        
    if len(existing_files) < 10:
        file_numbers = [int(f[:-4]) for f in existing_files] if existing_files else [0]
        next_number = max(file_numbers) + 1
    else:
        oldest_file = min(existing_files, key=lambda f: os.path.getctime(f"{TEST_DIR}/{f}"))
        next_number = int(oldest_file[:-4])
    
    filename = f"{TEST_DIR}/{next_number}.txt"
    with open(filename, "w") as f:
        for _ in range(FIELD_SIZE):
            row = ''.join("1" if random.random() < density else "0"
                          for _ in range(FIELD_SIZE))
            f.write(row + '\n')

    with open(filename, 'r') as f:
        content = f.read()
        ones = content.count('1')
        zeros = content.count('0')
        total_cells = ones + zeros
        actual_density = ones / total_cells if total_cells > 0 else 0
    
    if VERBOSE:
        print(f"created file: {filename}")
        print(f"  density: {actual_density*100:.2f}%")
        print(f"  cells: {FIELD_SIZE**2}")
    
    return filename


if __name__ == "__main__":
    create_field()