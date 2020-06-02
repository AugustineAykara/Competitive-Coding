A building have several floors. Each floor has an elevator. You are given integers X and Y. The elevators in the  building have a system with following rules :  

1. From any floor number A, you can only move to the floors numbered A/P, where P is a prime factor of A that is smaller than a given number M.  
2. The elevator takes exactly 1 second to move to another floor.  
3. Only one elevator can move at a time.

Write a program to find the minimum time required to move from the Xth to the Yth floor of the building.

#### Input Format

First line : T Number of test cases  
Next T lines : Three space-seperated integers X, Y and M

##### Constraints

1 <= T <= 100  
1 <= X, Y <= 10^9  
1 <= M <= 10^6

#### Output Format

For each test case, print two space-seperated integers in a single line i.e. the time taken to meet and the floor number at which you meet.  
In case, it is not possible to meet, print -1

#### Sample Input

3  
20 16 10  
100 120 10  
160 180 10

#### Sample Output

3 4  
3 20  
5 20

#### Explanation
##### Case 1

After 1 second : You move from 20 to 4(dividing by 5)  
After 2 second : Your friend moves from 16 to 8(dividing by 2)  
After 3 second : Your friend moves from 8 to 4 (dividing by 2)
