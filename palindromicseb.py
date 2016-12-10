
def ispalindrome(string):
    start = 0
    end = len(string) -1

    while(start <= end):
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

    return True



def longestpalisubstring(string):
    length = 0
    palidrome = ""

    for start_index in range(0,len(string)):
        for end_index in range(start_index ,len(string)):
            if(ispalindrome(string[start_index:end_index+1])):
                l = end_index - start_index + 1
                if length < l:
                    palidrome = string[start_index:end_index+1]
                    length = l

    print(length, palidrome)

longestpalisubstring("asdsade")
