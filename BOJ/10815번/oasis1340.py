count1 = int(input())
cards = set(map(int, input().split()))

count2 = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")
