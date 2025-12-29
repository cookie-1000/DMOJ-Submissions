n=int(input())
curr=-1
max_name=""
for _ in range(n):
    name = input()
    bid=int(input())
    if bid>curr:
        curr=bid
        max_name=name
print(max_name)
#dictionary approach doesn't work D:<