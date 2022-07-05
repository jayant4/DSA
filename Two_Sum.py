'''
Calculate 2 sum
Given an array of numbers, and a number return a pair of numbers which add up to the given number
'''

arr:int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 5
output = []
def TwoSum():
    for i in range(0,len(arr)):
        for j in range(0,len(arr) -1):
            if((i + j) == sum):
                output.append((i,j))
TwoSum()
print(output)