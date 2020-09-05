# Page 89
# Complete 5-10 on page 89 of your book by completing the following program:

def check_users(current_users, new_users):
    pass
    # YOUR CODE HERE

    new_list = []
    for current_user in current_users:
        new_list.append(current_user.lower())
    current_users = new_list

    for new_user in new_users:
        if new_user.lower() in current_users:
            print(f"{new_user} is an unavailable username. Please enter a new username.")
        else:
            print(f"{new_user} is an available username.")

if __name__ == "__main__":
    current_users = ['chris','haritha', 'sally', 'darnell', 'superman']
    new_users = ['george', 'ringo', 'superman', 'hannibal']
    check_users(current_users, new_users)

# Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. 
# If a username has not been used, print a message saying that the username is available. 
# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
# (To do this, you'll need to make a copy of current_users containing the lowercase versions of all existing users.)