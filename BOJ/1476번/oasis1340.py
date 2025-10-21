nums = list(map(int, input().split()))
result = [0, 0, 0]
count = 0
e = nums[0]
s = nums[1]
m = nums[2]

for i in range (10**10):
  result[0] += 1
  result[1] += 1
  result[2] += 1

  count += 1

  if result[0] > 15:
    result[0] = 1
  
  if result[1] > 28:
    result[1] = 1

  if result[2] > 19:
    result[2] = 1

  if result[0] == e and result[1] == s and result[2] == m:
    break
  
print(count)
