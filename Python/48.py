# Read the number of test cases
T = int(input())

# Loop through each test case
for t in range(T):
    # Read the size of the matrix
    N, M = map(int, input().split())

    # Read the matrix elements
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    # Find the shortest path from A[1][1] to A[N][M]
    path = []
    min_steps = float('inf')
    for i in range(N):
        for j in range(M):
            # Calculate the distance between A[i][j] and A[i+1][j]
            d1 = abs(A[i+1][j] - A[i][j])
            # Calculate the distance between A[i][j] and A[i][j+1]
            d2 = abs(A[i][j+1] - A[i][j])
            # Calculate the distance between A[i][j] and A[i+1][j+1]
            d3 = abs(A[i+1][j+1] - A[i][j])
            # Choose the shortest distance
            min_distance = min(d1, d2, d3)
            # Add the distance to the total cost
            cost = min_distance + (i == 0 or j == 0 or i == N - 1 or j == M - 1) * 1000
            # Check if the path is feasible
            if cost < min_steps:
                min_steps = cost
                path = [i, j]
    # Print the result
    print(min_steps, path[0], path[1])