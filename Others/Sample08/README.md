# Question

To get onto the ship, you get in line to buy a ticket. The line is very long, so you buy the special pass. The special pass allows you to move ahead in the line.

Using this special pass, if you are at the ith position in the line, you can move forward by x steps where 1 <= x <= A[i]. Then, when you get to a new position, you can again move by the same logic.

For example, let's say line is like this: 4 1 2 2 3 3 1 2 4 4:

At the first position, you can move forward by 1, 2, 3 or 4 stepssince A[0] is 4  
At the 2nd position, you can move forward by 1 step only (since A[1] is 1)  
At the 3rd position you man move forward by 1 or 2 steps (since A[2] is 2)  
And so on...  
In order to reach the end of the line, the minimum number of steps you require are 3. A[0] -> A[4]; A[4] -> A[7]; A[7] -> A[9]

Given the various line positions, find the minimum number of steps to reach the end line.

### Input

The first line contains T, the number of inputs  
The following lines contain N followed by space-separated numbers A1, A2, A3.... AN

Constraints  
1 <= A[i] <= 1000  
1 <= N <= 1000

### Output

Print minimum number of steps for each test case

#### Sample Input

3  
3 7 8 7  
2 2 1  
10 4 1 2 2 3 3 1 2 4 4

#### Sample Output

1  
1  
3

#### Explanation

We can reach A[2] directly from A[0], because we are allowed 1,2,.... 7 steps and we just need 2 steps  
We can reach A[1] in just 1 step  
Explained in the example above
