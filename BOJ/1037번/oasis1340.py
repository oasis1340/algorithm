count = int(input())
nums = list(map(int, input().split()))

nums.sort()

a = len(nums) // 2

if len(nums) % 2 == 0:
  print(nums[a-1] * nums[a])

if len(nums) % 2 == 1:
  print(nums[a]**2)
