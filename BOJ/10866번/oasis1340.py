from collections import deque

count = int(input())

nums = deque()
result = deque()

for i in range (count):
  text = list(input().split())
  if text[0] == 'push_front':
    nums.appendleft(text[1])
  if text[0] == 'push_back':
    nums.append(text[1])
  if text[0] == 'size':
      result.append(len(nums))
  if text[0] == 'empty':
    if len(nums) == 0:
      result.append('1')
    else:
      result.append('0')
  if text[0] == 'pop_front':
    if len(nums) == 0:
      result.append('-1')
    else:
      result.append(nums[0])
      nums.popleft()
  if text[0] == 'pop_back':
    if len(nums) == 0:
      result.append('-1')
    else:
      result.append(nums[-1])
      nums.pop()
  if text[0] == 'front':
    if len(nums) == 0:
      result.append('-1')
    else:
      result.append(nums[0])
  if text[0] == 'back':
    if len(nums) == 0:
      result.append('-1')
    else:
      result.append(nums[-1])

for i in range(len(result)):
  print(result[i])
