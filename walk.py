import sys
from time import clock


def walk(sideLength):
    startTime = clock()
    max1 = sideLength + 1
    pathsList = []
    start = ((0, 1), [(0, 0)])
    global end
    end = (sideLength, sideLength)
    current = start
    global pathNumber
    pathNumber = 0

    while True:
        for node in getNextNodes(current, max1):
            pathsList.append(node)
        if pathsList:
            current = pathsList.pop()
        else:
            break
    print(pathNumber * 2)
    print(clock() - startTime)


def getNextNodes(node, max1):
    global pathNumber
    nextNodes = []
    previousNodes = node[1]
    current = node[0]
    x = current[0]
    y = current[1]

    for i in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):

        if (i == end):
            pathNumber += 1

        elif (i not in previousNodes) & (i[0] < max1) & (i[1] < max1) \
                & (i[0] >= 0) & (i[1] >= 0):

            newPastNodes = []
            newPastNodes.insert(0, current)
            for node in previousNodes:
                newPastNodes.append(node)
            nextNodes.append((i, newPastNodes))
        else:
            pass
    return nextNodes


if __name__ == '__main__':
    length = int(sys.argv[1])
    print(walk(length))
