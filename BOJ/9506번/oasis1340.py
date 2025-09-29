nums = list()

while True :
  n = int(input())

  if n == -1 :
    break
  else:
    nums.append(n)

for i in range(len(nums)):
  result = list()

  for j in range(nums[i]):
    if nums[i] % (j+1) == 0:
      result.append(j+1)
  
  g = sum(result) - nums[i]

  if nums[i] == g:
    print(nums[i], end="")
    print(' = ' , end="")
    print(result[0], end="")
    for k in range(len(result)-2):
      print(' + ' ,end="")
      print(result[k+1], end="")
    print()
  else:
    print(nums[i], end=" ")
    print('is NOT perfect.')

  for i in range(len(result)):
    result.pop()
