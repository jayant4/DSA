'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''

"""
Algorithm: 
Using stack

1. Initialize an empty stack.

Loop on input string:
    2. Create a top variable, if stack is empty then give some arbitary value, if stack is not empty then give the top value of the stack.
    3. Check if the top is an opening bracket and if the inputstring[i] is the same pair of closing bracket. If so then pop element from stack
    4. If step 3 doesn't happen then insert the value in the stack
5. Return if the stack is empty

Result - If stack is empty then the input string contains valid parenthesis match otherwise it is an invalid parenthesis match.
"""


mystack = []
inputString = '{}({}[])'




def checkBrackets(inputStr: str) -> bool:
    doesMatch: bool = False
    for i in range(0, len(inputStr)):
        top:str = 0
        if(len(mystack)<=0):
            top = "#"
        else:
            top = mystack[len(mystack)-1]
            
        if(top == "(" and inputStr[i] == ")"):
            mystack.pop()
        elif(top == "[" and inputStr[i] == "]"):
            mystack.pop()
        elif(top == "{" and inputStr[i] == "}"):
            mystack.pop()
        else:
            mystack.append(inputStr[i])
    
    return len(mystack) == 0
        

if(checkBrackets(inputString)):
    print('Valid parenthesis')
else:
    print('Invalid parenthesis')


