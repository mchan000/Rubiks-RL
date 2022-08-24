import os
import random
import math
import time


class Face:
    def __init__(self, color):
        self.tF = [''] * 3
        for i in range(3):
            self.tF[i] = [color] * 3

        # ctr = 1
        # for i in range(3):
        #     self.tF[i] = [''] * 3
        #     for j in range(3):
        #         if color == "r":
        #             self.tF[i][j] = '\u001b[31m' + str(ctr) + '\u001b[0m'
        #         elif color == "g":
        #             self.tF[i][j] = '\u001b[32m' + str(ctr) + '\u001b[0m'
        #         elif color == 'w':
        #             self.tF[i][j] = str(ctr)
        #         elif color == 'b':
        #             self.tF[i][j] = '\u001b[34m' + str(ctr) + '\u001b[0m'
        #         elif color == 'y':
        #             self.tF[i][j] = '\u001b[38;5;11m' + str(ctr) + '\u001b[0m'
        #         elif color == 'o':
        #             self.tF[i][j] = '\u001b[38;5;208m' + str(ctr) + '\u001b[0m'
        #         ctr += 1

    def __str__(self):
        to_string = ""
        for i in self.tF:
            for j in range(len(i)):
                if (j + 1) % 3 == 0:
                    to_string += i[j] + '\n'
                else:
                    to_string += i[j] + ' '
        return to_string

    def clockwise(self):
        self.tF = [list(r) for r in zip(*self.tF[::-1])]

    def c_clockwise(self):
        self.tF = [[self.tF[j][i] for j in range(len(self.tF))] for i in range(len(self.tF[0]) - 1, -1, -1)]


class Cube:

    def __init__(self):
        self.tC = [''] * 6
        colors = ["w", "o", "g", "r", "b", "y"]
        for i in range(len(colors)):
            self.tC[i] = Face(colors[i])

    def __str__(self):
        to_string = ('%7s' %
                     self.tC[0].tF[0][0] + ' ' + self.tC[0].tF[0][1] + ' ' + self.tC[0].tF[0][2] +
                     "\n" +
                     '%7s' %
                     self.tC[0].tF[1][0] + ' ' + self.tC[0].tF[1][1] + ' ' + self.tC[0].tF[1][2] +
                     "\n" +
                     '%7s' %
                     self.tC[0].tF[2][0] + ' ' + self.tC[0].tF[2][1] + ' ' + self.tC[0].tF[2][2] +
                     "\n" +
                     self.tC[1].tF[0][0] + ' ' + self.tC[1].tF[0][1] + ' ' + self.tC[1].tF[0][2] +
                     ' ' +
                     self.tC[2].tF[0][0] + ' ' + self.tC[2].tF[0][1] + ' ' + self.tC[2].tF[0][2] +
                     ' ' +
                     self.tC[3].tF[0][0] + ' ' + self.tC[3].tF[0][1] + ' ' + self.tC[3].tF[0][2] +
                     ' ' +
                     self.tC[4].tF[0][0] + ' ' + self.tC[4].tF[0][1] + ' ' + self.tC[4].tF[0][2] +
                     '\n' +
                     self.tC[1].tF[1][0] + ' ' + self.tC[1].tF[1][1] + ' ' + self.tC[1].tF[1][2] +
                     ' ' +
                     self.tC[2].tF[1][0] + ' ' + self.tC[2].tF[1][1] + ' ' + self.tC[2].tF[1][2] +
                     ' ' +
                     self.tC[3].tF[1][0] + ' ' + self.tC[3].tF[1][1] + ' ' + self.tC[3].tF[1][2] +
                     ' ' +
                     self.tC[4].tF[1][0] + ' ' + self.tC[4].tF[1][1] + ' ' + self.tC[4].tF[1][2] +
                     '\n' +
                     self.tC[1].tF[2][0] + ' ' + self.tC[1].tF[2][1] + ' ' + self.tC[1].tF[2][2] +
                     ' ' +
                     self.tC[2].tF[2][0] + ' ' + self.tC[2].tF[2][1] + ' ' + self.tC[2].tF[2][2] +
                     ' ' +
                     self.tC[3].tF[2][0] + ' ' + self.tC[3].tF[2][1] + ' ' + self.tC[3].tF[2][2] +
                     ' ' +
                     self.tC[4].tF[2][0] + ' ' + self.tC[4].tF[2][1] + ' ' + self.tC[4].tF[2][2] +
                     '\n%7s' %
                     self.tC[5].tF[0][0] + ' ' + self.tC[5].tF[0][1] + ' ' + self.tC[5].tF[0][2] +
                     "\n" +
                     '%7s' %
                     self.tC[5].tF[1][0] + ' ' + self.tC[5].tF[1][1] + ' ' + self.tC[5].tF[1][2] +
                     "\n" +
                     '%7s' %
                     self.tC[5].tF[2][0] + ' ' + self.tC[5].tF[2][1] + ' ' + self.tC[5].tF[2][2])
        colorize = ''
        for i in range(len(to_string)):
            if to_string[i] == "r":
                colorize += '\u001b[31m■\u001b[0m'
            elif to_string[i] == "g":
                colorize += '\u001b[32m■\u001b[0m'
            elif to_string[i] == 'w':
                colorize += '■'
            elif to_string[i] == 'b':
                colorize += '\u001b[34m■\u001b[0m'
            elif to_string[i] == 'y':
                colorize += '\u001b[38;5;11m■\u001b[0m'
            elif to_string[i] == 'o':
                colorize += '\u001b[38;5;208m■\u001b[0m'
            else:
                colorize += to_string[i]
        return colorize
        # return to_string

    def print_arr(self):
        pseq = ''
        rseq = ''
        ctr = 1
        for face in self.tC:
            for row in face.tF:
                for sqr in row:
                    if ctr % 9 == 0:
                        pseq += sqr + '\n'
                    else:
                        pseq += sqr + ' '
                    rseq += sqr
                    ctr += 1
        print(pseq)
        return rseq

    def u(self):
        tmp = self.tC[1].tF[0]
        self.tC[1].tF[0] = self.tC[2].tF[0]
        self.tC[2].tF[0] = self.tC[3].tF[0]
        self.tC[3].tF[0] = self.tC[4].tF[0]
        self.tC[4].tF[0] = tmp
        self.tC[0].clockwise()

    def up(self):
        tmp = self.tC[4].tF[0]
        self.tC[4].tF[0] = self.tC[3].tF[0]
        self.tC[3].tF[0] = self.tC[2].tF[0]
        self.tC[2].tF[0] = self.tC[1].tF[0]
        self.tC[1].tF[0] = tmp
        self.tC[0].c_clockwise()

    def d(self):
        tmp = self.tC[4].tF[2]
        self.tC[4].tF[2] = self.tC[3].tF[2]
        self.tC[3].tF[2] = self.tC[2].tF[2]
        self.tC[2].tF[2] = self.tC[1].tF[2]
        self.tC[1].tF[2] = tmp
        self.tC[5].clockwise()

    def dp(self):
        tmp = self.tC[1].tF[2]
        self.tC[1].tF[2] = self.tC[2].tF[2]
        self.tC[2].tF[2] = self.tC[3].tF[2]
        self.tC[3].tF[2] = self.tC[4].tF[2]
        self.tC[4].tF[2] = tmp
        self.tC[5].c_clockwise()

    def r(self):
        u = self.tC[0].tF[0][2]
        m = self.tC[0].tF[1][2]
        d = self.tC[0].tF[2][2]

        self.tC[0].tF[0][2] = self.tC[2].tF[0][2]
        self.tC[0].tF[1][2] = self.tC[2].tF[1][2]
        self.tC[0].tF[2][2] = self.tC[2].tF[2][2]

        self.tC[2].tF[0][2] = self.tC[5].tF[0][2]
        self.tC[2].tF[1][2] = self.tC[5].tF[1][2]
        self.tC[2].tF[2][2] = self.tC[5].tF[2][2]

        self.tC[5].tF[0][2] = self.tC[4].tF[2][0]
        self.tC[5].tF[1][2] = self.tC[4].tF[1][0]
        self.tC[5].tF[2][2] = self.tC[4].tF[0][0]

        self.tC[4].tF[0][0] = d
        self.tC[4].tF[1][0] = m
        self.tC[4].tF[2][0] = u

        self.tC[3].clockwise()

    def rp(self):
        u = self.tC[4].tF[0][0]
        m = self.tC[4].tF[1][0]
        d = self.tC[4].tF[2][0]

        self.tC[4].tF[0][0] = self.tC[5].tF[2][2]
        self.tC[4].tF[1][0] = self.tC[5].tF[1][2]
        self.tC[4].tF[2][0] = self.tC[5].tF[0][2]

        self.tC[5].tF[0][2] = self.tC[2].tF[0][2]
        self.tC[5].tF[1][2] = self.tC[2].tF[1][2]
        self.tC[5].tF[2][2] = self.tC[2].tF[2][2]

        self.tC[2].tF[0][2] = self.tC[0].tF[0][2]
        self.tC[2].tF[1][2] = self.tC[0].tF[1][2]
        self.tC[2].tF[2][2] = self.tC[0].tF[2][2]

        self.tC[0].tF[0][2] = d
        self.tC[0].tF[1][2] = m
        self.tC[0].tF[2][2] = u

        self.tC[3].c_clockwise()

    def l(self):
        u = self.tC[5].tF[0][0]
        m = self.tC[5].tF[1][0]
        d = self.tC[5].tF[2][0]

        self.tC[5].tF[0][0] = self.tC[2].tF[0][0]
        self.tC[5].tF[1][0] = self.tC[2].tF[1][0]
        self.tC[5].tF[2][0] = self.tC[2].tF[2][0]

        self.tC[2].tF[0][0] = self.tC[0].tF[0][0]
        self.tC[2].tF[1][0] = self.tC[0].tF[1][0]
        self.tC[2].tF[2][0] = self.tC[0].tF[2][0]

        self.tC[0].tF[0][0] = self.tC[4].tF[2][2]
        self.tC[0].tF[1][0] = self.tC[4].tF[1][2]
        self.tC[0].tF[2][0] = self.tC[4].tF[0][2]

        self.tC[4].tF[0][2] = d
        self.tC[4].tF[1][2] = m
        self.tC[4].tF[2][2] = u

        self.tC[1].clockwise()

    def lp(self):
        u = self.tC[0].tF[0][0]
        m = self.tC[0].tF[1][0]
        d = self.tC[0].tF[2][0]

        self.tC[0].tF[0][0] = self.tC[2].tF[0][0]
        self.tC[0].tF[1][0] = self.tC[2].tF[1][0]
        self.tC[0].tF[2][0] = self.tC[2].tF[2][0]

        self.tC[2].tF[0][0] = self.tC[5].tF[0][0]
        self.tC[2].tF[1][0] = self.tC[5].tF[1][0]
        self.tC[2].tF[2][0] = self.tC[5].tF[2][0]

        self.tC[5].tF[0][0] = self.tC[4].tF[2][2]
        self.tC[5].tF[1][0] = self.tC[4].tF[1][2]
        self.tC[5].tF[2][0] = self.tC[4].tF[0][2]

        self.tC[4].tF[2][2] = u
        self.tC[4].tF[1][2] = m
        self.tC[4].tF[0][2] = d

        self.tC[1].c_clockwise()

    def f(self):
        u = self.tC[5].tF[0][0]
        m = self.tC[5].tF[0][1]
        d = self.tC[5].tF[0][2]

        self.tC[5].tF[0][0] = self.tC[3].tF[2][0]
        self.tC[5].tF[0][1] = self.tC[3].tF[1][0]
        self.tC[5].tF[0][2] = self.tC[3].tF[0][0]

        self.tC[3].tF[0][0] = self.tC[0].tF[2][0]
        self.tC[3].tF[1][0] = self.tC[0].tF[2][1]
        self.tC[3].tF[2][0] = self.tC[0].tF[2][2]

        self.tC[0].tF[2][0] = self.tC[1].tF[2][2]
        self.tC[0].tF[2][1] = self.tC[1].tF[1][2]
        self.tC[0].tF[2][2] = self.tC[1].tF[0][2]

        self.tC[1].tF[0][2] = u
        self.tC[1].tF[1][2] = m
        self.tC[1].tF[2][2] = d

        self.tC[2].clockwise()

    def fp(self):
        u = self.tC[5].tF[0][0]
        m = self.tC[5].tF[0][1]
        d = self.tC[5].tF[0][2]

        self.tC[5].tF[0][0] = self.tC[1].tF[0][2]
        self.tC[5].tF[0][1] = self.tC[1].tF[1][2]
        self.tC[5].tF[0][2] = self.tC[1].tF[2][2]

        self.tC[1].tF[0][2] = self.tC[0].tF[2][2]
        self.tC[1].tF[1][2] = self.tC[0].tF[2][1]
        self.tC[1].tF[2][2] = self.tC[0].tF[2][0]

        self.tC[0].tF[2][0] = self.tC[3].tF[0][0]
        self.tC[0].tF[2][1] = self.tC[3].tF[1][0]
        self.tC[0].tF[2][2] = self.tC[3].tF[2][0]

        self.tC[3].tF[0][0] = d
        self.tC[3].tF[1][0] = m
        self.tC[3].tF[2][0] = u

        self.tC[2].c_clockwise()

    def b(self):
        u = self.tC[0].tF[0][0]
        m = self.tC[0].tF[0][1]
        d = self.tC[0].tF[0][2]

        self.tC[0].tF[0][0] = self.tC[3].tF[0][2]
        self.tC[0].tF[0][1] = self.tC[3].tF[1][2]
        self.tC[0].tF[0][2] = self.tC[3].tF[2][2]

        self.tC[3].tF[0][2] = self.tC[5].tF[2][2]
        self.tC[3].tF[1][2] = self.tC[5].tF[2][1]
        self.tC[3].tF[2][2] = self.tC[5].tF[2][0]

        self.tC[5].tF[2][0] = self.tC[1].tF[0][0]
        self.tC[5].tF[2][1] = self.tC[1].tF[1][0]
        self.tC[5].tF[2][2] = self.tC[1].tF[2][0]

        self.tC[1].tF[0][0] = d
        self.tC[1].tF[1][0] = m
        self.tC[1].tF[2][0] = u
        self.tC[4].clockwise()

    def bp(self):
        u = self.tC[0].tF[0][0]
        m = self.tC[0].tF[0][1]
        d = self.tC[0].tF[0][2]

        self.tC[0].tF[0][0] = self.tC[1].tF[2][0]
        self.tC[0].tF[0][1] = self.tC[1].tF[1][0]
        self.tC[0].tF[0][2] = self.tC[1].tF[0][0]

        self.tC[1].tF[0][0] = self.tC[5].tF[2][0]
        self.tC[1].tF[1][0] = self.tC[5].tF[2][1]
        self.tC[1].tF[2][0] = self.tC[5].tF[2][2]

        self.tC[5].tF[2][0] = self.tC[3].tF[2][2]
        self.tC[5].tF[2][1] = self.tC[3].tF[1][2]
        self.tC[5].tF[2][2] = self.tC[3].tF[0][2]

        self.tC[3].tF[0][2] = u
        self.tC[3].tF[1][2] = m
        self.tC[3].tF[2][2] = d

        self.tC[4].c_clockwise()


def c_clockwise(a):
    return list(zip(*a))[::-1]


def clockwise(a):
    return zip(*a[::-1])


def shuffle(cube, num):
    if num == 0:
        cube.u()
        return 'U'
    elif num == 1:
        cube.up()
        return "U'"
    elif num == 2:
        cube.d()
        return "D"
    elif num == 3:
        cube.dp()
        return "D'"
    elif num == 4:
        cube.l()
        return "L"
    elif num == 5:
        cube.lp()
        return "L'"
    elif num == 6:
        cube.r()
        return "R"
    elif num == 7:
        cube.rp()
        return "R'"
    elif num == 8:
        cube.f()
        return "F"
    elif num == 9:
        cube.fp()
        return "F'"
    elif num == 10:
        cube.b()
        return "B"
    elif num == 11:
        cube.bp()
        return "B'"


if __name__ == '__main__':
    c = Cube()
    shuffleseq = 'Shuffle sequence: '
    for i in range(20):
        n = math.floor(random.random() * 12)
        move = shuffle(c, n)
        shuffleseq += str(move) + ' '
    print(c)
    print(shuffleseq)