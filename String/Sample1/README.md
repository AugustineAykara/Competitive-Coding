# Question

Nobita has a specific medicine to solve this problem. He tried to say the name of the medicine, but his sentences are jumbled beyond imagination.  
Here is how you can help him:

His sentence is in the form of a very long word. mymedicinesarerighthere  
You need to break this word down in the following way: m, ym ,edi ,cine ,sarer ,ighthe, re  
Then take the first and last characters of the sub-words as long as the sub-word is longer than the previous sub-word: m, ym, ei, ce, sr, ie.  
Notice we don't touch re because it is shorter than the previous sub-word  
The words on joining gives the name of Nobita's medicines: mymeicesrie  

### Input

The first line contains T, the number of test cases  
This is followed by T strings (with length >=1)  

### Output

Print the name of Nobita's medicines

#### Sample Input

3  
mymedicinesarerighthere  
isnobitaalive  
testcasesoftenmakemuchmoresensethanthisone

#### Sample Output

mymeicesrie  
isnoitl  
testasofmachent
