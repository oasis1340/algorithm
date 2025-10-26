count = int(input())

wd = []
lt = []

for i in range (count):
  a, b = map(int, input().split())
  wd.append(a)
  lt.append(b)

max_wd = max(wd)
min_wd = min(wd)

max_lt = max(lt)
min_lt = min(lt)

result = (max_wd - min_wd) * (max_lt - min_lt)

if count < 2:
  print(0)
else:
  print(result)
