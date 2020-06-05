# Question

Noddy's vehicle has 2 issues:  
It needs exactly F amounts of fuel to fly this distance - not more and not less.  
At a particular time, it cannot increase the fuel by more than K  
There are N fuel stations on the way: each having A1 A2..... AN amount of fuel.

You have to tell us whether it is possible to fill the tank up to exactly F amounts.

### Input

The first line contains T, the number of test cases. Each test case contains:  
N, followed by N numbers denoting the amount of fuel at the ith station  
F - the target fuel that you must reach  
K - your limit for max fuel at one station

### Output

Print Yes if you can fill with the given stations and capacities. Otherwise, print No  

#### Sample Input

3  
6 6 10 3 2 2 1  
7  
5  
5 6 10 3 2 2  
7  
1  
6 8 10 3 9 7 4  
2  
10

#### Sample Output

Yes  
No  
No

#### Explanation

In the first case, 7 can be reached by taking 3, 2, and 2  
In the second case, since we can never pick up more than 1, we can't reach 7  
There is no way of reaching 2
