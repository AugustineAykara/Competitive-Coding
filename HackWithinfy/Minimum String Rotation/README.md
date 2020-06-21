A rotation on a string is defined as removing first element and concatenating it at the end.

Given N, and an array of N strings, print the minimum no. of cumulative rotations on the string so as to make all the strings equal.

If this is not possible return -1

#### Input Format

First line contain N, number of strings  
This is followed by N strings

###### Constraints

2 <= N <= 10^4  
3 <= string.length <= 100  
All characters in uppercase

#### Sample Input

4  
CDAAB  
AABCD  
DAABC  
AABCD

#### Sample Output

3

#### Explanation

CDAAB rotating 2 time gives AABCD  
AABCD rotating 0 time gives AABCD  
DAABC rotating 1 time gives AABCD  
AABCD rotating 0 time gives AABCD  
Hence all strings can be made AABCD using min string rotation of 3 
