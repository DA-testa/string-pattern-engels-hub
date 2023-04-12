# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    if "I" in input():
        pattern = input().strip()
        text = input().strip()
    else:
        f = open("tests/06", "r")
        pattern=f.readline().strip()
        text=f.readline()
        f.close()

    return (pattern, text)
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    #return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_hash(text):
    b=13
    q=256
    m=len(text)
    result=0
    for i in range(m):
        result = (b*result+ord(text[i])) % q
    return result


def get_occurrences(pattern, text):
    output =[]
    # this function should find the occurances using Rabin Karp alghoritm 
    for i in range(0, len(text)-len(pattern)+1):
        if get_hash(text[i:i+len(pattern)]) == get_hash(pattern):
            if text[i:i+len(pattern)] == pattern:
                output.append(i)
    # and return an iterable variable
    return output


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

