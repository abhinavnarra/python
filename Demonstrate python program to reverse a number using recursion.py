#Demonstrate python program to reverse a number using recursion


num = int(input("Please Enter any Number: "))#asking user to enter a number
reverse = 0
def reverse_int(num):#defining reverse_int function
    global reverse#making reverse variable as global variable
    if(num > 0):#if (Number > 0) will check whether the number is greater than 0 or not. For Recursive functions it is very important to place a condition before using the function recursively otherwise, we will end up in infinite execution
        rem = num %10#store the reminder of the number
        reverse = (reverse *10) + rem
        reverse_int(num //10)#// operator always carries out floor division, it always truncates the fraction and moves to the left of the number line
    return reverse
reverse = reverse_int(num)#creating object
print("\n Reverse of entered number is {}" .format(reverse))#printing reversed number

