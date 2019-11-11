new_map = [[1, 2, 3], [2, 3, 4]]

print(new_map)
y_map = [*zip(*new_map)]
x_map = list(map(list, zip(*new_map)))
print(y_map)
print(x_map)