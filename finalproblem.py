'''
we will be building a search engine
the input to the search engines indexing process will be a multi line string. imgaine thisd is the content of a book

the next step of a search engine is to supply a keyword and get the sentences that match. a sentence is defined as a string of characters, serperated by a period.

the 'index' function takes a 'str' parameter, finds all unqiue words and maps them to complete sentences.
the returned value shall be a 'dict' with the keys being each unque word in the original string and the values will be a list of full sentences that contain that string

the 'search' function takes two parameters. The first parameter is the 'index/dict' returned from the first function.
The second paramter is a 'keyword' that you should search for

the returned value should be a unique list of the original sentences that contain the 'keyword'

for this assignment, i am giving you a __main__ method. your job is to make it work. your functions should match my code and my code should execute without error

'''
def index(str):
    
    sentences = str.split(".")
    new_list = {}
    for sentence in sentences:
        sentence = sentence.strip('\n')
        words = sentence.split(" ")
        for word in words:
            if not word in new_list:
                new_list[word] = []
                new_list[word].append(sentence)
    return new_list
            

if __name__ == "__main__":
    full_string = """
    Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types,
    and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming. Python combines remarkable
    power with very clear syntax. It has interfaces to many system calls and libraries, as well as to various window systems, and is extensible in C or C++. It is also usuable
    as an extension language for applications that need a programmable interface. Finally, Python is portable: it runs on many Unix variants including Linux and macOS, and on
    Windows.
    """
    
    idx = index(full_string)
    # for x in idx:
    #  print(x)
    # print(len(idx))
    
    # print("Length should be 71")
    if len(idx) != 71:
        raise Exception("Length of idx should have 71 keywords.")
    
    res = search(idx, "unix")
    if len(res) != 1:
        raise Exception("Length of search results should have 1 line.")
    
    res = search(idx, "finally")
    if len(res) != 1:
        raise Exception("Length of search results should have 1 line.")   
        
    res = search(idx, "it")
    if len(res) != 5:
        raise Exception("Length of search results should have 5 line.")
        
    test_line = "Python is an interpreted, interactive, object-oriented programming language."
    res = search(idx, "Python")
    if len(res) != 3:
        raise Exception("Length of search results should have 3 line.")
    if test_line not in res:
        raise Exception("The original sentence is not in the results: {}".formate(test_line))
        
    res = search(idx, "as")
    if len(res) != 3:
        raise Exception("Length of search results should have 3 line.")