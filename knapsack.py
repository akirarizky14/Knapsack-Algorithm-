# How to solve it ? There's three way
# 1. Greedy Approximation
# 2. Dynamic Programming
# 3. Dominance Relation
# class KnapsackPackage(object):
#     """ Knapsack Package Data Class """
#     def __init__(self, weight, value):
#         self.weight = weight
#         self.value = value
#         self.cost = value / weight
#
#     def __lt__(self, other):
#         return self.cost < other.cost
#
# class FractionalKnapsack(object):
#     def __init__(self):
#         pass
#
#     def knapsackGreProc(self, W, V, M, n):
#         packs = []
#         for i in range(n):
#             packs.append(KnapsackPackage(W[i], V[i]))
#         packs.sort(reverse = True)
#         remain = M
#         result = 0
#         i = 0
#         stopProc = False
#         while (stopProc != True):
#             if (packs[i].weight <= remain):
#                 remain -= packs[i].weight;
#                 result += packs[i].value;
#             print("Pack ", i, " - Weight ", packs[i].weight, " - Value ", packs[i].value)
#             if (packs[i].weight > remain):
#                 i += 1
#             if (i == n):
#                 stopProc = True
#         print("Max Value:\t", result)
#
# if __name__ == "__main__":
#     W = [15, 10, 2, 4]
#     V = [30, 25, 2, 6]
#     M = 37
#     n = len(W)
#     proc = FractionalKnapsack()
#     proc.knapsackGreProc(W, V, M, n)


# Second way
# def knapsack(W, wt, val, n):
#     K = [[0 for x in range(W + 1)] for x in range(n + 1)]
#
#     for i in range(n + 1):
#         for w in range(W + 1):
#             if i == 0 or w == 0:
#                 K[i][w] = 0
#             elif wt[i-1] <= w:
#                 K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
#             else:
#                 K[i][w] = K[i-1][w]
#
#     return K[n][W]
#
# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)
#
# print(knapsack(W, wt, val, n))


import numpy as np

class KnapsackProblem:
    def __init__(self):

        # initialize instance variables:
        self.items = []
        self.maxCapacity = 0

        # initialize the data:
        self.__initData()

    def __len__(self):
        """
        :return: the total number of items defined in the problem
        """
        return len(self.items)

    def __initData(self):
        self.items = [
            ("map", 9, 150),
            ("compass", 13, 35),
            ("water", 153, 200),
            ("sandwich", 50, 160),
            ("glucose", 15, 60),
            ("tin", 68, 45),
            ("banana", 27, 60),
            ("apple", 39, 40),
            ("cheese", 23, 30),
            ("beer", 52, 10),
            ("suntan cream", 11, 70),
            ("camera", 32, 30),
            ("t-shirt", 24, 15),
            ("trousers", 48, 10),
            ("umbrella", 73, 40),
            ("waterproof trousers", 42, 70),
            ("waterproof overclothes", 43, 75),
            ("note-case", 22, 80),
            ("sunglasses", 7, 20),
            ("towel", 18, 12),
            ("socks", 4, 50),
            ("book", 30, 10)
        ]

        self.maxCapacity = 400

    def getValue(self, zeroOneList):
        totalWeight = totalValue = 0

        for i in range(len(zeroOneList)):
            item, weight, value = self.items[i]
            if totalWeight + weight <= self.maxCapacity:
                totalWeight += zeroOneList[i] * weight
                totalValue += zeroOneList[i] * value
        return totalValue

    def printItems(self, zeroOneList):
        totalWeight = totalValue = 0

        for i in range(len(zeroOneList)):
            item, weight, value = self.items[i]
            if totalWeight + weight <= self.maxCapacity:
                if zeroOneList[i] > 0:
                    totalWeight += weight
                    totalValue += value
                    print("- Adding {}: weight = {}, value = {}, accumulated weight = {}, accumulated value = {}".format(item, weight, value, totalWeight, totalValue))
        print("- Total weight = {}, Total value = {}".format(totalWeight, totalValue))


# testing the class:
def main():
    # create a problem instance:
    knapsack = KnapsackProblem()
    # create a random solution and evaluate it:
    randomSolution = np.random.randint(2, size=len(knapsack))
    print("Random Solution = ")
    print(randomSolution)
    knapsack.printItems(randomSolution)


if __name__ == "__main__":
    main()