'''
Question 1: -
Write a program that takes a string as input, and counts the frequency of each word in the string, there might
be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
highest-frequency word.
Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
an explanation for the same.
Example input - string = “write write write all the number from from from 1 to 100”
Example output - 5
Explanation - From the given string we can note that the most frequent words are “write” and “from” and
the maximum value of both the values is “write” and its corresponding length is 5
'''

def find_and_count(srt):
    try:
        counter = srt.split()
        count = {}
        ## creating the  for loop to make dictory of count 
        for ele in counter:
            if ele in count:
                count[ele] = count[ele] + 1
            else:
                count[ele] = 1
        return len(max(zip(count.values(),count.keys()))[1]) ## returning the len of phrase which is frequently repeted 

    except Exception as e:
        raise e
    

srt = input("""Please Enter the string
For Example 
1. “write write write all the number from from from 1 to 100”
2. humpy dumpy dumpy setting on the dumpy
3. jjingle bell jjingle bell jjingle jjingle 
anything you got me right :)""")

print(find_and_count(srt=srt))