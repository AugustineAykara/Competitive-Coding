You are given a set of numbers. Using the binary representation of all the numbers from L to R and have to count the special ones on the list.

A bit is called to be set if it has value 1  
The special one is a set bit in the binary representation of any number X where L<=X < =R and this bit is at prime index in the binary representation of X.  
The positioning of the bits is done from right to left and starts from 1.

For example, the binary representation of 4 is 100. In this, 1st and 2nd bits are not set while 3rd bit is set. Also, this 3rd bit is a special one because 3 is a prime number.

#### Input Format:

First line of input contains a single integer T denoting the number of test cases  
T lines follow each containing two space-separated integer L and R

#### Output format:

For each test case, print a single integer denoting the number of special 1's on the list.

#### Constraints:

1 <= L <= R <= 106  
1 < T < 103

#### Sample Input

3  
1 31  
100 1000  
2 4

#### Sample Output

48
1803
3
