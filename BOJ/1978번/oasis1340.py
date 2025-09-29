count = int(input())
nums = list(map(int, input().split()))
result = list()
total = 0

for i in range(len(nums)):
  if nums[i] == 1:
    continue

  for j in range(nums[i]):
    if nums[i] % (j+1) == 0:
      result.append(j+1)

  if len(result) == 2:
    total += 1
  
  for k in range(len(result)):
    result.pop()
  
print(total)
