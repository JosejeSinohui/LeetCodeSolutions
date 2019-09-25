import random

# Simulates a random hit given a target for debugging purposes
def calculateHit(targets, target):
    # First checks if all of them are at 0 and returns "0 0" to emulate the testing tool
    done = True
    for v in targets.values():
        if v > 0:
            done = False
    if done:
        return "0 0"

    i = target[0]
    j = target[1]
    prepared_i = random.randint(i - 1, i + 1)
    prepared_j = random.randint(j - 1, j + 1)
    return "{} {}".format(prepared_i, prepared_j)


def findSquareDimentions(a):
    ## Find square optimal dimentions
    smallestDifference = 100000
    dimentions = (0,0)
    for i in range(1,a//2):
        if a % i == 0:
            x = a // i
            y = i
            if abs(x - y) < smallestDifference:
                if x < 3:
                    x = 3
                if y < 3:
                    y = 3
                dimentions = (x, y)
                smallestDifference = x - y
    return dimentions

# Gets the most optimal target square (the one with the less probability to miss)
def getBestTarget(targets):
    highest_missing_squares = -1
    for target, missing_squares in targets.items():
        if missing_squares > highest_missing_squares:
            highest_missing_squares = missing_squares
            best_target = target
    return best_target

# Given a hit (x,y) updates the counter on the targets that require it
def updateTargets(targets, x, y):
    for target in targets:
        if target[0] - 1 <= x <= target[0] + 1 and target[1] - 1 <= y <= target[1] + 1:
            targets[target] -= 1


# Test purposes
# t = 100
# total = 0
t = int(input())
for i in range(1, t+1):
    # Test purposes
    # a = 20
    a = int(input())
    max_x, max_y = findSquareDimentions(a) # X in 0, Y in 1

    # now we create a map of the places where we can deploy the gopher
    # and assigns them a starting scores of the number of squares
    # that haven't been marked yet
    # For example, for a = 16 we would get the dimensions of x=4 and y=4
    #   1 2 3 4 5 6
    # 1|0 0 0 0 0 0
    # 2|0 x x 0 0 0 
    # 3|0 x x 0 0 0 
    # 4|0 0 0 0 0 0 
    # 5|0 0 0 0 0 0

    # the places where 'x' it's the only places we would want to shoot, notice how the 0's
    # surrounding the x's form a 4x4 square
    targets = {} 
    for i in range(2, max_x):
        for j in range(2, max_y):
            targets[(i,j)] = 9


    alreadyHit = []
    x, y = -1, -1 
    hits = 0
    while not (x == 0 and y == 0):
        target = getBestTarget(targets)
        # Test purposes
        # hits+=1
        # hit = calculateHit(targets, target)
        print(str(target[0]) + " " + str(target[1]))
        hit = input()
        x = int(hit.split(" ")[0])
        y = int(hit.split(" ")[1])    
        if (x,y) not in alreadyHit:
            updateTargets(targets, x, y)
            alreadyHit.append((x,y))

    # total += hits

# Tests
# print("Average: " + str(total/t))
        