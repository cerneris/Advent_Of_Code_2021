import math

class day5:
    def __init__(self):
        self._points = self.load_input()
        self._points2 = []
        self._array = [ [ "." for y in range( 1000 ) ] for x in range( 1000 ) ]
        self._calc = 0

    def load_input(self):
        data = open("input.txt", "r")
        points = []
        for line in data.readlines():
            point = line.strip().split("->")
            start = point[0].split(",")
            stop = point[1].split(",")
            points.append([start, stop])
        return points

    def draw_line_straight(self, point, array):
        x1 = int(point[0][0])
        y1 = int(point[0][1])
        x2 = int(point[1][0])
        y2 = int(point[1][1])

        if x1 > x2:
            x2 -= 1
            step_x = -1
        elif x1 == x2:
            pass
        else:
            x2 += 1
            step_x = 1
        if y1 > y2:
            y2 -= 1
            step_y = -1
        elif y1 == y2:
            pass
        else:
            y2 += 1
            step_y = 1
        if x1 == x2:
            for i in range(y1, y2, step_y):
                if self._array[i][x1] == ".":
                    self._array[i][x1] = 1
                else:
                    self._array[i][x1] += 1

        elif y1 == y2:
            for i in range(x1, x2, step_x):
                if self._array[y1][i] == ".":
                    self._array[y1][i] = 1
                else:
                    self._array[y1][i] += 1
        
        else:
            self._points2.append(point)

    def draw_line_diagonal(self, point, array):
        x1 = int(point[0][0])
        y1 = int(point[0][1])
        x2 = int(point[1][0])
        y2 = int(point[1][1])
        radians = math.atan2(y1-y2, x1-x2)
        degrees = math.degrees(radians)
        if x1 > x2:
            x2 -= 1
            step_x = -1
        elif x1 == x2:
            pass
        else:
            x2 += 1
            step_x = 1
        if y1 > y2:
            y2 -= 1
            step_y = -1
        elif y1 == y2:
            pass
        else:
            y2 += 1
            step_y = 1
        for i in range(y1, y2, step_y):
            if self._array[i][x1] == ".":
                self._array[i][x1] = 1
            else:
                self._array[i][x1] += 1
            if x1 == x2:
                continue
            else:
                x1 += step_x

        for i in range(x1, x2, step_x):
            if self._array[y1][i] == ".":
                self._array[y1][i] = 1
            else:
                self._array[y1][i] += 1
            if y1 == y2:
                continue
            else:
                y1 += step_y

    def draw_board_part_1(self):
        for i in range(len(self._points)):
            self.draw_line_straight(self._points[i], self._array)
        for i in self._array:
            for j in i:
                try:
                    if int(j) >= 2:
                        self._calc += 1
                except:
                    continue
        print("Total number of intersections with horizontal or vertical lines: {}".format(self._calc))

    def draw_board_part_2(self):
        self._calc = 0
        for i in range(len(self._points2)):
            self.draw_line_diagonal(self._points2[i], self._array)
        for i in self._array:
            for j in i:
                try:
                    if int(j) >= 2:
                        self._calc += 1
                except:
                    continue
        print("Total number of intersections with horizontal, vertical or diagonal lines: {}".format(self._calc))

day_5 = day5()
day_5.draw_board_part_1()
day_5.draw_board_part_2()