import os
import random
import math
import time
import numpy as np


class Face:
    def __init__(self, color):
        self.tF = [''] * 3
        for i in range(3):
            self.tF[i] = [color] * 3

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
        return colorize + '\n'

    # def print_arr(self):
    #     pseq = ''
    #     rseq = ''
    #     ctr = 1
    #     for face in self.tC:
    #         for row in face.tF:
    #             for sqr in row:
    #                 if ctr % 9 == 0:
    #                     pseq += sqr + '\n'
    #                 else:
    #                     pseq += sqr + ' '
    #                 rseq += sqr
    #                 ctr += 1
    #     print(pseq)
    #     return rseq

    def u(self):
        """Rotate upper layer of cube clockwise"""
        tmp = self.tC[1].tF[0]
        self.tC[1].tF[0] = self.tC[2].tF[0]
        self.tC[2].tF[0] = self.tC[3].tF[0]
        self.tC[3].tF[0] = self.tC[4].tF[0]
        self.tC[4].tF[0] = tmp
        self.tC[0].clockwise()

    def up(self):
        """Rotate upper layer of cube counter clockwise"""
        tmp = self.tC[4].tF[0]
        self.tC[4].tF[0] = self.tC[3].tF[0]
        self.tC[3].tF[0] = self.tC[2].tF[0]
        self.tC[2].tF[0] = self.tC[1].tF[0]
        self.tC[1].tF[0] = tmp
        self.tC[0].c_clockwise()

    def d(self):
        """Rotate bottom layer of cube clockwise"""
        tmp = self.tC[4].tF[2]
        self.tC[4].tF[2] = self.tC[3].tF[2]
        self.tC[3].tF[2] = self.tC[2].tF[2]
        self.tC[2].tF[2] = self.tC[1].tF[2]
        self.tC[1].tF[2] = tmp
        self.tC[5].clockwise()

    def dp(self):
        """Rotate bottom layer of cube counter clockwise"""
        tmp = self.tC[1].tF[2]
        self.tC[1].tF[2] = self.tC[2].tF[2]
        self.tC[2].tF[2] = self.tC[3].tF[2]
        self.tC[3].tF[2] = self.tC[4].tF[2]
        self.tC[4].tF[2] = tmp
        self.tC[5].c_clockwise()

    def r(self):
        """Rotate right side of cube clockwise"""
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
        """Rotate right side of cube counter clockwise"""
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
        """Rotate left side of cube clockwise"""
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
        """Rotate left side of cube counter clockwise"""
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
        """Rotate face of cube clockwise"""
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
        """Rotate face of cube counter clockwise"""
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
        """Rotate back side of cube clockwise"""
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
        """Rotate back side of cube counter clockwise"""
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

    def shuffle(self):
        """Shuffles the cube randomly"""
        shuffle_seq = ''
        last_move = 100
        count = 0
        # Shuffles 9 times
        while count != 9:
            num = math.floor(random.random() * 12)
            # num = 6

            if num % 2 == 1:
                while num == last_move - 1:
                    num = math.floor(random.random() * 12)
            if num % 2 == 0:
                while num == last_move + 1:
                    num = math.floor(random.random() * 12)

            if num == 0 and last_move != 1:
                self.u()
                shuffle_seq += 'U '
                count += 1
            elif num == 1 and last_move != 0:
                self.up()
                shuffle_seq += "U' "
                count += 1
            elif num == 2 and last_move != 3:
                self.d()
                shuffle_seq += "D "
                count += 1
            elif num == 3 and last_move != 2:
                self.dp()
                shuffle_seq += "D' "
                count += 1
            elif num == 4 and last_move != 5:
                self.l()
                shuffle_seq += "L "
                count += 1
            elif num == 5 and last_move != 4:
                self.lp()
                shuffle_seq += "L' "
                count += 1
            elif num == 6 and last_move != 7:
                self.r()
                shuffle_seq += "R "
                count += 1
            elif num == 7 and last_move != 6:
                self.rp()
                shuffle_seq += "R' "
                count += 1
            elif num == 8 and last_move != 9:
                self.f()
                shuffle_seq += "F "
                count += 1
            elif num == 9 and last_move != 8:
                self.fp()
                shuffle_seq += "F' "
                count += 1
            elif num == 10 and last_move != 11:
                self.b()
                shuffle_seq += "B "
                count += 1
            elif num == 11 and last_move != 10:
                self.bp()
                shuffle_seq += "B' "
                count += 1
            last_move = num
        return shuffle_seq


def compare(cube1, cube2):
    score = 0

    for i in range(6):
        for j in range(3):
            for k in range(3):
                if cube1.tC[i].tF[j][k] == cube2.tC[i].tF[j][k]:
                    score += 1

    return score


def c_clockwise(a):
    """Rotates 2D array counterclockwise"""
    return list(zip(*a))[::-1]


def clockwise(a):
    """Rotates 2D array clockwise"""
    return zip(*a[::-1])


def flattenCube(c):
    arr = []

    for i in range(6):
        for j in range(3):
            for k in range(3):
                if c.tC[i].tF[j][k] == 'w':
                    arr.append(0)
                elif c.tC[i].tF[j][k] == 'o':
                    arr.append(1)
                elif c.tC[i].tF[j][k] == 'g':
                    arr.append(2)
                elif c.tC[i].tF[j][k] == 'r':
                    arr.append(3)
                elif c.tC[i].tF[j][k] == 'b':
                    arr.append(4)
                elif c.tC[i].tF[j][k] == 'y':
                    arr.append(5)

    return arr
