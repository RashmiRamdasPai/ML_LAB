def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, maxDepth):

    if depth == maxDepth:
        return values[nodeIndex]

    if maximizingPlayer:
        best = float('-inf')

        for i in range(2):
            val = alphabeta(depth + 1,
                            nodeIndex * 2 + i,
                            False,
                            values,
                            alpha,
                            beta,
                            maxDepth)

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alphabeta(depth + 1,
                            nodeIndex * 2 + i,
                            True,
                            values,
                            alpha,
                            beta,
                            maxDepth)

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [3, 5, 2, 9, 12, 5, 23, 23]

result = alphabeta(
    0,                  # depth
    0,                  # root node
    True,               # maximizing player
    values,
    float('-inf'),      # alpha
    float('inf'),       # beta
    3                   # maxDepth
)

print("Optimal Value:", result)
