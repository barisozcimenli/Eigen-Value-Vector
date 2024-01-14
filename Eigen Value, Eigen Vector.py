import numpy as np

def question_1():
    a1 = np.array([[1, 2, 2], [1, 3, 5], [2, 4, 5]])
    a2 = np.array([[2, 4, 5], [1, 3, 2], [1, 2, 3]])
    a3 = np.array([[1, 2, 3], [1, 5, 3], [2, 5, 4]])
    a4 = np.array([[2, 5, 4], [1, 3, 2], [1, 5, 3]])

    matrices = [a1, a2, a3, a4]

    for i in range(4):
        evalue, evector = np.linalg.eig(matrices[i])
        print(f"Matrix {i + 1}:\n", matrices[i])
        print("\nEigenvalue:\n", evalue)
        print("\nEigenvector:\n", evector)
        print("-" * 30)
question_1()