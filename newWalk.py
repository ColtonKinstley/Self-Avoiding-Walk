#Calculates all uninterrupted paths for a n^2 coordinate system
# See http://mathworld.wolfram.com/Self-AvoidingWalk.html

from sys import argv
from time import clock

PATHS = 0


def main():
    start = clock()  # gets the system clock current time as a float
    nodeList = []  # initialize a list of pathways/nodes

    primeNode = node(0, 1, [(0, 0)])  # this initializes the first node at (0,1) with the history of 0,0 we do this because
                                      # of the symmetry of the square for every path that is branched from 0,1 will have
                                      # an equal path from 1,0

    nodeList.append(primeNode)

    while nodeList:

        n = nodeList.pop()  # set n to the last node in the list while removing it from the list

        ns = branch(n, SIZE)  # this will be a list of the new points that are branched from n

        for i in testEndConditions(ns, SIZE):  # tests for
            nodeList.append(i)

    print(PATHS)
    print(clock() - start)


def branch(nd, size):

    previous = []
    previous += (nd.previousNodes)  # Get the previous node list
    previous.append((nd.x, nd.y))    # append the current position to previous nodes

    if (nd.x in (0, size)) or (nd.y in (0, size)):  # If the position is on the edge don't bother branching past it or back into
                                                    # the closed loop should save some cycles, i don't know...

        n1 = node(nd.x + 1, nd.y, previous)  # prime to go forward but this is wrong for the x = side length we can remove it later
        n2 = 0
        n3 = node(nd.x, nd.y + 1, previous)  # prime to go forward but this is wrong for the x = side length we can remove it later
        n4 = 0

        if (nd.x == size):  # if x is the side length/maximum don't increase it but do decrease it
            n1 = 0
            n2 = node(nd.x - 1, nd.y, previous)

        if (nd.y == size):  # if y is the side length/maximum don't increase it but do decrease it
            n3 = 0
            n4 = node(nd.x, nd.y - 1, previous)

    else:  # if x,y is not on the edge branch all directions
        n1 = node(nd.x + 1, nd.y, previous)
        n2 = node(nd.x - 1, nd.y, previous)
        n3 = node(nd.x, nd.y + 1, previous)
        n4 = node(nd.x, nd.y - 1, previous)

    # for i in n1,n2,n3,n4:
    #     if i != 0:
    #         print(i.x,i.y,i.previousNodes)

    return [n1, n2, n3, n4]


def testEndConditions(nodes, size):
    global PATHS
    for n in nodes:

        if (n == 0) or ((n.x, n.y) in n.previousNodes):  # drop if no node or if it ran into itself
            # if n != 0:
            #     print('Dropped')
            #     print(n.x, n.y, n.previousNodes)
            continue

        elif (n.x, n.y) == (size, size):  # drop if it hit the end of the path
            # print('full path')
            # print(n.x, n.y, n.previousNodes)
            PATHS += 2
            continue

        else:
            # print('recycled')
            # print(n.x, n.y, n.previousNodes)
            yield n


class node:
    def __init__(self, x, y, previous):
        self.x = x
        self.y = y
        self.previousNodes = previous  # list previous positions of the path


if __name__ == '__main__':
    global SIZE
    SIZE = int(argv[1])
    main()
