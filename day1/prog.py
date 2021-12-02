import time
def day_1_part_1():
    data = open("input.txt", "r")

    lines = data.readlines()

    temp = ""
    increased = 0
    for line in lines:
        if temp == "":
            #print("No measurement yet")
            temp = line
            continue
        else:
            if int(line) > int(temp):
                increased += 1
                temp = line
            else:
                temp = line
                
    #print("Measurements increased in {}".format(increased))

def day_1_part_2():    
    data = open("input.txt", "r")

    lines = [int(i) for i in data.readlines()]
    increased = 0
    for line in range(len(lines)):
        data_1 = sum(lines[line:line+3])
        data_2 = sum(lines[line+1:line+4])
        if data_1 < data_2:
            increased += 1
    #print("Measurements increased in {}".format(increased))

times = []
for i in range(500):
    start = time.time()
    #day_1_part_1()
    day_1_part_2()
    end = time.time() - start
    times.append(end)
print("Time taken {}".format(sum(times) / len(times)))
    
