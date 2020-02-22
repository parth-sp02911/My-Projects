#Parth Patel
#2018 J4/S2 Sunflower Code

def rotate(table, new_table):   #Multiply count by num of sunflowers
    r = 0
    c = 0
    count = len(table)
    for row in range(count):
        for column in range(count-1, -1, -1):

            new_table[c][r].append(table[column][row][0])
            r += 1
        c += 1
        r = 0

    return new_table
    
num_of_sunflowers = int(input("Enter the number of sunflowers: "))
data_table = []
empty_table = []
for row in range(num_of_sunflowers):

    row_info = (input("")).split()
    data_table.append([])
    empty_table.append([])
    for column in range(num_of_sunflowers):
        empty_table[row].append([])
        data_table[row].append([])

        data_table[row][column].append(int(row_info[column]))



for i in rotate(data_table, empty_table):
    print (i)
print("")
for i in data_table:
    print (i)

