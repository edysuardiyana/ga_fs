x = [[1,1],[1,1],[1,1]]
y = [[1,1],[1,0],[0,1],[1,1]]
z = [[1,1],[1,1],[1,1]]

len_x = len(x)
len_y = len(y)
len_z = len(z)

array =[len_x, len_y, len_z]

tel = {len_x:x, len_y : y, len_z : z}

max_val = max(array)

new_val = tel[max_val]
