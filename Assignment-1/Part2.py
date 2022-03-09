class Node:
    def __init__(self, val1, val2):
        self.sum = val1 + val2
        self.child = (val1, val2)
        self.rev_child = (val2, val1)


def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    tup_list = []
    for val1 in inputArray:
        for val2 in inputArray:
            node = Node(val1, val2)
            if (node.sum == targetSum) and (node.rev_child not in tup_list):
                tup_list.append(node.child)

    return tup_list


if __name__ == "__main__":
    print("\n",
          pairsThatEqualSum([1, 2, 3, 4, 5], 5), "\n",
          pairsThatEqualSum([1, 2, 3, 4, 5], 1), "\n",
          pairsThatEqualSum([1, 2, 3, 4, 5], 7)

          )
