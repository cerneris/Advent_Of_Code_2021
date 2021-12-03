class day_3:
    def __init__(self):
        self.power_consumpt = 0
        self.life_support = 1
        
    def day_3_part_1(self, data):
        ones = 0
        zeroes = 0
        gamma = []
        epsilon = []
        data_len = len(data)
        bin_len = len(data[0].strip())
        for i in range(bin_len):
            for j in range(data_len):
                if data[j][i] == "0":
                    zeroes += 1
                else:
                    ones += 1
            if ones > zeroes:
                gamma.append("1")
                epsilon.append("0")
            else:
                gamma.append("0")
                epsilon.append("1")
            ones = 0
            zeroes = 0
        gamma = int("".join(gamma), 2)
        epsilon = int("".join(epsilon), 2)
        
        self.power_consumpt = gamma*epsilon
        print("Power consumption is {}.".format(self.power_consumpt))

    def day_3_part_2(self, data, j=0, rec=1):
        new_data_1 = []
        new_data_2 = []
        ones = 0
        zeroes = 0
        for i in range(len(data)):
            if data[i][j] == "0":
                zeroes += 1
            else:
                ones += 1
        if zeroes > ones:
            main = "0"
            sec = "1"
        elif zeroes == ones:
            main = "1"
            sec = "0"
        else:
            main = "1"
            sec = "0"
        for i in range(len(data)):
            if data[i][j] == main:
                new_data_1.append(data[i])
            else:
                new_data_2.append(data[i])
        if j == len(data[0]) or len(data) == 1:
            self.life_support = self.life_support * int(data[0], 2)
        else:
            j += 1
            if rec == 1:
                self.day_3_part_2(new_data_1, j, rec)
            else:
                self.day_3_part_2(new_data_2, j, rec)

    def day_3_combine_and_calc(self, data):
        self.day_3_part_2(data, 0, 1)
        self.day_3_part_2(data, 0, 2)
        print("Life support rating is {}.".format(self.life_support))
    
    
data = open("input.txt", "r").readlines()
day_3_class = day_3()
day_3_class.day_3_part_1(data)
day_3_class.day_3_combine_and_calc(data)