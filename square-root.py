from math import sqrt

y = float(input("Enter a number to get squre root: "))
if y < 0:
    x = y
elif y == 0:  # else if condition
    x = 0
else:         # else condition
    x = sqrt(y)

print("result is ", x)
if x > 0:
    print ( "positive root correct")
elif x ==0:
    print ("zero == 0 not positive or negative")
else:
    print ("negative no root") 
# Output:
# Enter a number to get squre root: 9
# result is  3.0
# positive root correct

