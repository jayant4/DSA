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

def ReverseString2(inputString : str) -> str:
    reverseStr = ""
    for i in range(len(inputString)-1,-1,-1):
        reverseStr += inputString[i]

    # for i in inputString:
    #     reverseStr += myStack.pop()
        pass

    return reverseStr
print(ReverseString2(inputString))