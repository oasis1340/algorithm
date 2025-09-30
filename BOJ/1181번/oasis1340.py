count = int(input())
sentences = list()

for i in range(count):
  s = input()
  sentences.append(s)

sentences = list(set(sentences))
sentences.sort()
sentences.sort(key=len)

for i in range(len(sentences)):
  print(sentences[i])
