list_of_ranks = list(map(int, input().split()))

gift_prev = 0
gift = 1
count = 0
i_prev = 0
for i in list_of_ranks:
    if(i_prev == 0):
        count+=gift
    elif(i_prev<i):
        gift+=1
        count+=gift
    elif(i_prev>i):
        gift-=1
        count+=gift
    elif(i_prev==i):
        count+=gift
    i_prev = i
print(count)