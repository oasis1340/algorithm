nums = []
index = []

for i in range(8):
  num = int(input())
  nums.append(num)

reverse = sorted(nums)

for i in range(5):
  for j in range(8):
    if reverse[i+3] == nums[j]:
      index.append(j+1)

index.sort()

print(sum(reverse) - reverse[0] - reverse[1] - reverse[2])

for i in range(len(index)):
  print(index[i], end=" ")
