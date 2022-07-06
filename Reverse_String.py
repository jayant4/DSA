# Given an input string reverse it
inputString = "Hello World !!!"
myStack = []

def ReverseString(inputString : str) -> str:
    reverseStr = ""
    for i in inputString:
        myStack.append(i)

    for i in inputString:
        reverseStr += myStack.pop()
        pass

    return reverseStr
print(ReverseString(inputString))