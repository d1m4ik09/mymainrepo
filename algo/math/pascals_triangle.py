def generate(numRows: int):
    lists = [[1], [1, 1]]
    last_list = [1, 1]
 
    if numRows == 1:
        return [[1]]
    
    if numRows == 2:
        return lists
    
    for i in range(3, numRows + 1):
        list = [1, 1]
 
        for j in range(1, i - 1):
            list.insert(j, last_list[j -1] + last_list[j])
 
        lists.append(list)
        last_list = lists[-1]

    return lists

generate(int(input()))