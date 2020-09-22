import sys

def add_them_all(filename):
    sum = 0

    filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt']
    for filename in filenames:

        f = open(filename, "r")

    for line in f:
        sum = sum + int(line)

    return sum

if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))
    

#Could not remember exactly how you wanted the homework, but this commented code I *believe* will total each individual file, and not just the sum of all together

#filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt']
#for filename in filenames:

    #f = open(filename, "r")

    #for line in f:
        #sum = sum + int(line)