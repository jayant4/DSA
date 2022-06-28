'''
Reverse a given integer
'''

num = 123456789

def Reverse(num:int) -> int:
    
    temp = 0
    while(True):
        temp = (temp*10) + num%10
        num = num//10
        if(num == 0):break
    return temp

print(Reverse(num))
    

