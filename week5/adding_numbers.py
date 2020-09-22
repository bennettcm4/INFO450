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
    
# filename takes a string
# will return sum
# You will open file, read through the file, make sure everything is an integer, add them all together, and return sum of that file
# 6? different files


#Totals each individual file

#filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt']
#for filename in filenames:

    #f = open(filename, "r")

    #for line in f:
        #sum = sum + int(line)