"""
Find 2 elements in the array which give the sum
"""

arr = [1,2,3,4,5,6,7,8,9]
sum = 12



"""
Algo:
take 1 element loop through the array and check if their sum is equal to given sum then create a tuple and store it in the new out arr
"""

outputArr = []
for i in arr:
    for j in arr:
        if(i + j == sum):
            outputArr.append((i,j))

print(outputArr)
