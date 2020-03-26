matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]

print([[i[n] for i in matrix] for n in range(4)])

print(list(zip(*matrix)))
