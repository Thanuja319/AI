import math
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if curDepth == targetDepth: 
        return scores[nodeIndex]
    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))
def get_user_input():
    num_leaves = int(input("Enter the number of leaf nodes (must be a power of 2): "))
    if math.log(num_leaves, 2) % 1 != 0:
        print("Error: The number of leaf nodes must be a power of 2.")
        return None
    scores = []
    print(f"Enter {num_leaves} scores for the leaf nodes:")
    for i in range(num_leaves):
        score = int(input(f"Leaf node {i + 1} score: "))
        scores.append(score)
    return scores
if __name__ == "__main__":
    scores = get_user_input()
    if scores:
        treeDepth = int(math.log(len(scores), 2))  
        print("The optimal value is:", end=" ")
        print(minimax(0, 0, True, scores, treeDepth))
