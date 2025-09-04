import numpy as np

def input_matrix(name):
    try:
        rows = int(input(f"Enter number of rows for {name}: "))
        cols = int(input(f"Enter number of columns for {name}: "))
    except (EOFError, OSError, ValueError):
        print("Invalid input. Defaulting to 2x2 matrix.")
        rows, cols = 2, 2

    print(f"\nEnter elements for {name} (row by row, space separated):")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = input(f"Row {i+1}: ").split()
                if len(row) != cols:
                    print(f"Please enter exactly {cols} elements.")
                    continue
                matrix.append(list(map(float, row)))
                break
            except (EOFError, OSError):
                print("Input stream closed unexpectedly.")
                return np.array(matrix)
            except ValueError:
                print("Invalid input. Please enter numeric values only.")
    return np.array(matrix)

def display_matrix(matrix, title="Result"):
    print(f"\n{title}:")
    print(matrix)

def matrix_operations():
    while True:
        try:
            print("""
======= Matrix Operations Tool =======
1. Matrix Addition
2. Matrix Subtraction
3. Matrix Multiplication
4. Transpose of a Matrix
5. Determinant of a Matrix
6. Exit
====================================
""")
            choice = input("Enter your choice (1-6): ")
        except (EOFError, OSError):
            print("\nNo input detected. Exiting.")
            break

        if choice == '1':
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                display_matrix(A + B, "A + B")
            else:
                print("Error: Matrices must have the same dimensions for addition.")

        elif choice == '2':
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                display_matrix(A - B, "A - B")
            else:
                print("Error: Matrices must have the same dimensions for subtraction.")

        elif choice == '3':
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape[1] == B.shape[0]:
                display_matrix(np.dot(A, B), "A × B")
            else:
                print("Error: Columns of A must equal rows of B for multiplication.")

        elif choice == '4':
            A = input_matrix("Matrix A")
            display_matrix(np.transpose(A), "Transpose of A")

        elif choice == '5':
            A = input_matrix("Matrix A")
            if A.shape[0] == A.shape[1]:
                display_matrix(np.linalg.det(A), "Determinant of A")
            else:
                print("Error: Determinant can only be calculated for square matrices.")

        elif choice == '6':
            print("Exiting Matrix Operations Tool. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    matrix_operations()
