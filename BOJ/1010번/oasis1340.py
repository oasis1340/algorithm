import math

count = int(input())
n = []
r = []
results = []

for i in range (count):
  nums = list(map(int, input().split()))
  n.append(nums[0])
  r.append(nums[1])

for i in range (count):
  if (n[i] > r[i]):
    nF = math.factorial(n[i])
    rF = math.factorial(r[i])
    dF = math.factorial(n[i] - r[i])
    result = nF/(rF*dF)
    results.append()
  else:
    nF = math.factorial(n[i])
    rF = math.factorial(r[i])
    dF = math.factorial(r[i] - n[i])
    result = rF/(nF*dF)
    results.append(int(result))

for i in range(len(results)):
  print(results[i])
