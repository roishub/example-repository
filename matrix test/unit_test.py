import unittest

def transpose(matrix):
    """
    Transposes the given matrix.
    """
    if not matrix:  # Check if the matrix is empty
        return []

    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

class MatrixTest(unittest.TestCase):
    def test_transpose(self):
        # Test case 1
        matrix1 = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
        expected1 = [[1, 4, 7],
                     [2, 5, 8],
                     [3, 6, 9]]
        self.assertEqual(transpose(matrix1), expected1)

        # Test case 2
        matrix2 = [[1, 2],
                   [3, 4],
                   [5, 6]]
        expected2 = [[1, 3, 5],
                     [2, 4, 6]]
        self.assertEqual(transpose(matrix2), expected2)

        # Test case 3 (empty matrix)
        matrix3 = []
        expected3 = []
        self.assertEqual(transpose(matrix3), expected3)

        # Test case 4 (singleton matrix)
        matrix4 = [[7]]
        expected4 = [[7]]
        self.assertEqual(transpose(matrix4), expected4)

if __name__ == '__main__':
    unittest.main()
