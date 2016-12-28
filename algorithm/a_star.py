# -*- coding: utf-8 -*-
import bisect

class Node:
    def __init__(self, x, y, parent=None, g=0, h=0):
        self.x, self.y = x, y
        self.parent = parent
        self.g, self.h = g, h
        self.f = g + h

    def get_path(self):
        path = []

        t = self
        while t:
            path.append((t.x, t.y))
            t = t.parent

        path.reverse()
        return path

    def __cmp__(self, other):
        return other.f - self.f

    def __str__(self):
        return "{(%d, %d), g: %d, h: %d, f: %d}" % (self.x, self.y, self.g, self.h, self.f)


class _OpenList(list):
    def __init__(self):
        self._nodes = {}

    def push(self, node):
        # 按f值逆排序
        key = "%d,%d" % (node.x, node.y)
        assert key not in self._nodes

        idx = bisect.bisect_right(self, node)  #f值相同，后插入优先
        self.insert(idx, node)
        self._nodes[key] = node

        #print "push:", node
        #print "insert idx:", idx

    def remove(self, node):
        assert node in self

        key = "%d,%d" % (node.x, node.y)
        assert key in self._nodes

        #print "remove", node

        del self._nodes[key]
        b = bisect.bisect_left(self, node)
        e = bisect.bisect_right(self, node)
        assert b < e
        for i in range(b, e):
            if self[i] is node:
                del self[i]
                #print "del idx:", i
                break

    def get(self, x, y):
        key = "%d,%d" % (x, y)
        return self._nodes.get(key)

    def __contains__(self, item):
        key = "%d,%d" % (item.x, item.y)
        return key in self._nodes


DIRS = ((1, 0, 1000), (1, -1, 1414), (0, -1, 1000), (-1, -1, 1414), (-1, 0, 1000), (-1, 1, 1414), (0, 1, 1000), (1, 1, 1414), )

def search_path(map, sx, sy, ex, ey):
    if sx == ex and sy == ey:
        return [(sx, sy), (ex, ey)]

    calc_h = lambda x, y: abs(x-ex) + abs(y-ey)
    rows = len(map)
    cols = len(map[0])
    open_list = _OpenList()
    close_set = set()
    begin = Node(sx, sy)
    open_list.push(begin)

    while open_list:
        current = open_list.pop()
        close_set.add((current.x, current.y))

        for dx, dy, g in DIRS:
            x = current.x + dx
            y = current.y + dy
            if x < 0 or y < 0 or x >= cols or y >= rows:
                continue
            if not map[y][x] or (x, y) in close_set:
                continue

            node = Node(x, y, current, current.g + g, calc_h(x, y))
            if x == ex and y == ey:
                return node.get_path()

            if node in open_list:
                node2 = open_list.get(x, y)
                if node2.g > node.g:
                    open_list.remove(node2)
                    open_list.push(node)
            else:
                open_list.push(node)
    else:
        return []


def print_path(map, path):
    rows = len(map)
    cols = len(map[0])

    print ' ',
    for col in range(0, cols):
        print col,
    print

    for row in range(0, rows):
        print row,
        for col in range(0, cols):
            if map[row][col] == 0:
                print '^',
            else:
                if (col, row) in path:
                    print '-',
                else:
                    print '.',

        print

if __name__ == '__main__':
    map = []
    for row in range(0, 7):
        map.append([])
        for col in range(0, 9):
            map[-1].append(1)

    map[1][4] = 0
    map[2][4] = 0
    map[3][4] = 0
    map[4][4] = 0
    map[5][4] = 0

    path = search_path(map, 2, 3, 6, 3)

    print_path(map, path)