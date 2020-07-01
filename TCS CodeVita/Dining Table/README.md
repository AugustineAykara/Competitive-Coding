In a conference, attendees are invited for a dinner after the conference. The Coordinator, Sagar arranged round tables for dinner and want to have an impactful seating experience for the attendees. Before finalizing the seating arrangement, he want to analyze all possible arrangements. There are R round tables and N attendees. In case where N is an exact multiple of R, the number of attendees must be exactly N/R. If N is not an exact multiple of R, then the distribution of attendees must be as equal as possible. Please refer Example section for better understanding.

For example, R =2 and N=3  
All possible seating arrangements are  
(1,2) & (3)  
(1,3) & (2)  
(2,3) & (1)

Attendees are numbered from 1 to N.

##### Constraints

0 < R <= 10 (Integer)  
0 < N <= 20 (Integer)

#### Input Format

One line containing two space delimited integers R and N, where R denotes the number of round tables and N denotes the number of attendees

#### Output Format

Single integer S denoting number of possible unique arrangements

#### Sample Input

2 5

#### Sample Output

10

##### Explanation

R=2, N=5

(1,2,3) & (4,5)  
(1,2,4) & (3,5)  
(1,2,5) & (3,4)  
(1,3,4) & (2,5)  
(1,3,5) & (2,4)  
(1,4,5) & (2,3)  
(2,3,4) & (1,5)  
(2,3,5) & (1,4)  
(2,4,5) & (1,3)  
(3,4,5) & (1,2)

For arrangements like  
(1,2,3) & (4,5)  
(2,1,3) & (4,5)  
(2,3,1) & (4,5) etc.  
As it is a round table, all the above arrangements are same
