List1 = [56, 78, 34, 21, 56, 34, 45, 89, 75, 12, 56, 125]
#The list to be sorted
List1.sort()
print(List1)
#Finding the sum of the list
total = sum(List1)
print(total)
#Displaying the numbers Largest to Smallest
List1.reverse()
print(List1)
#List = List(re(List))
#Finding the largest in the list
print("The largest is ", max(List1))
#Finding the smallest in the list
print("The smallest is ", min(List1))
#Removing the Duplicated numbers
#quickest way to remove the duplicate in the list
myresult=list(set(List1))
#To display now the results without the duplicates
myresult.sort()
print(myresult)


















