We define d(X, Y) as number of different corresponding bits in binary representation of X and Y. For example, d(3, 9) = 2, since binary representation of 3 and 9 are 0011 and 1001, respectively. The first and the third bit differ, so f(3, 9) = 2.

### Question

You are given an array of N positive integers, A1, A2 ,…, AN. Find sum of d(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 10^9+7.

### example

A = [3,7,9]

#### Output

12

#### Explanation

d(3,3) + d(3,7) + d(3,9) +  
d(7,3) + d(7,7) + d(7,9) +  
d(9,3) + d(9,7) + d(9,9)

0 + 1 + 2 +  
1 + 0 + 3 +  
2 + 3 + 0  
= 12  
Thus, we return 12

