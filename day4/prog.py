class day_4():
    def __init__(self):
        self._boards, self._numbers = self.create_boards()

    def check_vals(self, board, number):
        row = 0
        for val in board:
            for num in val:
                if num == "x":
                    continue
                elif num == number:
                    index = board[row].index(number)
                    board[row][index] = "x"
                else:
                    continue
            row += 1
        for i in range(5):
            calc_ver = 0
            calc_hor = 0
            for j in range(5):
                if board[i][j] == "x":
                    calc_ver += 1
                if board[j][i] == "x":
                    calc_hor += 1
                if calc_ver == 5 or calc_hor == 5:
                    return board, True
                    break
        if calc_ver == 5 or calc_hor == 5:
            return board, True
        return board, False
                
    def calculate_board(self, board, number):
        value = 0
        for val in board:
            for num in val:
                if num == "x":
                    continue
                else:
                    value += int(num)
        return value * int(number)

    def create_boards(self):
        data = open("input.txt", "r")
        bingo_vals = data.readline()
        data.readline()
        line = 0
        temp_list = []
        board_list = []
        while True:
            val = data.readline()
            if val == "\n":
                board_list.append(temp_list)
                temp_list = []
            elif val == '':
                board_list.append(temp_list)
                break
            else:
                temp_list.append(val.replace("  ", " ").strip().split(" "))
        return board_list, bingo_vals
    
    def get_winner(self):
        winner = []
        win = False
        for i in self._numbers.split(","):
            if win == True:
                break
            for boards in range(len(self._boards)):
                self._boards[boards], status = self.check_vals(self._boards[boards], i)
                if status == True:
                    winner = self._boards[boards]
                    win = True
                    winning_number = i
                    break
        print("Final score is: {}".format(self.calculate_board(winner, winning_number)))

    def last_winner(self):
        winners = []
        last = False
        last_winner = []
        for i in self._numbers.split(","):
            winners = []
            if last == True:
                break
            for boards in range(len(self._boards)):
                self._boards[boards], status = self.check_vals(self._boards[boards], i)
                if status == True:
                    if len(self._boards) == 1:
                        last = True
                        last_winner = self._boards[boards]
                        winning_number = i
                        break
                    winners.append(boards)
            temp = 0
            for j in winners:
                print(j)
                self._boards.pop(j-temp)
                temp += 1
        print("Final score for last winner: {}".format(self.calculate_board(last_winner, winning_number)))

    def main(self):
        print("Part 1:")
        self.get_winner()
        print("Part 2:")
        self.last_winner()

day4 = day_4()
day4.main()