def close(list, num):
	a = min([i for i in list if num < i])
	b = max([i for i in list if num > i])
	return a, b

print(close([3, 8, 5, 9, 10], 6))