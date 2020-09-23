import sys

def add_them_all(filename):
    sum = 0
    ### Your code here

    filename = open(filename, "r")

    for line in filename:
        sum = sum + int(line)

    ### End of your code
    return sum

if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))
    
# Needed to "cd" to week5 to test in the terminal