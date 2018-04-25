#Demonstrate python program that need to purchase 100 fruits by using 100 rupees (fruits apple -5$, orange - 1$, banana - 0.5$) need the combinations

#100=apple*5+orange*1+banana*0.5
temp=0
for apple in range(1,101):
    for orange in range(1,101):
        for banana in range(1,101):
            if 100==(5*apple)+(1*orange)+(0.5*banana):#if condition for calculating  the sum of prices of fruits is equal to 100
                if (apple+orange+banana)==100:#if condition for calculating the sum of fruits is equal to 100
                    print(apple,orange,banana)#to print all the possible combinations
                    temp+=1
print('the number of combinations to purchase 100 fruits by using 100 rupees is:  ',  temp)#to display no of combinations to purchase 100 fruits by using 100 rupees 


                              
