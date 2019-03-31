''' Matrix addition 
    
[[12 , 10], [03 , 09]]
  |     |    |    |
[[03 , 04], [07 , 04]]

    12 + 3 = 15 
    10 + 4 = 14
    03 + 7 = 10
    09 + 4 = 13
'''
## Code Date : 01-4-2019

def add(matrix_a, matrix_b):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    matrix_c = []
    for i in range(rows):
        list_1 = []
        for j in range(columns):
            val = matrix_a[i][j] + matrix_b[i][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c

def main():
    matrix_a = [[12, 10], [3, 9]]
    matrix_b = [[3, 4], [7, 4]]
    print('The Matrix addition is :',add(matrix_a, matrix_b))
   
if __name__ == '__main__':
    main()
