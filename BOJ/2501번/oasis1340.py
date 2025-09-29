num, count = map(int, input().split())

result = list()

for i in range(num):
  if num % (i+1) == 0:
    result.append(i+1)

try:
    print(result[count-1])
except IndexError:
    print(0)
