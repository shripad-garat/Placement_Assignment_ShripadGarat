"""
Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
he can remove just one character at the index in the string, and the remaining characters will occur the same
number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .
Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
an explanation for the same.
Example input 1 - s = “abc”. This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }
Example output 1- YES
Example input 2 - s “abcc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves
character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }
Example output 2 - NO
"""

def counter(srt):
    try:
        """Counting the character frequency"""
        counter = list(srt)
        count = {}
        for ele in counter:
            if ele in count:
                count[ele] = count[ele] + 1
            else:
                count[ele] = 1
        return count

    except Exception as e:
        raise e
    
def isvalid(count):
    try:
        """Valaditing the given condition """
        valid = sorted(set(count.values()))
        if len(valid)==1:
            return "YES"
        elif len(valid)>2:
            return "NO"
        else:
            if valid[1]-1 == valid[0]:
                return "YES"
            else:
                return "NO"
    except Exception as e:
        raise e
    
def exe(srt):
    try:
        count = counter(srt=srt)
        valid = isvalid(count=count)
        return valid

    except Exception as e:
        raise e
    
srt = input("""Please Enter the string
For Example 
1.aabbccddeeffgghhijkllmmm
2.fzdgIgtjkb
3.aaabbbbkkklllppp""")
print(exe(srt=srt))