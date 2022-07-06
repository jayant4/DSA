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


mystack = []
inputString = '{}}({}[])'




def checkBrackets(inputStr: str) -> bool:
    doesMatch: bool = False
    for i in range(0, len(inputStr)):
        top = 0
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


"""
"""