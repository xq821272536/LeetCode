# -*- coding: utf-8 -*-
import time
"""
Spyder Editor

This is a temporary script file.
"""
#import numpy as np
start = time.time()

class Solution(object):
    def minimalSteps(self, maze):
        m = len(maze)
        n = len(maze[0])
        
        self.mm = {}
        walls = []
        Ms = {}
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'S':
                    start = i*n+j
                if maze[i][j] == 'T':
                    target = i*n+j
                if maze[i][j] == '#':
                    walls.append(i*n+j)
                if maze[i][j] == 'M':
                    Ms[i*n+j] = 0
        print(start)
        print(target)
        print(walls)
        print(Ms)
        matric = []
        for i in range(m*n):
            x, y = i // n, i % n
            row = [0]*(m*n)
            if not [x, y] in walls:
                if i % n != 0 and maze[(i-1) // n][(i-1) % n] != '#':
                    row[i-1] = 1
                if (i+1) % n != 0 and maze[(i+1) // n][(i+1) % n] != '#':
                    row[i+1] = 1
                if i >= n and maze[(i-n) // n][(i-n) % n] != '#':
                    row[i-n] = 1
                if i < (m*n-n) and maze[(i+n) // n][(i+n) % n] != '#':
                    row[i+n] = 1
            matric.append(row)
        self.mm[1] = matric
        present = matric
        while Ms
        

matrix = ["S#O", "M..", "M.T"]
print(Solution().minimalSteps(matrix))
print(time.time()-start)























