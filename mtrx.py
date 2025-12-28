import string

alp = string.ascii_uppercase
letters = list(alp)
cols = 6 
matrix = []

for i, ch in enumerate(letters):
    row = i // cols
    if (col := i % cols) == 0:
        matrix.append([])
    matrix[row].append(ch)
print(matrix)
