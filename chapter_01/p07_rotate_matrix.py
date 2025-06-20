# O(NxN)
import unittest
from copy import deepcopy


def rotate_matrix(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

            # top -> right
            matrix[i][-layer - 1] = top
    return matrix


def rotate_matrix_double_swap(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - 1 - j]
            matrix[i][n - 1 - j] = temp
    return matrix


def rotate_matrix_pythonic(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)
    result = [[0] * n for i in range(n)]  # empty list of 0s
    for i, j in zip(range(n), range(n - 1, -1, -1)):  # i counts up, j counts down
        for k in range(n):
            result[k][i] = matrix[j][k]
    return result


def rotate_matrix_pythonic_alternate(matrix):
    """rotates a matrix 90 degrees clockwise"""
    return [list(reversed(row)) for row in zip(*matrix)]


def inner_rotate(matrix):
    tmp = None
    for layer in range(len(matrix) // 2):
        final = len(matrix) - 1 - layer
        for i in range(final - layer):
            coords = [
                (layer, i + layer),
                (i + layer, final),
                (final, final - i),
                (final - i, layer),
            ]
            start = coords[0]
            tmp = matrix[start[0]][start[1]]
            j = -1
            while j > -4:
                this_coords = coords[j]
                next_coords = coords[j + 1]
                matrix[next_coords[0]][next_coords[1]] = matrix[this_coords[0]][
                    this_coords[1]
                ]
                j -= 1
            first = coords[1]
            matrix[first[0]][first[1]] = tmp
    return matrix


class Test(unittest.TestCase):

    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
    testable_functions = [
        rotate_matrix_pythonic,
        rotate_matrix,
        rotate_matrix_pythonic_alternate,
        rotate_matrix_double_swap,
        inner_rotate,
    ]

    def test_rotate_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()
