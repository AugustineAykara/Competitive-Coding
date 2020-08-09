Imagine you are a martial arts fighter fighting with fellow martial artists to win prize money. However unlike traditional competitions, here you have the opportunity to pick and choose your opponent to maximize your prize kitty. The rules of maximization of prize kitty are as follows

► You have a superpower bestowed upon you, that you will win against anyone you challenge

► You have to choose the right order because unfortunately the superpower does not ensure that your prize money is always the highest

► Every victory against an opponent that you challenge and win against, will translate into a certain winning sum

► Here begins the technical part that you need to know in order to maximize your winning prize money

All your opponents are standing in one line next to each other i.e. the order of opponents is fixed

Your first task is to choose a suitable opponent from this line

When you choose one opponent from that line, he steps out of the line and fights you.

After you beat him, you get to decide how your prize money for winning against him will be calculated

Essentially, if the opponent you have beaten has two neighbours, then you have the option to multiply the opponent number with any one of the two neighbours and add the other opponent number. That value becomes your prize money for that match

If your opponent has only one neighbor then your prize money for that match is product of current opponent number with neighbours' opponent number

When dealing with last opponent in the tournament, your prize money is equal to the value of the last opponent number

As the tournament proceeds, the opponent that you have beaten has to leave the tournament

Example: 2 5 6 7

This depicts that you have four opponents with numbers 2 5 6 and 7 respectively



Example 2

Input

3
7 8 9

Output

151

Explanation:

1. You choose to fight opponent number 8, then after winning, the max prize kitty you can win for that match is = 8*9+7 = 79
Now opponent number 8 is out of the game. So opponent number 7 9 remain

2. Suppose you now choose to fight opponent number 7, then after winning, the max prize kitty you can win for that match is = 7*9+0 = 63. Your overall prize kitty is now 79 + 63 = 142
Now opponent number 7 is out of the game. So opponent number 9 remains

3. After beating opponent number 9, the max prize kitty you can win for that match is 9
So overall prize kitty in this case is 142 + 9 = 151.