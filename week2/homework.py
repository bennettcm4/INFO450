import logging
logging.basicConfig(level=logging.DEBUG)

def squared_threes():
    return_value = []
    # YOUR CODE GOES HERE

    return_value = [value ** 2 for value in range(0,100,3)]
    
    # END SHOULDNT GO BEYOND HERE
    return return_value

if __name__ == "__main__":
    for x in squared_threes():
        print(x)
    
    # should print out all numbers between 0 and 99 (inclusive)
    # that are evenly divisible by 3, then squared
    # e.g
    # 9
    # 36
    # 81
    # ..... etc
