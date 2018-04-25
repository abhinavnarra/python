#Demonstrate python program to input ‘n’ employee number and name and to display all employee’s information in ascending order based upon their number - dictionary method.




dict1={}
dict2={}
l=[]
No_of_employees=int(input("Enter No of Employees:"))#enter number of employees to be sorted

for i in range(1,No_of_employees+1):
    emp_id=input("Enter id:")
    name=input("Enter name:")
    dict1[emp_id]=name#storing the elements in a dictionary
print(dict1)#unsorted dictionary   
for i in dict1.keys():
    l.append(int(i))#appending the elements into a list

l.sort()#sorting the elements of the list
    
for i in l:#printing the employee number and name and to display all employee’s information in ascending order based upon their number .
    dict2[i]=dict1[str(i)]

print(dict2)#sorted dictionary

