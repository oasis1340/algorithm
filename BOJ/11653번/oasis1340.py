num = int(input())
count = 2

while num > 1:
  
  if num % count == 0:
    print(count)
    num //= count
  else:
    count += 1
