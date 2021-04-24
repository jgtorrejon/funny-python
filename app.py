# Challente link: https://edabit.com/challenge/3DAkZHv2LZjgqWbvW

def is_adjacent(matrix, node1, node2):
    return bool(matrix[node1][node2])

matrix = [
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]

print(is_adjacent(matrix, 0, 1))