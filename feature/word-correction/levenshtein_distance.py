def levenshtein_distance(token1, token2):
    # Create a matrix to store distances
    distances = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]

    # Initialize the first column of each row
    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    # Initialize the first row of each column
    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    # Initialize variables to hold cost of deletions, insertions, and substitutions
    a = 0
    b = 0
    c = 0

    # Fill the distances matrix
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:  # Characters match, no cost
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:  # Characters do not match, calculate minimum cost
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                # Choose the minimum cost and add 1 to account for the operation
                if a <= b and a <= c:
                    distances[t1][t2] = a + 1
                elif b <= a and b <= c:
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    # The distance between the two tokens is in the bottom-right cell
    return distances[len(token1)][len(token2)]
