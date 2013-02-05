import threading
import sys


def main(length):
    start1 = (length, 2)
    start2 = (length - 1, 1)
    one = CalculatePaths(length, start1)
    two = CalculatePaths(length, start2)
    one.start()
    two.start()


class CalculatePaths(threading.Thread):
    def __init__(self, sideLength, startPosition):
        threading.Thread.__init__(self)
        self.sideLength = sideLength
        self.startPosition = startPosition

    def run(self):
        k = self.walk(self.sideLength, self.startPosition)
        print k

    def walk(self, sideLength, startPosition):
        max1 = sideLength + 1
        min1 = 0
        pathsList = []
        start = ((startPosition), [(sideLength, 0), (sideLength, 1)])
        end = (0, sideLength)
        current = start
        pathNumber = 0

        while True:
            for node in self.getNextNodes(current, max1, min1):
                pathsList.append(node)
            if pathsList:
                current = pathsList.pop()
            else:
                break
            while current[0] == end:
                pathNumber += 1
                #print(pathNumber)
                if pathsList:
                    current = pathsList.pop()
                else:
                    break

        #print(pathNumber*2)
        return pathNumber

    def getNextNodes(self, node, max1, min1):
        nextNodes = []
        previousNodes = node[1]
        current = node[0]
        x = current[0]
        y = current[1]
        a = (x + 1, y)
        b = (x, y + 1)
        c = (x - 1, y)
        d = (x, y - 1)

        for i in a, b, c, d:
            if (i not in previousNodes) & (i[0] < max1) & (i[1] < max1) &\
                    (i[0] >= min1) & (i[1] >= min1):
                newPastNodes = []
                newPastNodes.insert(0, current)
                for node in previousNodes:
                    newPastNodes.append(node)
                nextNodes.append((i, newPastNodes))
            else:
                pass
        return nextNodes
length = int(sys.argv[1])
main(length)
