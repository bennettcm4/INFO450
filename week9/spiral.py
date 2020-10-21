import sys

size = 501

def print_square(square):
    direction = [(0,1),(1,0),(0,-1),(-1,0)] # Right, down, left, up
    directionindex = 0 # Current direction
    count = 1
    currentx = int((len(square) - 1) / 2) # Middle x
    currenty = int((len(square) - 1) / 2) # Middle y
    stepamount = 1 # How far to move in current direction
    currentstep = 0
    for y in range(len(square)):
        for x in range(len(square[y])):
            square[currentx][currenty] = count 
            currentx = currentx + direction[directionindex][0] # Move in current direction
            currenty = currenty + direction[directionindex][1] # Move in current direction
            currentstep += 1
            if currentstep == stepamount: # Changing direction 
                currentstep = 0 
                if directionindex == 3:
                    directionindex = 0
                else: 
                    directionindex += 1          
                if directionindex == 0 or directionindex == 2: # Incrementing the step amount
                    stepamount += 1

               
            count += 1

square = [[f"{x}.{y}" for x in range(size)] for y in range(size)]

#print_square(square)
#for row in square:
#    print(row)

# Got it to build the grid in a spiral pattern
# Could not figure out how to get diagonals