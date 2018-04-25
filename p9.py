# Python program to remove to every third element until list becomes empty
def removeThirdNumber(int_list):
     
    # list starts with 0 index
    pos = 3 - 1
    index = 0
    len_list = (len(int_list))
     
    # breaks out once the list becomes empty
    while len_list > 0: 
     
        index = (pos + index) % len_list#for first iteration 2%3 remainder 2 so element in 2nd index will be deleted and it will be continued untill the list become empty.
         
        # removes and prints the required element
        print(int_list.pop(index)) 
        len_list -= 1
 

nums = [1, 2, 3, 4] 
removeThirdNumber(nums)
