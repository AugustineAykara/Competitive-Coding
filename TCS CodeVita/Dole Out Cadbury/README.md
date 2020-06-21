You are a teacher in reputed school. During Celebration Day you were assigned a task to distribute Cadbury such that maximum children get the chocolate. You have a box full of Cadbury with different width and height. You can only distribute la then you need to break Cadbury in 5X5 square and distribute to first child and then remaining 5X5 to next in queue

##### Constraints 

O < P < Q < 1501  
0 < R < S < 1501

#### Input Format 

First line contains an integer P that denotes minimum length of Cadbury in the box  
Second line contains an integer Q that denotes maximum length of Cadbury in the box  
Third line contains an integer R that denotes minimum width of Cadbury in the box  
Fourth line contains an integer S that denotes maximum width of Cadbury in the box

#### Output Format

Print total number of children who will get chocolate 

#### Sample Input

5  
7  
3  
4

#### Sample Output

24

#### Explanation

Types of Cadbury in the box Length is in between 5 to 7 and width is in between 3 to 4. So we have 5x3,5x4,6x3,6X4,7x3,7X4 type of Cadbury in the box.  
First, we can give 3X3 square Cadbury to 1st child Then we are left with 3X2. Now largest square is 2x2 which will be given to next child. Next, we are left with two 1X1 part of Cadbury which will be given to another two children. And so on
