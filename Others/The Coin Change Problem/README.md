# Question

You are working at the cash counter at a fun-fair, and you have different types of coins available to you in infinite quantities. The value of each coin is already given. Can you determine the number of ways of making change for a particular number of units using the given types of coins ?

For example, if you have 4 types of coins, and the value of each type is given as 8,3,1,2 respectively, you can make change for 3 units in three ways: {1,1,1}, {1,2} and {3}.

### Input Format

The first line contains two space-separated integers describing the respective values of n and m, where:
 n is the number of units
 m is the number of coin types
The second line contains m space-separated integers describing the respective values of each coin type.

### Output Format

Print a long integer denoting the number of ways we can get a sum of n from the given infinite supply of m types of coins.

#### Sample Input 0

4 3  
1 2 3

#### Sample Output 0

4

#### Explanation

There are four ways to make change for  using coins with values given by :  
Thus, we print  as our answer.  

#### Sample Input 1

10 4  
2 5 3 6

#### Sample Output 1

5

#### Explanation 1

There are five ways to make change for  units using coins with values given by :  
Thus, we print  as our answer.

