You have been given longitude and latitude of locations from where the channels are going to be broadcasted. You also get the height of tower from which these channels are broadcasted. Moreover, you have been given the location of your friend Jason. You have to calculate how many connections he can make to the towers. Take Radius of earth= 6371 KM.

All the computation has to be accurate up to 6 digits after the decimal point.

Constraints
1 <= N < 10^5

Input
First line contains integer N denoting the number of locations from where the channel is going to be broadcasted
Second line contains N space-separated decimal values denoting latitudes
Third line contains N space-separated decimal values denoting longitudes
Fourth line contains N space-separated integer values denoting the height of tower from which channels are broadcasted
Fifth Line contains two space-separated decimal values denoting latitude, longitude of Jason's location

Output
Print the number of channels Jason can connect with

Time Limit
1

Examples
Example 1

Input
2
19.076090 17.387140
72.877426 78.491684
2 1
18.516726 73.856255

Output
1

Explanation

First latitude and longitude is Mumbai and second is for Hyderabad from where the channel signals are broadcasted. Jason is in Pune. According to signal strength Jason will only be able to connect Mumbai tower.

Example 2

Input
2
28.644800 22.572645
77.216721 88.363892
5 7
48.864716 2.349014

Output
0

Explanation

First latitude and longitude is Delhi and second is for Kolkata from where the channel signals are broadcasted. Jason is in Paris. According to signal strength Jason will not be able to connect any tower.