def day_2_part_1():
    data = open("input.txt", "r")
    
    horizontal = 0
    depth = 0
    for line in data.readlines():
        val = line.strip().split(" ")
        command = val[0]
        value = int(val[1])
        if command == "forward":
            horizontal += value
        elif command == "up":
            depth -= value
        else:
            depth += value
    print("Day 1 answer: {}".format(depth*horizontal))
    
def day_2_part_2():
    data = open("input.txt", "r")
    
    horizontal = 0
    depth = 0
    aim = 0
    for line in data.readlines():
        val = line.strip().split(" ")
        command = val[0]
        value = int(val[1])
        if command == "forward":
            temp_horizontal = value
            horizontal += value
            if aim == 0:
                continue
            else:
                depth += aim*temp_horizontal
        elif command == "up":
            aim -= value
        else:
            aim += value
    print("Day 2 answer: {}".format(depth*horizontal))
        
day_2_part_1()
day_2_part_2()