import  string 

letters = string.ascii_uppercase
cols = 6 
matrix = []
for index,ch in enumerate(letters):
    if index % cols == 0 :
        matrix.append([])
    matrix[index // cols].append(ch)
print(matrix)