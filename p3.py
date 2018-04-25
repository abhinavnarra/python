# Demonstrate python program for even and odd numbers in given range.


#Take in the upper range limit and the lower range limit and store it in separate variables.

lower=eval(input("Enter the lower limit for the range:"))
upper=eval(input("Enter the upper limit for the range:"))

#Use a for-loop ranging from the lower range to the upper range limit.
for i in range(lower,upper+1):
    if(i%2!=0):  #Then use an if statement  to check whether the number is odd or not and print the number.
        print("The Odd numbers within the range of ", lower ,'and' , upper, 'are ',i)

print ('##############################################')
for i in range(lower,upper+1):
    if(i%2==0):#Then use an elif statement  to check whether the number is even or not and print the number.
        print("The even numbers within the range of ", lower ,'and' , upper, 'are ',i)
