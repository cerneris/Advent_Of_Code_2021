def day_6(days):
    data = open("input.txt", "r")
    line = data.readline()
    values = [int(i.strip()) for i in line.split(",")]
    list_of_fish = [0 for i in range(9)]
    for fish in values:
        list_of_fish[fish] += 1
    for days in range(days):
        spawn = list_of_fish[0]
        list_of_fish = list_of_fish[1:] + [spawn]
        list_of_fish[6] += spawn
    print("Total amount of fish after {} days: {}".format(days+1, sum(list_of_fish)))
        
        
day_6(80)
day_6(256)