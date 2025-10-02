n = int(input())
result = 0

if n < 100:
  result = n

else:
  result = 99

for i in range(100, n+1):
  a = i // 100
  b = (i // 10) % 10
  c = (i % 100) % 10

  if a - b == b - c:
    result += 1

print(result)
