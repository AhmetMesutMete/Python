# Queues and Stacks

# Problem: A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards. 
# Determine if a given string, s, is a palindrome.
import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.stackItems = []
        self.queueItems = []
    def pushCharacter(self, item):
        self.stackItems.append(item)
    def enqueueCharacter(self, item):
        self.queueItems.insert(0,item)
    def popCharacter(self):
        return self.stackItems.pop()
    def dequeueCharacter(self):
        if len(self.queueItems) > 0:
            return self.queueItems.pop()
        


# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")  
