# Question

Mishki will be provided with an integer array A of size N and an integer K , where she needs to rotate the array in the right direction by K steps and then print the resultant array.

### Input:
The first line will consists of one integer T denoting the number of test cases.
For each test case:
1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
2) The next line consists of N space separated integers , denoting the elements of the array A.

### Output:
Print the required array.

#### Sample Input
1  
5 2  
1 2 3 4 5 
#### Sample Output
4 5 1 2 3

#### Explanation
N = 5 denoting the number of elements in the array and , denoting the number of steps of rotations.  
The initial array is : 1 2 3 4 5  
In first rotation, 5 will come in the first position and all other elements will move to one position ahead from their current position. Now, the resultant array will be : 5 1 2 3 4  
In second rotation, 4 will come in the first position and all other elements will move to one position ahead from their current position. Now, the resultant array will be : 4 5 1 2 3
