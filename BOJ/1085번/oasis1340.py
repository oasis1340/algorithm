x, y, w, h = map(int, input().split());

road = list()

road.append(x)
road.append(y)
road.append(w-x)
road.append(h-y)

result = min(road)

print(result)
