import string

alp = string.ascii_uppercase
letters = alp
cols = 6 

# row mappings..............
def create_row(letters,cols):
    matrix = []
    for i,ch in enumerate(letters):
        if i % cols == 0:
            matrix.append([])
        matrix[i // cols].append(ch)
    return matrix

n_row = create_row(letters,cols)
#print(n_row)

# Maximum column.......
max_cols = max(len(row) for row in n_row)

# Column-wise traversal (mapping)
def column_row(n_row,max_cols):
    columns = []
    for col_index in range(max_cols):
        col = []
        for row in n_row:
            if len(row) > col_index:
                col.append(row[col_index])
        columns.append(col)
    return columns
n_col = column_row(n_row,max_cols)
#print(n_col)
def show(ro):
    in_no = []
    i = 0
    while i <= 4:
        print(ro[i])
        user_input = input("if your letter exist here's so type  y/n:  ")
        if user_input.lower() == "y":
            in_no.append(i)
        elif user_input.lower() == "n":
            print()
        i += 1
        continue
    return in_no       
sho = show(n_row)
print(f"this is store value {sho}")
print(len(n_row))
"""
def main_logic(r,c):
    user_inpit = input("if your word exist here so type : y/n :   ")
"""