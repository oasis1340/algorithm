count, money = map(int, input().split())
tokens = list()

result = 0

for i in range (count):
  token = int(input())
  tokens.append(token)

for token in reversed(tokens):
    if money >= token:
        result += money // token
        money %= token

print(result)
