# Dynamic Programming:
Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. It's a technique to avoid computing the same results multiple times by storing the results of these subproblems. Dynamic Programming is particularly useful when a problem has overlapping subproblems and optimal substructure, meaning the problem can be broken down into smaller, reusable problems, and the optimal solution to the problem can be constructed from the optimal solutions of its subproblems.

## When to Use:
Dynamic Programming is used when the problem can be divided into stages, with a decision required at each stage that will lead to the next one. It's most effective when:

* The problem has overlapping subproblems that can be cached to avoid redundant calculations.
* The problem exhibits an optimal substructure, allowing solutions to be constructed efficiently from previously solved subproblems.

## Example Challenges:
1. 0/1 Knapsack Problem: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
2. Longest Common Subsequence: Find the longest subsequence present in two sequences.
3. Coin Change Problem: Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change?
4. Fibonacci Series: Computing the nth Fibonacci number efficiently.

## Real-Life Applications:
* Resource Allocation & Scheduling: E.g., allocating network bandwidth or scheduling tasks on machines.
* Text and Data Compression: Algorithms like LZ77 use DP for finding repeated occurrences of data.
* Game Theory and Strategic Planning: E.g., chess engines that evaluate future moves.
