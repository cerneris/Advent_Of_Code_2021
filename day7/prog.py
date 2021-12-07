def day_6_part_1():
    data = open("input.txt", "r")
    line = data.readline()
    values = [int(i.strip()) for i in line.split(",")]

    values_list = []
    for i in values:
        temp = 0
        for j in values:
            if j == i:
                pass
            if j > i:
                temp += (j - i)
            else:
                temp += (i - j)
        values_list.append(temp)
    print(min(values_list))
    
def day_6_part_2():
    data = open("input.txt", "r")
    line = data.readline()
    values = [int(i.strip()) for i in line.split(",")]
    max_val = max(values)
    values_list = []
    for j in range(max_val + 1):
        temp1 = 0
        temp2 = 0
        for i in values:
            if i == j:
                continue
            if i < j:
                temp1 = j - i
            else:
                temp1 = i - j
            temp2 += int(temp1 * (temp1 + 1) / 2)
        values_list.append(temp2)
    print(min(values_list))
    
day_6_part_1()
day_6_part_2()