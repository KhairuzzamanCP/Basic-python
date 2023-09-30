""" 
in,not, not in, is, is not
>, <, >=, <=,==, != 
or,and
 true,false
 """

a = int(input())
boss = False
if a> 9:
    print("5 ar besi hobe")
elif a== 5:
    print("5 ar soman")
else:
    print("5 ar kom hobe")

if boss is True:
    print("boss ajke asbe")
else:
    print("boss asbe na ")
if boss is not True:
    print("boss asbe na ")
else:
    print("boss ajke asbe")

coin = "head"
#nested conditions
if boss == True:
    print("boss you are joss")
    if coin == 'tail':
        print("batting")
    else:
        print("bowling")
        if 5>2 or boss!= True:
            print('do somsethings')
            if 8 % 2 == 0 and 5%2==1 :
                print("8 is even numbers")
            else:
                print('8 is not even')
else:
    print('boss is not joss')
    

 
