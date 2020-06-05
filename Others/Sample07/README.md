# Question

Dora has a pack of N batteries.

Given a battery of certain rating Ai, the battery's power is the number of set bits in Ai  
When two batteries Ai and Aj combine, their combined power becomes  Ai || Aj, where || is the bitwise OR operator  
Dora had carefully packed the batteries such that the power of the entire set of batteries is just enough to help us cross the tunnel. However, now we need to remove some batteries, without hurting the overall power of the set of batteries, because we don't have enough space in the backpack.

Given a set of N battery ratings, choose the minimum number of batteries min such that the power of the min batteries is the same as power of N batteries.


### Input

The first line contains T, the number of test cases. Each of the following T lines contain:  
N followed by N numbers A1, A2, A3...... An

##### Constraints:  
1 <= N <= 105  
1 <= Ai <= 106

### Output

Print min batteries required for each test case

#### Sample Input

3  
4 3 5 7 13  
4 2 4 8 16  
4 5 3 1 7

#### Sample Output

2  
4  
1

#### Explanation

Case 1: we have powers: 3: 011, 5: 101, 7: 111, 13: 1101. Combining 13 and 7 will give us 15 : 1111, which is the same as the bitwise OR of entire batteries. Thus answer is 2 - only 2 batteries needed  
Case 2: we need all 4 numbers to reach combined powers of  11110  
Case 3: we only need 7 ( 111) to reach the same combined power as the entire batteries
