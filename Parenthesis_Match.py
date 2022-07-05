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


dict = {
    '(': ')',
    '[': ']',
    '{': '}'
}


def checkBrackets(inputStr: str) -> bool:
    '''
    working solution
    but does not work for nested brackets like {[]} returns false
    '''

    for i in range(0, len(inputStr)-1):
        if(inputStr[i] == '('):
            if(inputStr[i+1] != dict['(']):
                return False
        elif(inputStr[i] == '['):
            if(inputStr[i+1] != dict['[']):
                return False
        elif(inputStr[i] == '{'):
            if(inputStr[i+1] != dict['{']):
                return False
    return True


inputString = '(){}[]'

# if(checkBrackets(inputString)):
#     print('Valid parenthesis')
# else:
#     print('Invalid parenthesis')


mystack = []
inputString2 = '{({}[])}'




def checkBrackets2(inputStr: str) -> bool:
    doesMatch: bool = False
    for i in range(0, len(inputStr)-1):
        if inputStr[i] in dict.keys():
            mystack.append(inputStr[i])
        
        if inputStr[i] in dict.values():
            x = mystack.pop()
            if(GetKey(inputStr[i]) == x):
                doesMatch = True
            else:
                return False
    
    return doesMatch
        
def GetKey(val):
   for key, value in dict.items():
      if val == value:
         return key

if(checkBrackets2(inputString2)):
    print('Valid parenthesis')
else:
    print('Invalid parenthesis')



