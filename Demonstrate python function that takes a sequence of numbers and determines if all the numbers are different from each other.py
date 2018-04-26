#Demonstrate python function that takes a sequence of numbers and determines if all the numbers are different from each other

def test_distinct(data):#defining function
  count = 0
  for k in data:
    for j in range(1, len(data) - 1):#for each value in data compares with the precinding value and return none if all the values are different from each other
      if k == j:
        count += 1
        if count == 2:#if the count value is 2 it will return False
          return False
          
print(test_distinct([2,4,5,7,9]))#returns None because all the values are different
print(test_distinct([2,4,5,5,7,9]))#returns False because it contains duplicate values
