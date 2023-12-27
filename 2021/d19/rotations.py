import numpy as np
import itertools

def rotations(array):
    for x, y, z in itertools.permutations([0, 1, 2]):
        for sx, sy, sz in itertools.product([-1, 1], repeat=3):
            rotation_matrix = np.zeros((3, 3))
            rotation_matrix[0, x] = sx
            rotation_matrix[1, y] = sy
            rotation_matrix[2, z] = sz
            if np.linalg.det(rotation_matrix) == 1:
                yield np.matmul(rotation_matrix, array)

def test():
    all_rotations = list(rotations(np.array([1,1,1])))
    #print(all_rotations)
    for i in range(len(all_rotations)):
        print(i, all_rotations[i])

if __name__ == "__main__":
    test()
